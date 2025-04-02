from unittest import TestCase

from textnode import TextNode, TextType
from text_to_nodes import text_to_nodes


class TestTextToNodes(TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_nodes(text)
        self.assertListEqual(nodes,
         [
             TextNode("This is ", TextType.TEXT),
             TextNode("text", TextType.BOLD),
             TextNode(" with an ", TextType.TEXT),
             TextNode("italic", TextType.ITALIC),
             TextNode(" word and a ", TextType.TEXT),
             TextNode("code block", TextType.CODE),
             TextNode(" and an ", TextType.TEXT),
             TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
             TextNode(" and a ", TextType.TEXT),
             TextNode("link", TextType.LINK, "https://boot.dev"),
         ]
         )

