from extract_md import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        ndelim = node.text.count(delimiter)
        if ndelim % 2 > 0:
            raise Exception("invalid markdown, unterminated delimiter " + delimiter)
        strs = node.text.split(delimiter)
        for i, s in enumerate(strs):
            if i % 2 == 0:
                # text nodes are even indexes
                new_nodes.append(TextNode(s.replace("\n"," "), TextType.TEXT))
            else:
                new_nodes.append(TextNode(s, text_type))

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        p = node.text
        while p:
            ml = extract_markdown_images(p)
            if not ml:
                new_nodes.append(TextNode(p, TextType.TEXT))
                p=''
                continue
            parts = p.split(f'![{ml[0][0]}]({ml[0][1]})', 1)
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(ml[0][0], TextType.IMAGE, ml[0][1]))
            p = parts[1] if len(parts) > 1 else ''
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        p = node.text
        while p:
            ml = extract_markdown_links(p)
            if not ml:
                new_nodes.append(TextNode(p, TextType.TEXT))
                p=''
                continue
            parts = p.split(f'[{ml[0][0]}]({ml[0][1]})', 1)
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(ml[0][0], TextType.LINK, ml[0][1]))
            p = parts[1] if len(parts) > 1 else ''
    return new_nodes

