# VimLM - LLM-powered Vim assistant

## Features

- Real-time code assistance using local LLMs
- Context-aware suggestions based on your current file
- Split-window interface showing LLM responses
- Simple keybinding integration with Vim
- Works completely offline with local models

## Installation

```zsh
pip install vimlm
```

## Usage

1. Start Vim with VimLM:

```zsh
vimlm your_file.js
```

2. Use the key bindings in Vim:
- `Ctrl-L` in normal mode: Get suggestions for current line
- `Ctrl-L` in visual mode: Get suggestions for selected code

The LLM response will appear in a split window on the right side of your Vim interface.

## Demo

![vimlm](https://github.com/user-attachments/assets/4aa39efe-aa6d-4363-8fe1-cf964d7f849c)


