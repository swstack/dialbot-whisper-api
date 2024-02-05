import unittest

from dialbot.app import app  # Replace with your Flask app instance
from tests import *       # Import your test modules

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    unittest.TextTestRunner(verbosity=2).run(suite)