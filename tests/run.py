import sys
import unittest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)

    if not result.wasSuccessful():
        sys.exit(1)
