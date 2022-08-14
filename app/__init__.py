from pkgutil import ImpImporter
from flask import Flask

app = Flask(__name__)

from app import routes