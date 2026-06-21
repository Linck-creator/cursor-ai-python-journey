import tkinter as tk
from tkinter import filedialog, messagebox

class NotesEditor(tk.Tk):
    """
    A Tkinter-based Notes Editor desktop application.
    Allows users to write, open, and save text files with ease.
    Now supports Light and Dark Mode.
    """
    def __init__(self):
        super().__init__()

        # Set the main window properties
        self.title("Notes Editor")
        self.geometry("900x600")
        self.minsize(400, 300)

        # Theme state: True = dark, False = light. Default is light.
        self.dark_mode = False

        # Initialize the current open file path
        self.current_file = None

        # Use a grid-based modern layout
        self._configure_layout()

        # Configure the menu bar
        self._create_menu_bar()

        # Configure the toolbar
        self._create_toolbar()

        # Configure the text area
        self._create_text_widget()

        # Apply the initial (light) theme
        self._apply_theme()

    def _configure_layout(self):
        # Root grid layout (toolbar row, text area row)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def _create_menu_bar(self):
        """
        Create the menu bar with File and View operations.
        """
        self.menu_bar = tk.Menu(self)

        # --- File menu ---
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # --- View menu ---
        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self._dark_mode_var = tk.BooleanVar(value=self.dark_mode)
        self.view_menu.add_checkbutton(
            label="Toggle Dark Mode",
            variable=self._dark_mode_var,
            command=self.toggle_dark_mode,
        )
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)

        self.config(menu=self.menu_bar)

    def _create_toolbar(self):
        """
        Create a toolbar above the text area with action buttons.
        """
        self.toolbar = tk.Frame(self, bg="#f4f4f4", padx=10, pady=6, relief=tk.FLAT)
        self.toolbar.grid(row=0, column=0, sticky="ew")
        self.toolbar.grid_columnconfigure((0, 1, 2), weight=0)
        self.toolbar.grid_columnconfigure(3, weight=1)  # Fill to right edge

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
            "pady": 4
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
        Create a multi-line Text widget that fills the window.
        """
        # Inner frame for text widget + scrollbar, with padding for modern look
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

        # Add modern-looking vertical scrollbar
        self.vsb = tk.Scrollbar(
            self.text_frame,
            orient="vertical",
            command=self.text_widget.yview
        )
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.text_widget.config(yscrollcommand=self.vsb.set)

    def new_file(self):
        """
        Clear the text area for a new file.
        """
        if self._confirm_unsaved_changes():
            self.text_widget.delete(1.0, tk.END)
            self.current_file = None
            self.title("Notes Editor")

    def open_file(self):
        """
        Open a text file and display its content in the text widget.
        """
        if not self._confirm_unsaved_changes():
            return
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
                self.current_file = file_path
                self.title(f"Notes Editor - {self._get_filename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def save_file(self):
        """
        Save the content of the text widget to a file.
        """
        if self.current_file:
            file_path = self.current_file
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            )
            if not file_path:
                return  # User canceled save dialog

        try:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content.rstrip('\n'))  # Remove extra blank at end
            self.current_file = file_path
            self.title(f"Notes Editor - {self._get_filename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

    def exit_app(self):
        """
        Exit the application, prompting to save unsaved changes.
        """
        if self._confirm_unsaved_changes():
            self.destroy()

    def _confirm_unsaved_changes(self):
        """
        Confirm and prompt the user if there are unsaved changes.
        Returns True if it's OK to proceed, False to cancel the action.
        """
        if self._is_text_modified():
            answer = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save them?"
            )
            if answer:  # Yes
                self.save_file()
                return True
            elif answer is None:  # Cancel
                return False
            else:  # No
                return True
        return True

    def _is_text_modified(self):
        """
        Check if the text widget content has unsaved modifications.
        """
        # Compare current content with saved file content
        current_content = self.text_widget.get(1.0, tk.END).rstrip('\n')
        if self.current_file:
            try:
                with open(self.current_file, "r", encoding="utf-8") as f:
                    saved_content = f.read().rstrip('\n')
                return current_content != saved_content
            except Exception:
                # If file can't be read, treat as modified
                return True
        else:
            # If new file and something has been typed
            return bool(current_content.strip())

    def _get_filename(self, path):
        """
        Get the filename from the full path.
        """
        import os
        return os.path.basename(path)

    def toggle_dark_mode(self):
        """Toggle between Dark and Light mode and update UI."""
        self.dark_mode = not self.dark_mode
        self._dark_mode_var.set(self.dark_mode)
        self._apply_theme()

    def _apply_theme(self):
        """Apply colors/styles for dark or light mode"""
        if self.dark_mode:
            # Dark mode colors
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
        else:
            # Light mode colors (originals)
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

        # Window bg
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

        # Toolbar frame (ignore column-3 filler)
        # Frame containing text and scrollbar
        self.text_frame.config(bg=frame_bg)
        # Text widget
        self.text_widget.config(
            bg=text_bg,
            fg=text_fg,
            insertbackground=fg,  # Cursor
            selectbackground="#536084" if self.dark_mode else "#a7cfff",
            selectforeground=text_fg,
            highlightbackground=text_highlight,
            highlightcolor=text_highlight
        )
        # Update scrollbar bg if desired (not always visible in native OS widgets)
        try:
            self.vsb.config(bg=scroll_bg, troughcolor=bg)
        except Exception:
            pass

        # Update menu colors if possible
        try:
            self.menu_bar.config(bg=toolbar_bg, fg=toolbar_btn_fg)
        except Exception:
            pass

if __name__ == "__main__":
    app = NotesEditor()
    app.mainloop()