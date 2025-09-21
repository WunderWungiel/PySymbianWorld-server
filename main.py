from flask import Flask, request, abort
from lib import config
import os

app = Flask(__name__)

if config["proxy"]:
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

folder = "/var/www/wunderwungiel.pl/html/Symbian/SymbianWorldMegaRepo"

@app.route("/get_categories/")
def _get_categories():

    folders = [path for path in os.listdir(folder) if os.path.isdir(os.path.join(folder, path)) and len(os.listdir(os.path.join(folder, path))) > 0]
    return folders

@app.route("/get_files/")
def _get_files():
    
    category = request.args.get("category")
    if not category: abort(422)
    if category not in _get_categories(): abort(422)

    files = [path for path in os.listdir(os.path.join(folder, category)) if os.path.isfile(os.path.join(folder, category, path))]
    return files