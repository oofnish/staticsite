import re

def extract_title(text):
    matches = re.findall(r"^# (.*)", text, re.MULTILINE)
    if matches:
        return matches[0].strip()
    else:
        raise Exception("no top level header")

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)]\((.*?)\)", text)
    return matches