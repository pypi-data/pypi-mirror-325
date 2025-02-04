import os
import webbrowser
from flask import Flask, request, render_template_string, redirect, url_for, session

class SyntaxMUI:
    def __init__(self, title="SyntaxMatrix", host="127.0.0.1", port=5000):
        self.app = Flask(__name__)
        self.app.secret_key = "syntaxmatrix_secret"
        self.title = title
        self.host = host
        self.port = port

        # Dictionary to store dynamic pages: {"page_name": "Page Content"}
        self.pages = {"Home": "Welcome to SyntaxMatrix!"}

        # Initialize all routes
        self.setup_routes()

    def setup_routes(self):
        """Define all routes for the application, including home, pages, and admin panel."""

        @self.app.route("/", methods=["GET"])
        def home():
            """Render the home page with the nav menu."""
            nav_html = self._generate_nav()
            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head><title>{self.title}</title></head>
                <body>
                    <nav>{nav_html}</nav>
                    <h1>Welcome to SyntaxMatrix!</h1>
                    <p>This is the home page.</p>
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
            """Admin panel to add, update, and delete pages."""
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

            # Render Admin Panel
            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head><title>Admin Panel</title></head>
                <body>
                    <h1>Admin Panel</h1>
                    <h2>Manage Pages</h2>
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

    def run(self):
        """Open the web browser and start the server."""
        url = f"http://{self.host}:{self.port}/"
        webbrowser.open(url)
        self.app.run(host=self.host, port=self.port, debug=False)
