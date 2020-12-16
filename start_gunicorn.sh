#!/bin/bash
source /home/www/code/ConversionToASCIIDjango/env/bin/activate
exec gunicorn  -c "/home/www/code/ConversionToASCIIDjango/gunicorn_config.py" CreateASCIIGraphics.wsgi
