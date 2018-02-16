#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.patch.insert(0,"/var/www/LenaforCityCouncil/")

from lenafornewark import app as application
application.secret_key = 'dRum&5853'
