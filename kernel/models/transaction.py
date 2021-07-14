from kernel.constants.graphconstants import GraphConstants
from kernel.constants.transaction import Transaction as TRCon
from kernel.models.nodeparent import NodeParent

class Transaction(NodeParent):
    def __init__(self, annotation: str):
        super().__init__(annotation)

        self.__datetime = None
        self.__activity = None
        self.__directed = None
        self.__line_style = None
        self.__width = None

    @property
    def datetime(self):
        return self.__datetime

    @datetime.setter
    def datetime(self, value):
        self.__datetime = value
        return self

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value: str):
        self.__activity = value
        return self

    @property
    def directed(self):
        return self.__directed

    @directed.setter
    def directed(self, value):
        self.__directed = value
        return self

    @property
    def line_style(self):
        return self.__line_style

    @line_style.setter
    def line_style(self, value: str):
        self.__line_style = value
        return self

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        return self