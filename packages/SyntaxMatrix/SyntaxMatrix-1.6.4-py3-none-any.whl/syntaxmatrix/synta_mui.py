# syntaxmatrix/synta_mui.py
import os
import webbrowser
from flask import Flask, request, render_template_string, redirect, url_for, session, has_request_context
from collections import OrderedDict
from syntaxmatrix import db  # For SQLite persistence (if using admin persistence)

class SyntaxMUI:
    def __init__(self, title="SyntaxMatrix", host="127.0.0.1", port=5000):
        self.app = Flask(__name__)
        self.app.secret_key = "syntaxmatrix_secret"  # For session management
        self.title = title
        self.host = host
        self.port = port

        # Dynamic pages loaded from SQLite (for admin functionality)
        # (If using SQLite, these are loaded from db.get_pages())
        self.pages = db.get_pages() if os.path.exists(os.path.join(os.path.dirname(__file__), "syntaxmatrix.db")) else {"Home": "Welcome to SyntaxMatrix!"}
        if "Home" not in self.pages:
            self.pages["Home"] = "Welcome to SyntaxMatrix!"

        # Widget definitions (for text inputs, buttons, etc.)
        self.widgets = OrderedDict()
        # Default widget position: "top" or "bottom"
        self.widget_position = "bottom"

        # Setup routes (home, admin, dynamic pages, etc.)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                # Process text inputs and button callbacks.
                for key, widget in self.widgets.items():
                    if widget["type"] == "text_input":
                        session[key] = request.form.get(key, widget["default"])
                    elif widget["type"] == "button":
                        if key in request.form and widget.get("callback"):
                            widget["callback"]()
                return redirect(url_for("home"))

            # Refresh pages from the database for navigation
            self.pages = db.get_pages()

            nav_html = self._generate_nav()
            chat_html = self._render_chat_history()
            widget_html = self._render_widgets()

            # Auto-scroll script: when the window loads, scroll the chat container to bottom.
            scroll_js = """
            <script>
              window.onload = function() {
                var chatContainer = document.getElementById("chat-history");
                if (chatContainer) {
                  chatContainer.scrollTop = chatContainer.scrollHeight;
                }
              };
            </script>
            """

            # Assemble page HTML with improved, responsive styling.
            page_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
              <meta charset="UTF-8">
              <title>{self.title}</title>
              <style>
                /* Global Styles */
                body {{
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background: #f4f7f9;
                    color: #333;
                }}
                nav {{
                    background: #007acc;
                    padding: 10px 20px;
                    text-align: center;
                }}
                nav a {{
                    color: #fff;
                    text-decoration: none;
                    margin: 0 15px;
                    font-size: 1.1em;
                }}
                /* Chat History */
                #chat-history {{
                    width: 90%;
                    max-width: 800px;
                    margin: 20px auto 140px auto;  /* leave extra bottom space for pinned widget */
                    padding: 20px;
                    background: #eef2f7;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    overflow-y: auto;
                    max-height: 500px;
                }}
                .chat-message {{
                    margin-bottom: 15px;
                    padding: 10px 15px;
                    border-radius: 8px;
                    line-height: 1.5;
                    opacity: 0;
                    animation: fadeIn 0.5s forwards;
                }}
                .chat-message.user {{
                    background: #e1f5fe;
                    text-align: right;
                }}
                .chat-message.bot {{
                    background: #ffffff;
                    border: 1px solid #e0e0e0;
                    text-align: left;
                }}
                @keyframes fadeIn {{
                  from {{ opacity: 0; }}
                  to {{ opacity: 1; }}
                }}
                /* Pinned Widget Container */
                #widget-container {{
                    width: 90%;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 15px;
                    background: #ddd;  /* Dimmer background */
                    border-top: 2px solid #007acc;
                    position: fixed;
                    bottom: 0;
                    left: 50%;
                    transform: translateX(-50%);
                    box-shadow: 0 -2px 4px rgba(0,0,0,0.1);
                }}
                #widget-container form {{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-wrap: wrap;
                }}
                #widget-container input[type="text"] {{
                    flex: 1;
                    min-width: 200px;
                    padding: 12px;
                    font-size: 1em;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    margin-right: 10px;
                }}
                #widget-container button {{
                    padding: 10px 15px;
                    font-size: 0.9em;
                    border: none;
                    border-radius: 20px;
                    background: #007acc;
                    color: #fff;
                    cursor: pointer;
                    margin: 5px;
                }}
                #widget-container button:hover {{
                    background: #005fa3;
                }}
              </style>
            </head>
            <body>
              <nav>{nav_html}</nav>
              <div id="chat-history">{chat_html}</div>
              <div id="widget-container">{widget_html}</div>
              {scroll_js}
            </body>
            </html>
            """
            return render_template_string(page_html)

        @self.app.route("/page/<page_name>")
        def view_page(page_name):
            if page_name in self.pages:
                content = self.pages[page_name]
                return f"<h1 style='text-align:center;'>{page_name}</h1><div style='max-width:800px;margin:20px auto;padding:20px;background:#fff;border-radius:8px;'>{content}</div>"
            return "<h1>Page Not Found</h1>", 404

        @self.app.route("/admin", methods=["GET", "POST"])
        def admin_panel():
            if request.method == "POST":
                action = request.form.get("action")
                if action == "add_page":
                    page_name = request.form.get("page_name", "").strip()
                    page_content = request.form.get("page_content", "").strip()
                    if page_name and page_name not in self.pages:
                        from syntaxmatrix import db
                        db.add_page(page_name, page_content)
                elif action == "update_page":
                    old_name = request.form.get("old_name", "").strip()
                    new_name = request.form.get("new_name", "").strip()
                    new_content = request.form.get("new_content", "").strip()
                    if old_name in self.pages and new_name:
                        from syntaxmatrix import db
                        db.update_page(old_name, new_name, new_content)
                elif action == "delete_page":
                    del_page = request.form.get("delete_page", "").strip()
                    if del_page in self.pages:
                        from syntaxmatrix import db
                        db.delete_page(del_page)
                return redirect(url_for("admin_panel"))

            self.pages = db.get_pages()
            return render_template_string(f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Admin Panel - {self.title}</title>
                    <style>
                      body {{
                          font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                          background: #f4f7f9;
                          padding: 20px;
                      }}
                      form {{
                          margin-bottom: 20px;
                          background: #fff;
                          padding: 15px;
                          border-radius: 8px;
                          box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                      }}
                      input, textarea, select {{
                          padding: 10px;
                          font-size: 1em;
                          margin: 5px 0;
                          width: 100%;
                          border: 1px solid #ccc;
                          border-radius: 4px;
                      }}
                      button {{
                          padding: 10px 20px;
                          font-size: 1em;
                          background: #007acc;
                          color: #fff;
                          border: none;
                          border-radius: 4px;
                          cursor: pointer;
                      }}
                      button:hover {{
                          background: #005fa3;
                      }}
                    </style>
                </head>
                <body>
                    <h1>Admin Panel</h1>
                    <form method="post">
                        <h3>Add a Page</h3>
                        <input type="text" name="page_name" placeholder="Page Name" required>
                        <textarea name="page_content" placeholder="Page Content"></textarea>
                        <button type="submit" name="action" value="add_page">Add Page</button>
                    </form>
                    <form method="post">
                        <h3>Update an Existing Page</h3>
                        <select name="old_name">
                            {''.join(f'<option value="{p}">{p}</option>' for p in self.pages)}
                        </select>
                        <input type="text" name="new_name" placeholder="New Page Name" required>
                        <textarea name="new_content" placeholder="New Page Content"></textarea>
                        <button type="submit" name="action" value="update_page">Update Page</button>
                    </form>
                    <form method="post">
                        <h3>Delete a Page</h3>
                        <select name="delete_page">
                            {''.join(f'<option value="{p}">{p}</option>' for p in self.pages)}
                        </select>
                        <button type="submit" name="action" value="delete_page">Delete Page</button>
                    </form>
                    <p><a href="/">Return to Home</a></p>
                </body>
                </html>
            """)

    def _generate_nav(self):
        nav_items = [f'<a href="/">Home</a>']
        for page in self.pages:
            nav_items.append(f'<a href="/page/{page}">{page}</a>')
        nav_items.append(f'<a href="/admin">Admin</a>')
        return " | ".join(nav_items)

    def _render_chat_history(self):
        chat_html = ""
        messages = session.get("chat_history", [])
        if messages:
            chat_html += "<h2 style='text-align:center;'>Chat History</h2>"
            for role, message in messages:
                chat_html += f"<div class='chat-message {role.lower()}'><strong>{role.capitalize()}:</strong> {message}</div>"
        return chat_html

    def _render_widgets(self):
        widget_html = ""
        for key, widget in self.widgets.items():
            if widget["type"] == "text_input":
                value = session.get(key, widget["default"])
                widget_html += f"""
                <div style="flex: 1; margin-right:10px;">
                    <label for="{key}" style="display:block; margin-bottom:5px;">{widget["label"]}</label>
                    <input type="text" id="{key}" name="{key}" value="{value}" style="width:100%; padding:12px; font-size:1em; border:1px solid #ccc; border-radius:4px;">
                </div>
                """
            elif widget["type"] == "button":
                widget_html += f"""
                <div style="margin-right:10px;">
                    <form method="POST">
                        <button type="submit" name="{key}" value="clicked" style="padding:10px 15px; font-size:0.9em; border:none; border-radius:20px; background:#007acc; color:#fff; cursor:pointer;">
                            {widget["label"]}
                        </button>
                    </form>
                </div>
                """
        return f"""<form method="POST" style="display:flex; align-items:center; flex-wrap:wrap;">{widget_html}</form>"""

    # Public API for widget registration
    def text_input(self, key, label, default=""):
        if key not in self.widgets:
            self.widgets[key] = {"type": "text_input", "key": key, "label": label, "default": default}

    def button(self, key, label, callback=None):
        if key not in self.widgets:
            self.widgets[key] = {"type": "button", "key": key, "label": label, "callback": callback}

    def get_text_input_value(self, key, default=""):
        return session.get(key, default)

    def clear_text_input_value(self, key):
        session[key] = ""
        session.modified = True

    # Chat history management
    def get_chat_history(self):
        return session.get("chat_history", [])

    def set_chat_history(self, history):
        session["chat_history"] = history
        session.modified = True

    def clear_chat_history(self):
        session["chat_history"] = []
        session.modified = True

    def set_widget_position(self, position):
        if position not in ["top", "bottom"]:
            raise ValueError("Invalid position. Choose 'top' or 'bottom'.")
        self.widget_position = position

    def write(self, content):
        if "content_buffer" not in session:
            session["content_buffer"] = ""
        session["content_buffer"] += str(content)
        session.modified = True

    def run(self):
        url = f"http://{self.host}:{self.port}/"
        webbrowser.open(url)
        self.app.run(host=self.host, port=self.port, debug=False)
