import unittest

from cyberconstellation.nodes import NodeParent

class TestNodeParent(unittest.TestCase):
    def setUp(self):
        self.annotation = "testparentnode"
        self.node = NodeParent(self.annotation)

    def tearDown(self):
        self.node = None

    def test_add_property_true(self):
        property_name = "property_name"
        property_value = "property_value"

        self.assertTrue(self.node.add_property(property_name, property_value))

    def test_add_property_same_value(self):
        property_name = "property_name"
        property_value = "property_value"
        self.node.add_property(property_name, property_value)

        self.assertEqual(
            self.node.get_property(property_name),
            property_value
        )

    def test_add_property_colliding(self):
        property_name = "property_name"
        property_value = "property_value"
        self.node.add_property(property_name, property_value)

        self.assertEqual(False, self.node.add_property(property_name, property_value))

    def test_compress(self):
        self.node.identifier = "Test node"
        self.node.label = "127.0.0.1"

        compressed = self.node.compress()

        self.assertEqual(
            [
                'testparentnode.annotation',
                'testparentnode.identifier',
                'testparentnode.label'
            ],
            list(compressed.keys())
        )

    def test_add_property_already_existing(self):
        self.assertEqual(False, self.node.add_property('identifier', 'identifier'))

    def test_prop_annotation(self):
        self.assertEqual(self.annotation, self.node.annotation)

    def test_prop_annotation_illegal_value(self):
        with self.assertRaises(ValueError):
            NodeParent(1234)

    def test_prop_identifier(self):
        value = "Identifier X"
        self.node.identifier = value
        self.assertEqual(value, self.node.identifier)

    def test_prop_identifier_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.identifier = 1234

    def test_prop_type(self):
        value = "XYX"
        self.node.type = value
        self.assertEqual(value, self.node.type)

    def test_prop_type_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.type = 1234

    def test_prop_label(self):
        value = "XYX"
        self.node.label = value
        self.assertEqual(value, self.node.label)

    def test_prop_label_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.label = 1234

    def test_prop_source(self):
        value = "XYX"
        self.node.source = value
        self.assertEqual(value, self.node.source)
    
    def test_prop_source_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.source = 1234

    def test_prop_color(self):
        value = "GREEN"
        self.node.color = value
        self.assertEqual(value, self.node.color)
    
    def test_prop_color_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.color = 1234

    def test_prop_dim(self):
        value = True
        self.node.dim = value
        self.assertEqual(value, self.node.dim)

    def test_prop_dim_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.dim = "TESTING"

    def test_prop_layer_mask(self):
        value = 1.0
        self.node.layer_mask = value
        self.assertEqual(value, self.node.layer_mask)

    def test_prop_layer_mask_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.layer_mask = "TESTING"

    def test_prop_visibility(self):
        value = 1.0
        self.node.visibility = value
        self.assertEqual(value, self.node.visibility)

    def test_prop_visibility_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.visibility = "TESTING"

    def test_prop_selected(self):
        value = True
        self.node.selected = value
        self.assertTrue(value, self.node.selected)

    def test_prop_selected_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.selected = "TESTING"

    def test_prop_layer_visibility(self):
        value = 1.0
        self.node.layer_visibility = value
        self.assertEqual(value, self.node.layer_visibility)

    def test_prop_layer_visibility_illegal_value(self):
        with self.assertRaises(ValueError):
            self.node.layer_visibility = "TESTING"
    
if __name__ == '__main__':
    unittest.main()