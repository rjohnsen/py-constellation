import unittest

from parentnode_test import TestNodeParent
from node_test import TestNode
from transaction_test import TestTransaction

loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestNodeParent()))
suite.addTests(loader.loadTestsFromModule(TestNode()))
suite.addTests(loader.loadTestsFromModule(TestTransaction()))


# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)