"""
Environment for Behave Testing
"""
from os import getenv

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '60'))
BASE_URL = getenv('BASE_URL', 'http://localhost:8080')

def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS

def after_all(context):
    """ Executed after all tests """
    pass