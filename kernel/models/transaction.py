from kernel.lib.graphconstants import GraphConstants

class Transaction:
    def __init__(self, annotation: str):
        self.annotation = annotation
        self.structure = {
            GraphConstants.DATETIME: None,
            GraphConstants.IDENTIFIER: None,
            GraphConstants.SOURCE: None,
            GraphConstants.TYPE: None,
            GraphConstants.ACTIVITY: None,
            GraphConstants.LABEL: None,
            GraphConstants.COLOR: None,
            GraphConstants.DIM: None,
            GraphConstants.DIRECTED: None,
            GraphConstants.LAYER_MASK: None,
            GraphConstants.LAYER_VISIBILITY: None,
            GraphConstants.LINE_STYLE: None,
            GraphConstants.SELECTED: None,
            GraphConstants.VISIBILITY: None,
            GraphConstants.WIDTH: None,
            GraphConstants.__DIRECTED__: None
        }

    @property
    def datetime(self):
        return self.structure[graphconstants.DATETIME]

    @datetime.setter
    def datetime(self, value):
        self.structure[GraphConstants.DATETIME] = value
        return self
    
    @property
    def identifier(self):
        return self.structure[graphconstants.IDENTIFIER]

    @identifier.setter
    def identifier(self, value):
        self.structure[GraphConstants.IDENTIFIER] = value
        return self

    @property
    def source(self):
        return self.structure[graphconstants.SOURCE]

    @source.setter
    def source(self, value):
        self.structure[GraphConstants.SOURCE] = value
        return self

    @property
    def type(self):
        return self.structure[graphconstants.TYPE]

    @type.setter
    def type(self, value):
        self.structure[GraphConstants.TYPE] = value
        return self

    @property
    def activity(self):
        return self.structure[graphconstants.ACTIVITY]

    @activity.setter
    def activity(self, value):
        self.structure[GraphConstants.ACTIVITY] = value
        return self

    @property
    def label(self):
        return self.structure[graphconstants.LABEL]

    @label.setter
    def label(self, value):
        self.structure[GraphConstants.LABEL] = value
        return self
    
    @property
    def color(self):
        return self.structure[graphconstants.COLOR]

    @color.setter
    def color(self, value):
        self.structure[GraphConstants.COLOR] = value
        return self

    @property
    def dim(self):
        return self.structure[graphconstants.DIM]

    @dim.setter
    def dim(self, value):
        self.structure[GraphConstants.DIM] = value
        return self

    @property
    def directed(self):
        return self.structure[graphconstants.DIRECTED]

    @directed.setter
    def directed(self, value):
        self.structure[GraphConstants.DIRECTED] = value
        return self

    @property
    def layer_mask(self):
        return self.structure[graphconstants.LAYER_MASK]

    @layer_mask.setter
    def layer_mask(self, value):
        self.structure[GraphConstants.LAYER_MASK] = value
        return self

    @property
    def layer_visibility(self):
        return self.structure[graphconstants.LAYER_VISIBILITY]

    @layer_visibility.setter
    def layer_visibility(self, value):
        self.structure[GraphConstants.LAYER_VISIBILITY] = value
        return self

    @property
    def line_style(self):
        return self.structure[graphconstants.LINE_STYLE]

    @line_style.setter
    def line_style(self, value):
        self.structure[GraphConstants.LINE_STYLE] = value
        return self
    
    @property
    def selected(self):
        return self.structure[graphconstants.SELECTED]

    @selected.setter
    def selected(self, value):
        self.structure[GraphConstants.SELECTED] = value
        return self

    @property
    def visibility(self):
        return self.structure[graphconstants.VISIBILITY]

    @visibility.setter
    def visibility(self, value):
        self.structure[GraphConstants.VISIBILITY] = value
        return self

    @property
    def width(self):
        return self.structure[graphconstants.WIDTH]

    @width.setter
    def width(self, value):
        self.structure[GraphConstants.WIDTH] = value
        return self

    def add_property(self, name: str, value: str) -> bool:
        if name in self.structure.keys():
            return False

        self.structure[name] = value

        return True

    def compress(self) -> dict:
        compressed = {key: value for key, value in self.structure.items() if value is not None}
        return {f"{self.annotation}." + str(key): val for key, val in compressed.items()}