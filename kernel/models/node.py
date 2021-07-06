from kernel.lib.graphconstants import GraphConstants

# pylint: disable=R0904,C0103,R0903
class Node:
    def __init__(self, annotation: str):
        self.annotation = annotation
        self.structure = {
            GraphConstants.IDENTIFIER: None,
            GraphConstants.TYPE: None,
            GraphConstants.LABEL: None,
            GraphConstants.RAW: None,
            GraphConstants.SOURCE: None,
            GraphConstants.BACKGROUND_ICON: None,
            GraphConstants.COLOR: None,
            GraphConstants.DIM: None,
            GraphConstants.ICON: None,
            GraphConstants.LAYER_MASK: None,
            GraphConstants.LAYER_VISIBILITY: None,
            GraphConstants.NRADIUS: None,
            GraphConstants.PINNED: None,
            GraphConstants.SELECTED: None,
            GraphConstants.VISIBILITY: None,
            GraphConstants.X: None,
            GraphConstants.X2: None,
            GraphConstants.Y: None,
            GraphConstants.Y2: None,
            GraphConstants.Z: None,
            GraphConstants.Z2: None
        }

    @property
    def identifier(self):
        return self.structure[GraphConstants.IDENTIFIER]

    @identifier.setter
    def identifier(self, value):
        self.structure[GraphConstants.IDENTIFIER] = value
        return self

    @property
    def type(self):
        return self.structure[GraphConstants.TYPE]

    @type.setter
    def type(self, value):
        self.structure[GraphConstants.TYPE] = value
        return self

    @property
    def label(self):
        return self.structure[GraphConstants.LABEL]

    @label.setter
    def label(self, value):
        self.structure[GraphConstants.LABEL] = value
        return self

    @property
    def raw(self):
        return self.structure[GraphConstants.RAW]

    @raw.setter
    def raw(self, value):
        self.structure[GraphConstants.RAW] = value
        return self

    @property
    def source(self):
        return self.structure[GraphConstants.SOURCE]

    @source.setter
    def source(self, value):
        self.structure[GraphConstants.SOURCE] = value
        return self

    @property
    def background_icon(self):
        return self.structure[GraphConstants.TYPE]

    @background_icon.setter
    def background_icon(self, value):
        self.structure[GraphConstants.BACKGROUND_ICON] = value
        return self

    @property
    def color(self):
        return self.structure[GraphConstants.COLOR]

    @color.setter
    def color(self, value):
        self.structure[GraphConstants.COLOR] = value
        return self

    @property
    def dim(self):
        return self.structure[GraphConstants.DIM]

    @dim.setter
    def dim(self, value):
        self.structure[GraphConstants.DIM] = value
        return self

    @property
    def icon(self):
        return self.structure[GraphConstants.ICON]

    @icon.setter
    def icon(self, value):
        self.structure[GraphConstants.ICON] = value
        return self

    @property
    def layer_mask(self):
        return self.structure[GraphConstants.LAYER_MASK]

    @layer_mask.setter
    def layer_mask(self, value):
        self.structure[GraphConstants.LAYER_MASK] = value
        return self

    @property
    def nradius(self):
        return self.structure[GraphConstants.NRADIUS]

    @nradius.setter
    def nradius(self, value):
        self.structure[GraphConstants.NRADIUS] = value
        return self

    @property
    def pinned(self):
        return self.structure[GraphConstants.PINNED]

    @pinned.setter
    def pinned(self, value):
        self.structure[GraphConstants.PINNED] = value
        return self

    @property
    def selected(self):
        return self.structure[GraphConstants.SELECTED]

    @selected.setter
    def selected(self, value):
        self.structure[GraphConstants.SELECTED] = value
        return self

    @property
    def visibility(self):
        return self.structure[GraphConstants.VISIBILITY]

    @visibility.setter
    def visibility(self, value):
        self.structure[GraphConstants.VISIBILITY] = value
        return self

    @property
    def x(self):
        return self.structure[GraphConstants.X]

    @x.setter
    def x(self, value):
        self.structure[GraphConstants.X] = value
        return self

    @property
    def x2(self):
        return self.structure[GraphConstants.X2]

    @x2.setter
    def x2(self, value):
        self.structure[GraphConstants.X2] = value
        return self

    @property
    def y(self):
        return self.structure[GraphConstants.Y]

    @y.setter
    def y(self, value):
        self.structure[GraphConstants.Y] = value
        return self

    @property
    def y2(self):
        return self.structure[GraphConstants.Y2]

    @y2.setter
    def y2(self, value):
        self.structure[GraphConstants.Y2] = value
        return self

    @property
    def z(self):
        return self.structure[GraphConstants.Z]

    @z.setter
    def z(self, value):
        self.structure[GraphConstants.Z] = value
        return self

    @property
    def z2(self):
        return self.structure[GraphConstants.Z2]

    @z2.setter
    def z2(self, value):
        self.structure[GraphConstants.Z2] = value
        return self

    def add_property(self, name: str, value: str) -> bool:
        if name in self.structure.keys():
            return False

        self.structure[name] = value
        return True

    def compress(self) -> dict:
        compressed = {key: value for key, value in self.structure.items() if value is not None}
        return {f"{self.annotation}." + str(key): val for key, val in compressed.items()}
