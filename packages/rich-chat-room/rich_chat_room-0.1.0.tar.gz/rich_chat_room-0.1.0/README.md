# rich-chat-room

rich-chat-room is a modern, dynamic chat interface built using Python and the [Rich](https://github.com/Textualize/rich) library. It provides a visually appealing command-line interface that displays chat messages in a structured and colorful layout.

## Overview

This project demonstrates how to leverage the Rich library to create a chat room experience in the terminal. It supports features like:

- **Dynamic Layout:** Automatically splits the terminal into header and chat areas.
- **Message Bubbles:** Displays messages with distinct styles based on the sender.
- **Adaptive Rendering:** Only renders the most recent messages that fit within the visible terminal window.

## Installation

Ensure you are using Python 3.9 or later (but less than 4.0).

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/rich-chat-room.git
   cd rich-chat-room
   ```

2. **Install Dependencies:**

   You can install the required dependency `rich` via pip:

   ```bash
   pip install rich
   ```

   Alternatively, if you prefer using Poetry:

   ```bash
   poetry install
   ```

## Usage

To integrate and use the chat room in your application, import the module and call the `render_chat_room` function with a list of messages. For example:

```python
from rich_chat_room import render_chat_room
from rich.console import Console

console = Console()

# Example messages
messages = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing great, thanks for asking!"}
]

# Render the chat room layout
layout = render_chat_room(messages)

# Clear the terminal and display the layout
console.clear()
console.print(layout)
```

This snippet will render a chat room with a header and the provided messages, automatically aligning user and assistant messages appropriately.

## Testing

Tests for the chat room functionality are included using [pytest](https://docs.pytest.org/). To run the tests, simply execute:

```bash
pytest
```

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or additional features, feel free to open an issue or submit a pull request.

## License

rich-chat-room is open-source software released under the [MIT License](./LICENSE).
