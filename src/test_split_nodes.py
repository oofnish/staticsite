from unittest import TestCase

from split_nodes import split_nodes_link
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image


class TestSplitNodes(TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text_type.value, TextType.TEXT.value)
        self.assertEqual(new_nodes[1].text_type.value, TextType.CODE.value)
        self.assertEqual(new_nodes[2].text_type.value, TextType.TEXT.value)

        self.assertEqual(new_nodes[0].text, 'This is text with a ')
        self.assertEqual(new_nodes[1].text, 'code block')
        self.assertEqual(new_nodes[2].text, ' word')
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text_type.value, TextType.TEXT.value)
        self.assertEqual(new_nodes[1].text_type.value, TextType.BOLD.value)
        self.assertEqual(new_nodes[2].text_type.value, TextType.TEXT.value)

        self.assertEqual(new_nodes[0].text, 'This is text with a ')
        self.assertEqual(new_nodes[1].text, 'bold block')
        self.assertEqual(new_nodes[2].text, ' word')

    def test_split_nodes_delimiter_bold_extra(self):
        node = TextNode("This is text with a **bold block** `code` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text_type.value, TextType.TEXT.value)
        self.assertEqual(new_nodes[1].text_type.value, TextType.BOLD.value)
        self.assertEqual(new_nodes[2].text_type.value, TextType.TEXT.value)

        self.assertEqual(new_nodes[0].text, 'This is text with a ')
        self.assertEqual(new_nodes[1].text, 'bold block')
        self.assertEqual(new_nodes[2].text, ' `code` word')

    def test_split_nodes_delimiter_code_unterminated(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

class TestSplitNodesImages(TestCase):
    def test_split_nodes_images_basic(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_nodes_images_basic_extra(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another [second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )


class TestSplitNodesLinks(TestCase):
    def test_split_nodes_links_basic(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_nodes_links_basic_extra(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another ![second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ![second link](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )