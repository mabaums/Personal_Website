#!/usr/bin/env python3

import connexion
import logging
import os
from logging.config import dictConfig

from swagger_server import encoder
from flask_cors import CORS
from flask import send_from_directory
import logging
from flask.logging import create_logger

dir_path = '../dist'


def static_proxy(path):
    if path.endswith("js") or path.endswith(".css"):
        return send_from_directory(dir_path, path)
    return send_from_directory(dir_path, 'index.html')


def root():
    return send_from_directory(dir_path, 'index.html')


def main():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Simple Inventory API'}, pythonic_params=True)
    app.app.add_url_rule('/', 'root', root)
    app.app.add_url_rule('/<path:path>', 'static_proxy', static_proxy)
    app.run(port=8080)


if __name__ == '__main__':
    main()
