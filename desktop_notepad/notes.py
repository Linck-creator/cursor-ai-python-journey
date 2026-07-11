"""
Desktop Notepad - Tkinter Notes Editor

This module provides a clean, object-oriented Tkinter-based desktop application
for editing notes. It features opening, saving, and creating text notes, with
support for both Light and Dark Mode themes and a modern user interface.

Developed during the "Cursor AI + Python: Intelligent Development with AI" course
provided by Santander Open Academy.

Author: Felipe Coelho Linck
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os


class NotesEditor(tk.Tk):
    """
    The main NotesEditor application class.

    A modern Tkinter desktop notepad editor supporting:
    - Creating new notes
    - Opening and saving text files
    - Light and Dark Mode themes (toggle from menu)
    - Responsive modern layout with toolbar and scrollbar

    All GUI layout and interactions are encapsulated in this class.
    """

    def __init__(self):
        """
        Initialize the NotesEditor main window and all widgets.
        """
        super().__init__()

        # Configure main window properties
        self.title("Notes Editor")
        self.geometry("900x600")
        self.minsize(400, 300)

        # Theme state: False = light (default), True = dark
        self.dark_mode = False

        # Currently open file path (None if editor is untitled)
        self.current_file = None

        # Build full UI
        self._configure_layout()
        self._create_menu_bar()
        self._create_toolbar()
        self._create_text_widget()

        # Apply initial theme (light by default)
        self._apply_theme()

    def _configure_layout(self):
        """
        Configure the root grid layout for toolbar and text area.
        """
        self.grid_rowconfigure(1, weight=1)    # Text area expands vertically
        self.grid_columnconfigure(0, weight=1) # Editor fills width

    def _create_menu_bar(self):
        """
        Create the application menu bar: File (New/Open/Save/Exit), View (Toggle Dark Mode).
        """
        self.menu_bar = tk.Menu(self)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # View menu (dark mode toggle)
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self._dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        self.view_menu.add_checkbutton(
            label="Toggle Dark Mode",
            variable=self._dark_mode_var,
            command=self.toggle_dark_mode
        )
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        # Attach menu to main window
        self.config(menu=self.menu_bar)

    def _create_toolbar(self):
        """
        Create a toolbar above the text area with New, Open, and Save buttons.
        """
        self.toolbar = tk.Frame(self, bg="#f4f4f4", padx=10, pady=6, relief=tk.FLAT)
        self.toolbar.grid(row=0, column=0, sticky="ew")
        self.toolbar.grid_columnconfigure((0, 1, 2), weight=0)
        self.toolbar.grid_columnconfigure(3, weight=1)  # Fill to right edge

        # Common button style for consistency
        self._btn_style = {
            "font": ("Segoe UI Emoji", 11, "bold"),
            "bg": "#e8e8e8",
            "fg": "#333",
            "activebackground": "#d0d0d0",
            "activeforeground": "#1a1a1a",
            "width": 9,
            "bd": 0,
            "cursor": "hand2",
            "relief": tk.RAISED,
            "padx": 6,
            "pady": 4,
        }

        self.new_btn = tk.Button(
            self.toolbar,
            text="🆕  New",
            command=self.new_file,
            **self._btn_style
        )
        self.new_btn.grid(row=0, column=0, padx=(0, 6), pady=0)

        self.open_btn = tk.Button(
            self.toolbar,
            text="📂  Open",
            command=self.open_file,
            **self._btn_style
        )
        self.open_btn.grid(row=0, column=1, padx=(0, 6), pady=0)

        self.save_btn = tk.Button(
            self.toolbar,
            text="💾  Save",
            command=self.save_file,
            **self._btn_style
        )
        self.save_btn.grid(row=0, column=2, padx=(0, 6), pady=0)

    def _create_text_widget(self):
        """
        Create the multi-line text editing area with vertical scrollbar.
        """
        # Frame for text widget and vertical scrollbar
        self.text_frame = tk.Frame(self, padx=10, pady=6, bg="#fafbfc")
        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.text_frame.grid_rowconfigure(0, weight=1)
        self.text_frame.grid_columnconfigure(0, weight=1)

        self.text_widget = tk.Text(
            self.text_frame,
            wrap="word",
            font=("Consolas", 12),
            undo=True,
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="#ddd"
        )
        self.text_widget.grid(row=0, column=0, sticky="nsew")

        # Modern-looking vertical scrollbar
        self.vsb = tk.Scrollbar(
            self.text_frame,
            orient="vertical",
            command=self.text_widget.yview
        )
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.text_widget.config(yscrollcommand=self.vsb.set)

    def new_file(self):
        """
        Clear the text area for a new untitled file.
        Prompts the user if there are unsaved changes.
        """
        if self._confirm_unsaved_changes():
            self.text_widget.delete(1.0, tk.END)
            self.current_file = None
            self.title("Notes Editor")

    def open_file(self):
        """
        Open a text file selected by the user and display its contents.
        Prompts for unsaved changes before opening.
        """
        if not self._confirm_unsaved_changes():
            return
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
                self.current_file = file_path
                self.title(f"Notes Editor - {self._get_filename(file_path)}")
            except Exception as exc:
                messagebox.showerror("Error", f"Failed to open file:\n{exc}")

    def save_file(self):
        """
        Save the content of the text editor to a file.
        If the file is new, prompt the user for a location.
        """
        if self.current_file:
            file_path = self.current_file
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not file_path:
                return  # User canceled dialog

        try:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content.rstrip('\n'))  # Remove trailing newlines
            self.current_file = file_path
            self.title(f"Notes Editor - {self._get_filename(file_path)}")
        except Exception as exc:
            messagebox.showerror("Error", f"Failed to save file:\n{exc}")

    def exit_app(self):
        """
        Exit the application.
        Prompts to save unsaved changes if needed.
        """
        if self._confirm_unsaved_changes():
            self.destroy()

    def _confirm_unsaved_changes(self):
        """
        Check for unsaved changes and prompt the user to save if necessary.

        Returns:
            bool: True if it's safe to proceed (no unsaved changes, or user chose to save/discard).
                  False if the user canceled.
        """
        if self._is_text_modified():
            answer = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save them?"
            )
            if answer:  # Yes
                self.save_file()
                return True
            if answer is None:  # Cancel
                return False
            # No (= discard changes)
            return True
        return True

    def _is_text_modified(self):
        """
        Determine if the text widget's content has unsaved modifications.

        Returns:
            bool: True if the content differs from the last saved state, or
                  if this is a new file with non-blank text.
        """
        current_content = self.text_widget.get(1.0, tk.END).rstrip('\n')
        if self.current_file:
            try:
                with open(self.current_file, "r", encoding="utf-8") as file:
                    saved_content = file.read().rstrip('\n')
                return current_content != saved_content
            except Exception:
                # If the file cannot be read, assume modified for safety
                return True
        return bool(current_content.strip())  # New file & non-blank

    def _get_filename(self, path):
        """
        Extract just the filename from a full file path.

        Args:
            path (str): The full filesystem path.

        Returns:
            str: The filename portion.
        """
        return os.path.basename(path)

    def toggle_dark_mode(self):
        """
        Toggle between Dark and Light mode for the editor and update the UI.
        """
        self.dark_mode = not self.dark_mode
        self._dark_mode_var.set(self.dark_mode)
        self._apply_theme()

    def _apply_theme(self):
        """
        Apply color scheme and styles for Dark or Light mode to all widgets.
        """
        if self.dark_mode:
            # ---- Dark Mode colors ----
            bg = "#23272e"
            fg = "#e0eaee"
            toolbar_bg = "#23272e"
            toolbar_btn_bg = "#323844"
            toolbar_btn_fg = "#e0eaee"
            toolbar_btn_abg = "#475063"
            toolbar_btn_afg = "#f6f6fa"
            text_bg = "#20232a"
            text_fg = "#e0eaee"
            text_highlight = "#404652"
            scroll_bg = "#282c34"
            frame_bg = "#20232a"
            select_bg = "#536084"
        else:
            # ---- Light Mode colors (default) ----
            bg = "#fafbfc"
            fg = "#181b1f"
            toolbar_bg = "#f4f4f4"
            toolbar_btn_bg = "#e8e8e8"
            toolbar_btn_fg = "#333"
            toolbar_btn_abg = "#d0d0d0"
            toolbar_btn_afg = "#1a1a1a"
            text_bg = "#fafbfc"
            text_fg = "#222"
            text_highlight = "#ddd"
            scroll_bg = "#dddddd"
            frame_bg = "#fafbfc"
            select_bg = "#a7cfff"

        # Main window background
        self.configure(bg=bg)

        # Toolbar + its buttons
        self.toolbar.config(bg=toolbar_bg)
        for btn in (self.new_btn, self.open_btn, self.save_btn):
            btn.config(
                bg=toolbar_btn_bg,
                fg=toolbar_btn_fg,
                activebackground=toolbar_btn_abg,
                activeforeground=toolbar_btn_afg,
            )

        # Editor frame and text widget
        self.text_frame.config(bg=frame_bg)
        self.text_widget.config(
            bg=text_bg,
            fg=text_fg,
            insertbackground=fg,  # caret color
            selectbackground=select_bg,
            selectforeground=text_fg,
            highlightbackground=text_highlight,
            highlightcolor=text_highlight
        )

        # Update scrollbar (note: appearance may depend on OS theme)
        try:
            self.vsb.config(bg=scroll_bg, troughcolor=bg)
        except Exception:
            pass

        # Update menu bar colors if applicable
        try:
            self.menu_bar.config(bg=toolbar_bg, fg=toolbar_btn_fg)
        except Exception:
            pass


if __name__ == "__main__":
    app = NotesEditor()
    app.mainloop()