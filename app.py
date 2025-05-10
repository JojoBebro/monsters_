from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page."""
    if not os.path.exists('index.html'):
        abort(404, description="index.html not found")
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, images, etc.)."""
    allowed_extensions = ['.html', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.otf']
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in allowed_extensions:
        return send_from_directory('.', filename)
    else:
        abort(403, description="File type not allowed")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)