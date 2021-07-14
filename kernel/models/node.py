from kernel.models.nodeparent import NodeParent

# pylint: disable=R0904,C0103,R0903
class Node(NodeParent):    
    def __init__(self, annotation: str):
        super().__init__(annotation)

        self.__background_icon = None
        self.__raw = None
        self.__icon = None
        self.__nradius = None
        self.__pinned = None
        self.__x = None
        self.__x2 = None
        self.__y = None
        self.__y2 = None
        self.__z = None
        self.__z2 = None

    @property
    def raw(self):
        return self.__raw

    @raw.setter
    def raw(self, value: str):
        self.__raw = value
        return self

    @property
    def background_icon(self):
        return self.__background_icon

    @background_icon.setter
    def background_icon(self, value: str):
        self.__background_icon = value
        return self

    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, value: str):
        self.__icon = value
        return self

    @property
    def nradius(self):
        return self.__nradius

    @nradius.setter
    def nradius(self, value: float):
        self.__nradius = value
        return self

    @property
    def pinned(self):
        return self.__pinned

    @pinned.setter
    def pinned(self, value: bool):
        self.__pinned = value
        return self

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: float):
        self.__x = value
        return self

    @property
    def x2(self):
        return self.__x2

    @x2.setter
    def x2(self, value: float):
        self.__x2 = value
        return self

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: float):
        self.__y = value
        return self

    @property
    def y2(self):
        return self.__y2

    @y2.setter
    def y2(self, value: float):
        self.__y2 = value
        return self

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value: float):
        self.__z = value
        return self

    @property
    def z2(self):
        return self.__z2

    @z2.setter
    def z2(self, value: float):
        self.__z2 = value
        return self
