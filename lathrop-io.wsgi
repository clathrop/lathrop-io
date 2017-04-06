#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/lathrop-io/")

from FlaskApp import app as application
application.secret_key = 'mYS3cretKey'
