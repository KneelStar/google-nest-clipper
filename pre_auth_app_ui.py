import tkinter as tk
from tkinter import messagebox
from nest_clipper_backend import NestClipperBackend


class PreAuthNestClipperApp:
    def __init__(self, root):
        self.root = root
        self.backend = NestClipperBackend()
        self.email_entry = None
        self.app_password_entry = None
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Nest Clipper")
        self.root.geometry("400x220")
        self.root.configure(bg="#f2f2f2")

        # Title label
        title_label = tk.Label(
            self.root,
            text="Nest Clipper",
            font=("Helvetica", 16, "bold"),
            fg="#333333",
            bg="#f2f2f2",
            pady=10,
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Email label and entry
        tk.Label(
            self.root,
            text="Email:",
            font=("Helvetica", 10),
            bg="#f2f2f2",
        ).grid(row=1, column=0, padx=(20, 10), sticky="e")
        self.email_entry = tk.Entry(self.root, width=30, font=("Helvetica", 10))
        self.email_entry.grid(row=1, column=1, padx=(10, 20), pady=5)

        # App Password label and entry
        tk.Label(
            self.root,
            text="App Password:",
            font=("Helvetica", 10),
            bg="#f2f2f2",
        ).grid(row=2, column=0, padx=(20, 10), sticky="e")
        self.app_password_entry = tk.Entry(self.root, show="*", width=30, font=("Helvetica", 10))
        self.app_password_entry.grid(row=2, column=1, padx=(10, 20), pady=5)

        # Authenticate button
        auth_button = tk.Button(
            self.root,
            text="Authenticate",
            command=self.authenticate,
            font=("Helvetica", 10, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            padx=10,
            pady=5,
        )
        auth_button.grid(row=3, column=0, columnspan=2, pady=(20, 10))

    def authenticate(self):
        email = self.email_entry.get().strip()
        app_password = self.app_password_entry.get().strip()

        try:
            self.backend.authenticate_user(email, app_password)
            
            self.root.destroy()
            import auth_app_ui
            root = tk.Tk()
            app = auth_app_ui.NestClipperApp(root)
            root.mainloop()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to authenticate: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PreAuthNestClipperApp(root)
    root.mainloop()
