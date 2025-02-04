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

            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head><title>{self.title}</title></head>
                <body>
                    <nav>{nav_html}</nav>
                    <h1>Welcome to SyntaxMatrix!</h1>
                    <p>This is the home page.</p>
                    <div id="widget-container">{widget_html}</div>
                </body>
                </html>
            """)

        @self.app.route("/page/<page_name>")
        def view_page(page_name):
            """Display dynamically created pages."""
            if page_name in self.pages:
                return f"<h1>{page_name}</h1><p>{self.pages[page_name]}</p>"
            return "<h1>Page Not Found</h1>", 404

        @self.app.route("/admin", methods=["GET", "POST"])
        def admin_panel():
            """Admin panel for adding/updating/deleting pages."""
            if request.method == "POST":
                action = request.form.get("action")
                if action == "add_page":
                    page_name = request.form.get("page_name", "").strip()
                    page_content = request.form.get("page_content", "").strip()
                    if page_name and page_name not in self.pages:
                        self.pages[page_name] = page_content
                elif action == "update_page":
                    old_name = request.form.get("old_name", "").strip()
                    new_name = request.form.get("new_name", "").strip()
                    new_content = request.form.get("new_content", "").strip()
                    if old_name in self.pages and new_name:
                        self.pages.pop(old_name)
                        self.pages[new_name] = new_content
                elif action == "delete_page":
                    del_page = request.form.get("delete_page", "").strip()
                    if del_page in self.pages:
                        del self.pages[del_page]
                return redirect(url_for("admin_panel"))

            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head><title>Admin Panel</title></head>
                <body>
                    <h1>Admin Panel</h1>
                    <form method="post">
                        <h3>Add a Page</h3>
                        <input type="text" name="page_name" placeholder="Page Name" required>
                        <textarea name="page_content" placeholder="Page Content"></textarea>
                        <button type="submit" name="action" value="add_page">Add Page</button>
                    </form>

                    <h3>Update an Existing Page</h3>
                    <form method="post">
                        <select name="old_name">
                            {''.join(f'<option value="{p}">{p}</option>' for p in self.pages)}
                        </select>
                        <input type="text" name="new_name" placeholder="New Page Name" required>
                        <textarea name="new_content" placeholder="New Page Content"></textarea>
                        <button type="submit" name="action" value="update_page">Update Page</button>
                    </form>

                    <h3>Delete a Page</h3>
                    <form method="post">
                        <select name="delete_page">
                            {''.join(f'<option value="{p}">{p}</option>' for p in self.pages)}
                        </select>
                        <button type="submit" name="action" value="delete_page">Delete</button>
                    </form>

                    <p><a href="/">Return to Home</a></p>
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

    def text_input(self, key, label, default=""):
        """Register a text input widget."""
        if key not in self.widgets:
            self.widgets[key] = {"type": "text_input", "key": key, "label": label, "default": default}

    def button(self, key, label, callback=None):
        """Register a button widget."""
        if key not in self.widgets:
            self.widgets[key] = {"type": "button", "key": key, "label": label, "callback": callback}

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
