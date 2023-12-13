import unittest
from HTMLTestRunner import HTMLTestRunner
from tests.login import TestLogin

# Test Suite
test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestLogin))

# Define HTMLRunner
runner = HTMLTestRunner(output='reports')

# Run the tests and generate HTML report
runner.run(test_suite)