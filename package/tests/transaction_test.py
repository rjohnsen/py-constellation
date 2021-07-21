import unittest

from cyberconstellation.nodes import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.annotation = "testnode"
        self.node = Transaction(self.annotation)

    def tearDown(self):
        self.node = None

    def test_prop_datetime(self):
        value = "16.07.2021"
        self.node.datetime = value
        self.assertEqual(value, self.node.datetime)

    def test_prop_datetime_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.datetime = 1234

    def test_prop_activity(self):
        value = "Login"
        self.node.activity = value
        self.assertEqual(value, self.node.activity)

    def test_prop_activity_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.activity = 1234

    def test_prop_directed(self):
        value = True
        self.node.directed = value
        self.assertEqual(value, self.node.directed)

    def test_prop_directed_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.directed = 1234

    def test_prop_line_style(self):
        value = "DOTTED"
        self.node.line_style = value
        self.assertEqual(value, self.node.line_style)

    def test_prop_line_style_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.line_style = 1234

    def test_prop_width_style(self):
        value = 1.0
        self.node.width = value
        self.assertEqual(value, self.node.width)

    def test_prop_line_style_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.width = 1234
