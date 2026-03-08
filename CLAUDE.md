# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
python app.py
```

Requires Python 3.10+ with Tkinter (included in standard Python distributions). No external dependencies.

## Architecture

This is a single-file Tkinter to-do app (`app.py`). All logic—UI setup, event handling, and state management—lives in one file with module-level globals.

**State:** Two globals drive the app: `item_list` (list of dicts with `text`, `done`, `selected` keys) and `selected_idx` (index of item selected for reordering, or `None`).

**Rendering:** `render_items()` is the single render function—it clears all canvas items tagged `"item"` and redraws from `item_list`. Every mutation to `item_list` must call `render_items()` afterward. Crossed-off items use `overstrike` font, selected items use `underline` font.

**Interactions:**
- Left-click toggles crossed-off state
- Right-click deletes (with confirmation dialog)
- Shift+left-click selects/deselects an item for reordering
- Up/Down arrow keys move the selected item in the list (wraps around)
- Enter key adds the entry text as a new item

**Constraints:** Max 7 items, max 21 characters per item. These are enforced in `add_to_list()`.

**Assets:** `assets/entry_1.png` is the entry field background image. The path is resolved relative to `app.py` via `ASSETS_PATH`.
