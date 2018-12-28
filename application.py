from flask import Flask
import json
import numpy as np
import pandas as pd
from keras.applications.resnet50 import ResNet50
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"