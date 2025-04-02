from unittest import TestCase

from blocks import block_to_block_type, markdown_to_blocks, BlockType


class TestBlockToBlockType(TestCase):
    def test_block_to_block_type_heading(self):
        block= \
"""### text goes here 
"""
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block= \
            """``` code goes here 
            more code here
            still more 
            all done ```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block= \
"""> quote goes here 
> more quote here
> still more 
> all done ```"""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_ulist(self):
        block= \
"""- list goes here 
- more list here
- still more 
- all done"""
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)


    def test_block_to_block_type_olist(self):
        block= \
"""1. list goes here 
2. more list here
3.  still more 
4. all done"""
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)


class TestMarkdownToBlocks(TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )