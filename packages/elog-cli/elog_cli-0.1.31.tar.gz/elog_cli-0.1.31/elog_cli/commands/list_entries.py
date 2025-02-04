import os
import curses
import click
from elog_cli.auth_manager import AuthManager
from elog_cli.hl_api import ElogAPIError, ElogApi
from elog_cli.elog_management_backend_client.types import Unset
from elog_cli.elog_management_backend_client.models import EntrySummaryDTO, EntryDTO
from datetime import datetime, timezone

def convert_to_local(utc_dt: datetime) -> datetime:
    # If the datetime is naive, assume it's in UTC.
    if utc_dt.tzinfo is None:
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
    # Convert to local time. This automatically detects the system's timezone.
    local_dt = utc_dt.astimezone()
    return local_dt

def get_full_entry(elog_api:ElogApi, entry_id:str)->EntryDTO:
    return elog_api.get_full_entry(entry_id)

def print_main_info(entry: EntryDTO, stdscr, y, max_lines, attr=curses.A_NORMAL):
    lines = [
        f"ID: {entry.id}",
        f"Title: {entry.title}",
        f"Content: {entry.text}",
        f"Event At: {entry.event_at}",
        f"Created At: {entry.logged_at}",
        f"Author: {entry.logged_by}",
    ]
    rows, cols = stdscr.getmaxyx()
    max_width = cols - 1
    for line in lines:
        if y < max_lines:
            stdscr.addnstr(y, 0, line, max_width, attr)
            y += 1
    return y

def print_additional_info(entry: EntryDTO, stdscr, y, max_lines, attr=curses.A_NORMAL):
    lines = []
    if not isinstance(entry.tags, Unset) and len(entry.tags) > 0:
        lines.append(f"Tags: {', '.join(tag.name for tag in entry.tags)}")
    if not isinstance(entry.references, Unset) and len(entry.references) > 0:
        lines.append(f"References: {', '.join(ref.id for ref in entry.references)}")
    if not isinstance(entry.referenced_by, Unset) and len(entry.referenced_by) > 0:
        lines.append(f"Referenced By: {', '.join(ref.id for ref in entry.referenced_by)}")
    if not isinstance(entry.follow_ups, Unset) and len(entry.follow_ups) > 0:
        lines.append(f"Follow Ups: {', '.join(fup.id for fup in entry.follow_ups)}")
    if not isinstance(entry.following_up, Unset) and len(entry.following_up) > 0:
        lines.append(f"Following Up: {', '.join(fup.id for fup in entry.following_up)}")
    if not isinstance(entry.history, Unset) and len(entry.history) > 0:
        lines.append(f"History: {', '.join(hist.id for hist in entry.history)}")
    if not isinstance(entry.superseded_by, Unset):
        lines.append(f"Superseded By: {entry.superseded_by.id}")
    if not isinstance(entry.attachments, Unset) and len(entry.attachments) > 0:
        lines.append(f"Attachments: {', '.join(att.file_name for att in entry.attachments)}")
    rows, cols = stdscr.getmaxyx()
    max_width = cols - 1
    for line in lines:
        if y < max_lines:
            stdscr.addnstr(y, 0, line, max_width, attr)
            y += 1
    return y

def print_entry_info(entry: EntryDTO, stdscr, max_lines, attr=curses.A_NORMAL):
    y = 0
    y = print_main_info(entry, stdscr, y, max_lines, attr)
    if y < max_lines:
        stdscr.addnstr(y, 0, "", stdscr.getmaxyx()[1] - 1, attr)  # blank line separator
        y += 1
    y = print_additional_info(entry, stdscr, y, max_lines, attr)
    return y

