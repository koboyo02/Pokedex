#!/bin/bash

# Installation de flask
pip install flask
pip install flask-cli

# Vérification de la version
python3 -c "import flask; print(flask.__version__)"