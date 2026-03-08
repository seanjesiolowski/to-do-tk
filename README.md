# tk-todo

A minimal to-do app built with Python and Tkinter.

The UI was designed in [Figma](https://www.figma.com/) and converted to Tkinter code using [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer), then customized from there.

<p align="center">
  <img src="screenshots/no-tasks.png" width="250" alt="Empty state">
  &nbsp;&nbsp;
  <img src="screenshots/tasks.png" width="250" alt="With tasks">
</p>

## Requirements

- Python 3.10+
- Tkinter (included with standard Python distributions)

## Quick Start

```bash
python app.py
```

## Usage

| Action | Effect |
|---|---|
| Type + Enter | Add a new item |
| Click an item | Toggle done (strikethrough) |
| Right-click an item | Delete it |
| Shift+click an item | Select/deselect for reordering |
| Arrow keys | Move the selected item up/down |
| Clear all button | Remove all items |
