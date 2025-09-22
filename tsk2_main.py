class GraphicObject:
    def __init__(self, object: str):
        self.object = object

class Rectangle(GraphicObject):
    pass

class ClickHandler:
    pass

class Button(Rectangle, ClickHandler):
    pass