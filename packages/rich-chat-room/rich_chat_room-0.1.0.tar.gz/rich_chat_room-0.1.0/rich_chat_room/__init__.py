from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text

__version__ = "0.1.0"

console = Console()

# You may adjust these constants as needed.
HEADER_HEIGHT = 3
CHAT_PANEL_BORDER = 2  # Top and bottom border of the chat panel.


def make_layout() -> Layout:
    """Creates the main layout with a header and a chat area."""
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=HEADER_HEIGHT), Layout(name="chat", ratio=1)
    )
    return layout


def render_header() -> Panel:
    """Renders the header panel."""
    header_text = Text("Chat Room", justify="center", style="bold white")
    return Panel(header_text, style="on blue")


def create_message_bubble(message: dict) -> Panel:
    """
    Creates a message bubble Panel based on the message dictionary.
    Long texts are automatically wrapped to multiple lines.
    """
    role = message.get("role", "unknown").lower()
    content = message.get("content", "")

    # Define bubble styling based on sender's role.
    if role == "user":
        bubble_style = "bold white on dark_green"
        title = ""  # User messages do not show a title.
    else:
        bubble_style = "white on dark_blue"
        title = role.capitalize()

    bubble = Panel(
        Text(content, justify="left", no_wrap=False, overflow="fold"),
        title=title,
        border_style=bubble_style,
        padding=(1, 2),
    )
    return bubble


def measure_renderable(renderable) -> int:
    """
    Returns the number of lines that the renderable will occupy
    when rendered in the current console.
    """
    # Use the current console options for measurement.
    options = console.options
    return sum(1 for _ in console.render_lines(renderable, options))


def render_chat(messages: list) -> Panel:
    """
    Renders the chat area by grouping message bubbles.
    Only the most recent messages that can fit into the available height are shown.
    User messages are aligned to the right, while others are aligned to the left.
    """
    # First, create an aligned bubble for each message.
    bubbles = []
    for msg in messages:
        role = msg.get("role", "unknown").lower()
        bubble = create_message_bubble(msg)
        aligned_bubble = (
            Align.right(bubble)
            if str(role).lower() in ("user", "me")
            else Align.left(bubble)
        )
        bubbles.append(aligned_bubble)

    # Determine the available height for the messages.
    # Total available height = Console height - header height - chat panel border lines.
    available_height = console.size.height - HEADER_HEIGHT - CHAT_PANEL_BORDER

    # Now, working from the last message upward, accumulate bubbles that fit.
    selected_bubbles = []
    total_height = 0
    # Iterate in reverse (latest messages first)
    for bubble in reversed(bubbles):
        h = measure_renderable(bubble)
        # If adding this bubble would exceed available height, stop.
        if total_height + h > available_height:
            break
        total_height += h
        selected_bubbles.insert(
            0, bubble
        )  # Insert at the beginning to keep chronological order

    chat_group = Group(*selected_bubbles)
    return Panel(chat_group, title="Chat", border_style="white")


def render_chat_room(messages: list) -> Layout:
    layout = make_layout()
    layout["header"].update(render_header())
    layout["chat"].update(render_chat(messages))
    return layout
