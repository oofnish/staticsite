import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(block):
    #matches = re.findall(r"#+ (.*)", block)
    #if matches:
    if block.startswith("#"):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    block_line_prefixes = list(map(lambda s: s.split(' ',1)[0], block.split("\n")))
    if block_line_prefixes[0] == ">" and len(list(set(block_line_prefixes))) <= 1:
        return BlockType.QUOTE
    elif block_line_prefixes[0] == "-" and len(list(set(block_line_prefixes))) <= 1:
        return BlockType.ULIST
    elif block_line_prefixes[0] == "1.":
        num = 1
        for pf in block_line_prefixes:
            if not pf.endswith("."):
                return BlockType.PARAGRAPH
            if not pf[:-1].isdigit():
                return BlockType.PARAGRAPH
            n = int(pf[:-1])
            if n != num:
                return BlockType.PARAGRAPH
            num += 1
        return BlockType.OLIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    blocks = list(map(lambda s: s.strip(), markdown.split("\n\n")))
    return [b for b in blocks if b]

