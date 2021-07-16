import unittest

from cyberconstellation.nodes import Node

class TestNode(unittest.TestCase):
    def setUp(self):
        self.annotation = "testnode"
        self.node = Node(self.annotation)

    def tearDown(self):
        self.node = None

    def test_prop_raw(self):
        value = "TEST"
        self.node.raw = value
        self.assertEqual(value, self.node.raw)

    def test_prop_raw_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.raw = 1234

    def test_prop_background_icon(self):
        value = "TEST"
        self.node.background_icon = value
        self.assertEqual(value, self.node.background_icon)

    def test_prop_background_icon_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.background_icon = 1234

    def test_prop_icon(self):
        value = "TEST"
        self.node.icon = value
        self.assertEqual(value, self.node.icon)

    def test_prop_icon_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.icon = 1234

    def test_prop_nradius(self):
        value = 1.0
        self.node.nradius = value
        self.assertEqual(value, self.node.nradius)

    def test_prop_nradius_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.nradius = 1234

    def test_prop_pinned(self):
        value = True
        self.node.pinned = value
        self.assertEqual(value, self.node.pinned)

    def test_prop_pinned_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.pinned = 1234

    def test_prop_x(self):
        value = 1.0
        self.node.x = value
        self.assertEqual(value, self.node.x)

    def test_prop_x_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.x = 1234

    def test_prop_x2(self):
        value = 1.0
        self.node.x2 = value
        self.assertEqual(value, self.node.x2)

    def test_prop_x2_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.x2 = 1234

    def test_prop_y(self):
        value = 1.0
        self.node.y= value
        self.assertEqual(value, self.node.y)

    def test_prop_y_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.y = 1234

    def test_prop_y2(self):
        value = 1.0
        self.node.y2 = value
        self.assertEqual(value, self.node.y2)

    def test_prop_y2_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.y2 = 1234

    def test_prop_z(self):
        value = 1.0
        self.node.z = value
        self.assertEqual(value, self.node.z)

    def test_prop_z_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.z = 1234

    def test_prop_z2(self):
        value = 1.0
        self.node.z2 = value
        self.assertEqual(value, self.node.z2)

    def test_prop_z2_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.z2 = 1234

if __name__ == '__main__':
    unittest.main()