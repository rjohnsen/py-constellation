from kernel.constants.graphconstants import GraphConstants
from kernel.models.nodeparent import NodeParent

# pylint: disable=R0904,C0103,R0903
class Node(NodeParent):
    def __init__(self, annotation: str):
        super().__init__(
            annotation,
            [
                GraphConstants.BACKGROUND_ICON,
                GraphConstants.RAW,
                GraphConstants.ICON,
                GraphConstants.NRADIUS,
                GraphConstants.PINNED,
                GraphConstants.X,
                GraphConstants.X2,
                GraphConstants.Y,
                GraphConstants.Y2,
                GraphConstants.Z,
                GraphConstants.Z2
            ]
        )

    @property
    def raw(self):
        return self.structure[GraphConstants.RAW]

    @raw.setter
    def raw(self, value: str):
        self.structure[GraphConstants.RAW] = value
        return self

    @property
    def background_icon(self):
        return self.structure[GraphConstants.TYPE]

    @background_icon.setter
    def background_icon(self, value: str):
        self.structure[GraphConstants.BACKGROUND_ICON] = value
        return self

    @property
    def icon(self):
        return self.structure[GraphConstants.ICON]

    @icon.setter
    def icon(self, value: str):
        self.structure[GraphConstants.ICON] = value
        return self

    @property
    def nradius(self):
        return self.structure[GraphConstants.NRADIUS]

    @nradius.setter
    def nradius(self, value: float):
        self.structure[GraphConstants.NRADIUS] = value
        return self

    @property
    def pinned(self):
        return self.structure[GraphConstants.PINNED]

    @pinned.setter
    def pinned(self, value: bool):
        self.structure[GraphConstants.PINNED] = value
        return self

    @property
    def x(self):
        return self.structure[GraphConstants.X]

    @x.setter
    def x(self, value: float):
        self.structure[GraphConstants.X] = value
        return self

    @property
    def x2(self):
        return self.structure[GraphConstants.X2]

    @x2.setter
    def x2(self, value: float):
        self.structure[GraphConstants.X2] = value
        return self

    @property
    def y(self):
        return self.structure[GraphConstants.Y]

    @y.setter
    def y(self, value: float):
        self.structure[GraphConstants.Y] = value
        return self

    @property
    def y2(self):
        return self.structure[GraphConstants.Y2]

    @y2.setter
    def y2(self, value: float):
        self.structure[GraphConstants.Y2] = value
        return self

    @property
    def z(self):
        return self.structure[GraphConstants.Z]

    @z.setter
    def z(self, value: float):
        self.structure[GraphConstants.Z] = value
        return self

    @property
    def z2(self):
        return self.structure[GraphConstants.Z2]

    @z2.setter
    def z2(self, value: float):
        self.structure[GraphConstants.Z2] = value
        return self
