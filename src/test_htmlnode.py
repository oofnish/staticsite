from unittest import TestCase

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(TestCase):
    def test_props_to_html_basic(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode(props=props)

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_three_vals(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        props["id"] = "htmlnodeid"
        node = HTMLNode(props=props)

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" id="htmlnodeid"')

    def test_props_to_html_empty(self):
        props = {}
        node = HTMLNode(props=props)

        self.assertEqual(node.props_to_html(), '')


class TestParentNode(TestCase):
    def test_paragraph(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        ret = node.to_html()
        self.assertEqual(ret, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


class TestLeafNode(TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), 'Click me!')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

