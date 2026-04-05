#!/usr/bin/env python3
"""
CBEF Expert System — Local Proxy Server
========================================
Serves the CBEF Expert System HTML and proxies API requests
to the Anthropic API (required because browsers block direct
cross-origin requests).

Usage:
    python server.py

Then open http://localhost:8080 in your browser.

Requirements: Python 3.7+ (standard library only, no pip installs)
"""

import http.server
import json
import os
import sys
import urllib.request
import urllib.error

PORT = 8080
HTML_FILE = "index.html"
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"


class CBEFHandler(http.server.BaseHTTPRequestHandler):
    """Handles two routes: serves HTML at / and proxies API at /api/messages."""

    def do_GET(self):
        """Serve the HTML file."""
        if self.path == "/" or self.path == "/index.html":
            html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), HTML_FILE)
            try:
                with open(html_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, f"{HTML_FILE} not found. Place it in the same directory as server.py.")
        else:
            self.send_error(404)

    def do_POST(self):
        """Proxy API requests to Anthropic."""
        if self.path != "/api/messages":
            self.send_error(404)
            return

        # Read the request body
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        # Get the API key from the request header
        api_key = self.headers.get("x-api-key", "")
        if not api_key:
            self.send_error(400, "Missing x-api-key header")
            return

        # Forward to Anthropic API
        req = urllib.request.Request(
            ANTHROPIC_API_URL,
            data=body,
            headers={
                "Content-Type": "application/json",
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                resp_body = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(resp_body)))
                self.end_headers()
                self.wfile.write(resp_body)
        except urllib.error.HTTPError as e:
            error_body = e.read()
            self.send_response(e.code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(error_body)))
            self.end_headers()
            self.wfile.write(error_body)
        except urllib.error.URLError as e:
            error_msg = json.dumps({"error": {"message": f"Could not reach Anthropic API: {e.reason}"}}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(error_msg)))
            self.end_headers()
            self.wfile.write(error_msg)

    def log_message(self, format, *args):
        """Quieter logging — only show requests, not every detail."""
        sys.stderr.write(f"  {args[0]}\n")


def main():
    # Check the HTML file exists
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), HTML_FILE)
    if not os.path.exists(html_path):
        print(f"\n  Error: {HTML_FILE} not found.")
        print(f"  Place it in the same directory as server.py.\n")
        sys.exit(1)

    server = http.server.HTTPServer(("", PORT), CBEFHandler)
    print()
    print("  ┌─────────────────────────────────────────────┐")
    print("  │   CBEF Expert System — Local Server          │")
    print("  │                                              │")
    print(f"  │   Open:  http://localhost:{PORT}              │")
    print("  │   Stop:  Ctrl+C                              │")
    print("  │                                              │")
    print("  │   Copas (2026h) · MIT Licence                │")
    print("  └─────────────────────────────────────────────┘")
    print()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.\n")
        server.server_close()


if __name__ == "__main__":
    main()
