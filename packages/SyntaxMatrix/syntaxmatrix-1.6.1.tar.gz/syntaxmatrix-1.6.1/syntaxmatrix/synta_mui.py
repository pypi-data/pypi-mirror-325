import os
import webbrowser
from flask import Flask, request, render_template_string, redirect, url_for, session, has_request_context
from collections import OrderedDict

class SyntaxMUI:
    def __init__(self, title="SyntaxMatrix", host="127.0.0.1", port=5000):
        self.app = Flask(__name__)
        self.app.secret_key = "syntaxmatrix_secret"  # Used for session management
        self.title = title
        self.host = host
        self.port = port

        # Dynamic pages for admin functionality
        self.pages = {"Home": "Welcome to SyntaxMatrix!"}

        # Widgets for text inputs, buttons, etc.
        self.widgets = OrderedDict()

        # Default widget position: "top" or "bottom"
        self.widget_position = "bottom"

        # Initialize routes (home, admin, etc.)
        self.setup_routes()

    def setup_routes(self):
        """Define routes for home, pages, and admin panel."""
        @self.app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                # Process widget submissions: update text inputs and call button callbacks.
                for key, widget in self.widgets.items():
                    if widget["type"] == "text_input":
                        session[key] = request.form.get(key, widget["default"])
                    elif widget["type"] == "button":
                        if key in request.form and widget.get("callback"):
                            widget["callback"]()
                return redirect(url_for("home"))
            
            nav_html = self._generate_nav()
            chat_html = self._render_chat_history()
            widget_html = self._render_widgets()

            # JavaScript to auto-scroll the chat container to the bottom on page load.
            scroll_js = """
            <script>
              window.onload = function() {
                var chatContainer = document.getElementById("chat-history");
                if(chatContainer) {
                  chatContainer.scrollTop = chatContainer.scrollHeight;
                }
              };
            </script>
            """

            # The full page HTML with updated styling and auto-scroll script.
            page_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>{self.title}</title>
                <style>
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
                  #chat-history {{
                      width: 90%;
                      max-width: 800px;
                      height: 400px;
                      margin: 20px auto;
                      padding: 20px;
                      background: #fff;
                      border-radius: 8px;
                      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                      overflow-y: auto;
                  }}
                  .chat-message {{
                      margin-bottom: 15px;
                      padding: 10px 15px;
                      border-radius: 8px;
                      line-height: 1.5;
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
                  #widget-container {{
                      width: 90%;
                      max-width: 800px;
                      margin: 0 auto;
                      padding: 15px;
                      background: #fff;
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
                  }}
                  #widget-container input[type="text"] {{
                      flex: 1;
                      padding: 10px;
                      font-size: 1em;
                      border: 1px solid #ccc;
                      border-radius: 4px;
                      margin-right: 10px;
                  }}
                  #widget-container button {{
                      padding: 10px 20px;
                      font-size: 1em;
                      border: none;
                      border-radius: 4px;
                      background: #007acc;
                      color: #fff;
                      cursor: pointer;
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
                return f"<h1>{page_name}</h1><p>{self.pages[page_name]}</p>"
            return "<h1>Page Not Found</h1>", 404

        @self.app.route("/admin", methods=["GET", "POST"])
        def admin_panel():
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
                      }}
                      input, textarea, select {{
                          padding: 8px;
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
        """Generate a dynamic navigation menu."""
        nav_items = [f'<a href="/">Home</a>']
        for page in self.pages:
            nav_items.append(f'<a href="/page/{page}">{page}</a>')
        nav_items.append(f'<a href="/admin">Admin</a>')
        return " | ".join(nav_items)

    def _render_chat_history(self):
        """Generate HTML for the chat history stored in session."""
        chat_html = ""
        messages = session.get("chat_history", [])
        if messages:
            chat_html += "<h2>Chat History</h2>"
            for role, message in messages:
                chat_html += f"<p><strong>{role.capitalize()}:</strong> {message}</p>"
        return chat_html

    def _render_widgets(self):
        """Generate HTML for UI widgets (text inputs, buttons)."""
        widget_html = ""
        for key, widget in self.widgets.items():
            if widget["type"] == "text_input":
                value = session.get(key, widget["default"])
                widget_html += f"""
                <div style="margin-bottom:10px;">
                    <label for="{key}">{widget["label"]}</label><br>
                    <input type="text" id="{key}" name="{key}" value="{value}" style="width:300px; padding:8px; border:1px solid #ccc; border-radius:4px;">
                </div>
                """
            elif widget["type"] == "button":
                widget_html += f"""
                <div style="display:inline-block; margin-right:10px;">
                    <form method="POST">
                        <button type="submit" name="{key}" value="clicked" style="padding:10px 20px; font-size:1em; border:none; border-radius:4px; background:#007acc; color:#fff; cursor:pointer;">
                            {widget["label"]}
                        </button>
                    </form>
                </div>
                """
        return widget_html

    # Public API functions
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

    def get_chat_history(self):
        return session.get("chat_history", [])

    def set_chat_history(self, chat_history):
        session["chat_history"] = chat_history
        session.modified = True

    def clear_chat_history(self):
        session["chat_history"] = []
        session.modified = True

    def set_widget_position(self, position):
        if position not in ["top", "bottom"]:
            raise ValueError("Invalid position. Choose 'top' or 'bottom'.")
        self.widget_position = position

    def write(self, content):
        """Append arbitrary HTML to the session's content buffer (if used)."""
        if "content_buffer" not in session:
            session["content_buffer"] = ""
        session["content_buffer"] += str(content)
        session.modified = True

    def run(self):
        url = f"http://{self.host}:{self.port}/"
        webbrowser.open(url)
        self.app.run(host=self.host, port=self.port, debug=False)
