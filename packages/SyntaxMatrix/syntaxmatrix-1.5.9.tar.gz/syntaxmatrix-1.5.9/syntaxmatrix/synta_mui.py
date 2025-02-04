import os
import webbrowser
from flask import Flask, request, render_template_string, redirect, url_for, session
from collections import OrderedDict

class SyntaxMUI:
    def __init__(self, title="SyntaxMatrix", host="127.0.0.1", port=5000):
        self.app = Flask(__name__)
        self.app.secret_key = "syntaxmatrix_secret"
        self.title = title
        self.host = host
        self.port = port

        # Stores dynamically created pages
        self.pages = {"Home": "Welcome to SyntaxMatrix!"}

        # Stores all widgets (text inputs, buttons, etc.)
        self.widgets = OrderedDict()

        # Default widget position (top or bottom)
        self.widget_position = "bottom"

        # Initialize all routes
        self.setup_routes()

    def setup_routes(self):
        """Define all routes for home, pages, admin panel, and UI widgets."""

        @self.app.route("/", methods=["GET", "POST"])
        def home():
            """Render home page with navigation and UI widgets."""
            if request.method == "POST":
                # Process form submission for text inputs and buttons
                for key, widget in self.widgets.items():
                    if widget["type"] == "text_input":
                        session[key] = request.form.get(key, widget["default"])
                    elif widget["type"] == "button":
                        if key in request.form and widget.get("callback"):
                            widget["callback"]()
                return redirect(url_for("home"))

            # Generate the navigation menu
            nav_html = self._generate_nav()
            widget_html = self._render_widgets()
            chat_html = self._render_chat_history()

            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head><title>{self.title}</title></head>
                <body>
                    <nav>{nav_html}</nav>
                    <h1>Welcome to SyntaxMatrix!</h1>
                    <p>This is the home page.</p>
                    <div id="chat-history">{chat_html}</div>
                    <div id="widget-container">{widget_html}</div>
                </body>
                </html>
            """)

    def _generate_nav(self):
        """Generate a navigation menu dynamically."""
        nav_items = [f'<a href="/">Home</a>']
        for page in self.pages:
            nav_items.append(f'<a href="/page/{page}">{page}</a>')
        nav_items.append(f'<a href="/admin">Admin</a>')
        return " | ".join(nav_items)

    def _render_widgets(self):
        """Generate HTML for all UI widgets (text inputs and buttons)."""
        widget_html = ""
        for key, widget in self.widgets.items():
            if widget["type"] == "text_input":
                value = session.get(key, widget["default"])
                widget_html += f"""
                <div>
                    <label for="{key}">{widget["label"]}</label><br>
                    <input type="text" id="{key}" name="{key}" value="{value}" style="width:300px;">
                </div>
                """
            elif widget["type"] == "button":
                widget_html += f"""
                <div>
                    <form method="POST">
                        <button type="submit" name="{key}" value="clicked">{widget["label"]}</button>
                    </form>
                </div>
                """
        return widget_html

    def _render_chat_history(self):
        """Generate HTML for chat history."""
        chat_html = "<h2>Chat History</h2>"
        chat_messages = session.get("chat_history", [])
        for sender, message in chat_messages:
            chat_html += f"<p><strong>{sender}:</strong> {message}</p>"
        return chat_html

    def text_input(self, key, label, default=""):
        """Register a text input widget."""
        if key not in self.widgets:
            self.widgets[key] = {"type": "text_input", "key": key, "label": label, "default": default}

    def button(self, key, label, callback=None):
        """Register a button widget."""
        if key not in self.widgets:
            self.widgets[key] = {"type": "button", "key": key, "label": label, "callback": callback}

    def get_text_input_value(self, key, default=""):
        """Retrieve the value of a text input field."""
        return session.get(key, default)

    def get_chat_history(self):
        """Retrieve chat history."""
        return session.get("chat_history", [])

    def set_chat_history(self, chat_history):
        """Update chat history."""
        session["chat_history"] = chat_history
        session.modified = True

    def clear_chat_history(self):
        """Clear chat history."""
        session["chat_history"] = []
        session.modified = True

    def set_widget_position(self, position):
        """Set widget position: 'top' or 'bottom'."""
        if position not in ["top", "bottom"]:
            raise ValueError("Invalid position. Choose 'top' or 'bottom'.")
        self.widget_position = position

    def run(self):
        """Open the web browser and start the Flask server."""
        url = f"http://{self.host}:{self.port}/"
        webbrowser.open(url)
        self.app.run(host=self.host, port=self.port, debug=False)
