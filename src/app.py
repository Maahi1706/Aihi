"""Serve a web page that displays a name.

Usage:
    python app.py              # shows the default name
    python app.py "Your Name"  # shows the given name

Then open http://localhost:8000 in your browser.
"""

import html
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000
NAME = sys.argv[1] if len(sys.argv) > 1 else "Aihi"

PAGE = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(NAME)}</title>
  <style>
    body {{
      margin: 0;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
      background: #f4f4f8;
      color: #222;
    }}
    h1 {{ font-size: 4rem; }}
  </style>
</head>
<body>
  <h1>{html.escape(NAME)}</h1>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Showing '{NAME}' at http://localhost:{PORT} (press Ctrl+C to stop)")
    try:
        HTTPServer(("", PORT), Handler).serve_forever()
    except KeyboardInterrupt:
        pass
