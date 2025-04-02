from blocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode, LeafNode
from text_to_nodes import text_to_nodes
from textnode import text_node_to_html_node


def paragraph_nodes(blocktext):
    children = []
    nodes = text_to_nodes(blocktext)
    for node in nodes:
        children.append(text_node_to_html_node(node))

    return ParentNode("p", children)


def code_nodes(blocktext):
    blocktext = blocktext.strip("```").lstrip()
    return ParentNode("pre",[LeafNode("code", blocktext)])


def quote_nodes(blocktext):
    children = []
    blocktext = blocktext.replace('> ', '')
    nodes = text_to_nodes(blocktext)
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return ParentNode('blockquote', children)


def heading_nodes(blocktext):
    parts = blocktext.split(" ", 1)
    hl = len(parts[0])
    return LeafNode(f'h{hl}', parts[1])


def ulist_nodes(blocktext):
    children = []
    lines = list(map(lambda s: s.lstrip('- '), blocktext.split('\n')))
    for l in lines:
        lchildren = []
        nodes = text_to_nodes(l)
        for node in nodes:
            lchildren.append(text_node_to_html_node(node))
        children.append(ParentNode('li', lchildren))
    return ParentNode('ul', children)


def olist_nodes(blocktext):
    children = []
    lines = list(map(lambda s: s.split('. ')[1], blocktext.split('\n')))
    for l in lines:
        lchildren = []
        nodes = text_to_nodes(l)
        for node in nodes:
            lchildren.append(text_node_to_html_node(node))
        children.append(ParentNode('li', lchildren))
    return ParentNode('ol', children)


def markdown_to_html_node(mdoc):
    blocks = markdown_to_blocks(mdoc)
    top_children = []
    for b in blocks:
        bt = block_to_block_type(b)
        match bt:
            case BlockType.PARAGRAPH:
                top_children.append(paragraph_nodes(b))
            case BlockType.CODE:
                top_children.append(code_nodes(b))
            case BlockType.QUOTE:
                top_children.append(quote_nodes(b))
            case BlockType.HEADING:
                top_children.append(heading_nodes(b))
            case BlockType.ULIST:
                top_children.append(ulist_nodes(b))
            case BlockType.OLIST:
                top_children.append(olist_nodes(b))

    return ParentNode("div", top_children)