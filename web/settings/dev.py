
from settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
USER_LOGIN_URL = "login"

if 'unittest.util' in __import__('sys').modules:
	# Show full diff in self.assertEqual.
	__import__('sys').modules['unittest.util']._MAX_LENGTH = 999999999 #pylint: disable=protected-access
