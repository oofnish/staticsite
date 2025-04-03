from unittest import TestCase
from extract_md import extract_markdown_images
from extract_md import extract_markdown_links
from staticsite.src.extract_md import extract_title


class TestExtractImages(TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    def test_extract_markdown_images_extra(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_extract_markdown_images_basic(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


class TestExtractLinks(TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
    def test_extract_markdown_images_extra(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [('to boot dev', 'https://www.boot.dev')])



class TestExtractTitle(TestCase):
    def test_extrac_title_basic(self):
        title = extract_title("# My test heading ")
        self.assertEqual(title, "My test heading")
    def test_extrac_title_multiline(self):
        title = extract_title("""
# My test heading 

some more text""")
        self.assertEqual(title, "My test heading")
    def test_extrac_title_notfound(self):
        with self.assertRaises(Exception):
            title = extract_title("## My test heading")


