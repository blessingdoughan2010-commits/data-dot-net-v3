from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__, static_folder='public')

# We use a string template so you don't need a separate templates folder on your phone
HTML_CODE = """
"""

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
