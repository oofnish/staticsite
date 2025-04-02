from textnode import TextNode, TextType


def main():
    tn = TextNode("this is some anchor text", TextType.LINK, "http://example.com")
    print(tn)

if __name__ == '__main__':
    main()