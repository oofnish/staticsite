class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ''
        return ' ' + ' '.join(list(map(lambda kv: f'{kv[0]}="{kv[1]}"', self.props.items())))

    def __repr__(self):
        return f'HTMLNode({self.tag, self.value, self.children, self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parent must have tag")

        if not self.children:
            raise ValueError("parent has no children")

        return f'<{self.tag}{self.props_to_html()}>{"".join(map(lambda c: c.to_html(), self.children))}</{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        # if not self.value:
        #     raise ValueError

        if not self.tag:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