def truncate_middle(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s.ljust(max_len)
    part_len = (max_len - 3) // 2
    remainder = (max_len - 3) % 2
    first_part = s[:part_len + remainder]
    second_part = s[-part_len:]
    return (first_part + "..." + second_part).ljust(max_len)

def format_author(author: str, max_len: int) -> str:
    inner_width = max_len - 2  # account for '[' and ']'
    if len(author) <= inner_width:
        return "[" + author.ljust(inner_width) + "]"
    if inner_width <= 3:
        return "[" + author[:inner_width] + "]"
    part_len = (inner_width - 3) // 2
    remainder = (inner_width - 3) % 2
    truncated = author[:part_len + remainder] + "..." + author[-part_len:]
    return "[" + truncated.ljust(inner_width) + "]"

def format_info(entry:EntrySummaryDTO) -> str:
    return "[{}{}{}{}{}{}{}]".format(has_text(entry), has_attachment(entry),is_supersede(entry),is_reference_to(entry), is_referred(entry), is_follow_up(entry), is_followed_up(entry))

def has_text(entry:EntrySummaryDTO) -> str:
    return "T" if entry.is_empty is False else "-"
def has_attachment(entry:EntrySummaryDTO) -> str:
    return "A" if entry.attachments else "-"
def is_supersede(entry:EntrySummaryDTO) -> str:
    return "S" if entry.is_supersede else "-"
def is_reference_to(entry:EntrySummaryDTO) -> str:
    return "R" if entry.references else "-"
def is_referred(entry:EntrySummaryDTO) -> str:
    return "r" if entry.referenced_by else "-"
def is_follow_up(entry:EntrySummaryDTO) -> str:
    return "F" if entry.follow_ups else "-"
def is_followed_up(entry:EntrySummaryDTO) -> str:
    return "f" if entry.following_up else "-"

@click.command()
@click.pass_context
def list_entries(ctx):
    """List all entries."""
    elog_api: ElogApi = ctx.obj["elog_api"]  # Retrieve shared ElogApi
    auth_manager: AuthManager = ctx.obj["auth_manager"]  # Retrieve shared AuthManager
    elog_api.set_authentication_token(auth_manager.get_access_token())  # Set the authentication token

    def main(stdscr):
        # Hide the cursor for a cleaner view.
        curses.curs_set(0)
        curses.mousemask(curses.ALL_MOUSE_EVENTS)
        stdscr.timeout(20000)  # Set timeout to 20 seconds for auto-update check.

        scroll_offset = 0              # Index of the first visible item
        selected_index = 0             # Global index of the currently selected item
        rows, cols = stdscr.getmaxyx()
        visible_count = rows - 2  # Reserve bottom line for instructions
        loading = False                # Flag to indicate a page is currently loading
        auto_update_enabled = True     # New variable to control auto-update

        # Load an initial page of items (load extra for smoother scrolling)
        

        # Initialize color pairs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.use_default_colors()
        curses.init_pair(3, curses.COLOR_YELLOW, -1)

        def fetch_entries_page(count:int, anchor:str = None, next:bool=True):
            nonlocal loading, visible_count, cols
            loading = True
            # Show loading indicator immediately
            stdscr.addnstr(visible_count + 1, 0, "Loading new entries...", cols - 1, curses.A_BLINK | curses.A_BOLD)
            stdscr.refresh()
            try:
                new_page = elog_api.list_entries(limit=count, anchor=anchor) if next else elog_api.list_entries(context=count, anchor=anchor, next=False)
                return new_page
            except ElogAPIError as e:
                raise click.ClickException(e)
            finally:
                loading = False

        items: list[EntrySummaryDTO] = fetch_entries_page(visible_count + 10)
        while True:
            stdscr.clear()
            # Dynamically get screen dimensions
            rows, cols = stdscr.getmaxyx()
            visible_count = rows - 2
            
            end_index = scroll_offset + visible_count
            visible_items = items[scroll_offset:end_index]

            # Render visible items using dynamic cols value
            for idx, item in enumerate(visible_items):
                global_idx = scroll_offset + idx
                attr = curses.A_REVERSE if global_idx == selected_index else curses.A_NORMAL
                date_str = "[{}]".format(item.logged_at)
                max_author_len = 20
                padded_author = format_author(str(item.logged_by), max_author_len)
                padded_info = format_info(item)
                title_str = "{}".format(item.title)
                # Compute positions:
                pos_date = 0
                pos_author = pos_date + len(date_str)
                pos_info = pos_author + 1 + max_author_len
                pos_title = pos_info + 1 + len(padded_info)
                # Render each part:
                stdscr.addstr(idx, pos_date, date_str, attr | curses.color_pair(1))
                stdscr.addstr(idx, pos_author, " " + padded_author, attr | curses.color_pair(2))
                stdscr.addstr(idx, pos_info, " " + padded_info, attr)
                stdscr.addstr(idx, pos_title, " " + title_str, attr)

            stdscr.addstr(visible_count, 0,
                          "Use UP/DOWN keys or mouse wheel to scroll, [q] to quit, [f] to force refresh.")
            # Show a loading indicator if a new API fetch is in progress.
            if loading:
                stdscr.addnstr(visible_count + 1, 0, "Loading new entries...", cols - 1, curses.A_BLINK | curses.A_BOLD)
            stdscr.refresh()

            key = stdscr.getch()

            # If no key is pressed within 20 seconds.
            if key == -1:
                if auto_update_enabled:
                    # Auto-update: fetch new first page.
                    new_items = fetch_entries_page(visible_count + 10)
                    # If new_items differ (e.g. new element inserted), update list.
                    if new_items and new_items[0].id != items[0].id:
                        items = new_items
                        scroll_offset = 0
                        selected_index = 0
                continue

            # If any key is pressed, disable auto-update when mouse is moved.
            if key == curses.KEY_MOUSE:
                try:
                    _, mx, my, _, bstate = curses.getmouse()
                except Exception:
                    continue
                # On any mouse event, stop auto-update.
                auto_update_enabled = False
                # Process mouse events as before.
                if bstate & curses.BUTTON1_CLICKED:
                    if 0 <= my < visible_count:
                        selected_index = scroll_offset + my
                elif bstate & curses.BUTTON4_PRESSED:
                    if selected_index > 0:
                        if selected_index > scroll_offset:
                            selected_index -= 1
                        elif scroll_offset > 0:
                            scroll_offset -= 1
                            selected_index -= 1
                        else:
                            curses.beep()
                    else:
                        curses.beep()
                elif bstate & curses.BUTTON5_PRESSED:
                    if selected_index == scroll_offset + visible_count - 1:
                        if selected_index == len(items) - 1:
                            loading = True
                            anchor = items[-1].id
                            try:
                                new_items = fetch_entries_page(visible_count+10, anchor=anchor)
                            except ElogAPIError as e:
                                stdscr.addstr(visible_count + 1, 0, f"Error: {e}")
                                stdscr.getch()
                                loading = False
                                continue
                            loading = False
                            curses.flushinp()
                            if new_items:
                                items.extend(new_items)
                                scroll_offset += 1
                                selected_index += 1
                            else:
                                curses.beep()
                        else:
                            scroll_offset += 1
                            selected_index += 1
                    else:
                        if selected_index < len(items) - 1:
                            selected_index += 1
                        else:
                            curses.beep()
                continue

            # If user presses 'f', force refresh: re-enable auto-update, update list and go to top.
            if key == ord('f'):
                auto_update_enabled = True
                items = fetch_entries_page(visible_count + 10)
                scroll_offset = 0
                selected_index = 0
                continue

            if key == ord("q"):
                break
            elif key in (10, curses.KEY_ENTER):
                selected_entry = items[selected_index]
                full_entry = get_full_entry(elog_api, selected_entry.id)
                stdscr.clear()  # clear full screen before showing entry info
                print_entry_info(full_entry, stdscr, visible_count - 1, curses.color_pair(3))
                stdscr.addnstr(visible_count - 1, 0, "Press ESC to return", cols - 1, curses.color_pair(3))
                stdscr.refresh()
                while True:
                    k = stdscr.getch()
                    if k == 27:  # ESC key
                        break
                continue

            # Ignore new input while a page is loading.
            if loading:
                continue

            elif key == curses.KEY_DOWN:
                if selected_index == scroll_offset + visible_count - 1:
                    if selected_index == len(items) - 1:
                        anchor = items[-1].id
                        new_items = fetch_entries_page(visible_count + 10, anchor=anchor)
                        curses.flushinp()  # Flush queued key/mouse events.
                        if new_items:
                            items.extend(new_items)
                            scroll_offset += 1
                            selected_index += 1
                        else:
                            curses.beep()
                    else:
                        scroll_offset += 1
                        selected_index += 1
                else:
                    if selected_index < len(items) - 1:
                        selected_index += 1
                    else:
                        curses.beep()

            elif key == curses.KEY_UP:
                if selected_index > 0:
                    if selected_index > scroll_offset:
                        selected_index -= 1
                    else:
                        if scroll_offset > 0:
                            scroll_offset -= 1
                            selected_index -= 1
                        else:
                            curses.beep()
                else:
                    curses.beep()

            elif key == curses.KEY_MOUSE:
                try:
                    _, mx, my, _, bstate = curses.getmouse()
                except Exception:
                    continue

                # Handle left-click to select the entry under the mouse.
                if bstate & curses.BUTTON1_CLICKED:
                    if 0 <= my < visible_count:
                        selected_index = scroll_offset + my
                # Mouse wheel up (BUTTON4_PRESSED) simulates Up arrow.
                elif bstate & curses.BUTTON4_PRESSED:
                    if selected_index > 0:
                        if selected_index > scroll_offset:
                            selected_index -= 1
                        else:
                            if scroll_offset > 0:
                                scroll_offset -= 1
                                selected_index -= 1
                            else:
                                curses.beep()
                    else:
                        curses.beep()
                # Mouse wheel down (BUTTON5_PRESSED) simulates Down arrow.
                elif bstate & curses.BUTTON5_PRESSED:
                    if selected_index == scroll_offset + visible_count - 1:
                        if selected_index == len(items) - 1:
                            anchor = items[-1].id
                            new_items = fetch_entries_page(visible_count + 10, anchor=anchor)
                            curses.flushinp()
                            if new_items:
                                items.extend(new_items)
                                scroll_offset += 1
                                selected_index += 1
                            else:
                                curses.beep()
                        else:
                            scroll_offset += 1
                            selected_index += 1
                    else:
                        if selected_index < len(items) - 1:
                            selected_index += 1
                        else:
                            curses.beep()
            elif key == curses.KEY_RESIZE:
                rows, cols = stdscr.getmaxyx()
                visible_count = rows - 2
                # If there are not enough items to fill the screen, attempt to load next page.
                if len(items) < scroll_offset + visible_count and len(items) > 0:
                    anchor = items[-1].id
                    new_items = fetch_entries_page(visible_count + 10, anchor=anchor)
                    if new_items:
                        items.extend(new_items)
                if selected_index < scroll_offset:
                    scroll_offset = selected_index
                continue

    try:
        curses.wrapper(main)
    finally:
        # At the end of the command, ensure the cursor is made visible again.
        # The ANSI escape sequence "\033[?25h" shows the cursor.
        click.echo("\033[?25h", nl=False)
        # Reset the terminal to a sane state.
        os.system('stty sane')
if __name__ == "__main__":
    list_entries()