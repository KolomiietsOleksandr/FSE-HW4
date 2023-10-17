import unittest

test_loader = unittest.TestLoader()
test_suite = test_loader.discover(start_dir='Unit_tests/', pattern='test_*.py')

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite)
