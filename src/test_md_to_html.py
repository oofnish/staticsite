from unittest import TestCase

from md_to_html import markdown_to_html_node


class TestMarkdownToHtmlNode(TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
> This is some **important**
> quote that is very
> _insightful_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is some <b>important</b> quote that is very <i>insightful</i></blockquote></div>",
        )

    def test_heading4(self):
        md = """
#### heading at level 4!
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>heading at level 4!</h4></div>",
        )

    def test_ulist(self):
        md = """
- This is some **important**
- list that is very
- _unordered_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is some <b>important</b></li><li>list that is very</li><li><i>unordered</i></li></ul></div>",
        )

    def test_olist(self):
        md = """
1. This is some **important**
2. list that is very
3. _ordered_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is some <b>important</b></li><li>list that is very</li><li><i>ordered</i></li></ol></div>",
        )