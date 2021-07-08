from kernel.constants.graphconstants import GraphConstants

class NodeParent:
    def __init__(self, annotation: str, node_properties: list):
        self.annotation = annotation
        self.structure = {}

        properties = [
            GraphConstants.IDENTIFIER,
            GraphConstants.TYPE,
            GraphConstants.SOURCE,
            GraphConstants.LABEL,
            GraphConstants.COLOR,
            GraphConstants.DIM,
            GraphConstants.LAYER_MASK,
            GraphConstants.VISIBILITY,
            GraphConstants.SELECTED,
            GraphConstants.LAYER_VISIBILITY
        ] + node_properties

        for prop in properties:
            self.add_property(prop, None)

    def add_property(self, name: str, value: str) -> bool:
        if name in self.structure.keys():
            return False

        self.structure[name] = value
        return True

    def compress(self) -> dict:
        compressed = {key: value for key, value in self.structure.items() if value is not None}
        return {f"{self.annotation}." + str(key): val for key, val in compressed.items()}

    @property
    def identifier(self):
        return self.structure[GraphConstants.IDENTIFIER]

    @identifier.setter
    def identifier(self, value: str):
        self.structure[GraphConstants.IDENTIFIER] = value
        return self

    @property
    def type(self):
        return self.structure[GraphConstants.TYPE]

    @type.setter
    def type(self, value: str):
        self.structure[GraphConstants.TYPE] = value
        return self

    @property
    def source(self):
        return self.structure[GraphConstants.SOURCE]

    @source.setter
    def source(self, value: str):
        self.structure[GraphConstants.SOURCE] = value
        return self

    @property
    def label(self):
        return self.structure[graphconstants.LABEL]

    @label.setter
    def label(self, value: str):
        self.structure[GraphConstants.LABEL] = value
        return self

    @property
    def color(self):
        return self.structure[GraphConstants.COLOR]

    @color.setter
    def color(self, value: str):
        self.structure[GraphConstants.COLOR] = value
        return self

    @property
    def dim(self):
        return self.structure[GraphConstants.DIM]

    @dim.setter
    def dim(self, value: bool):
        self.structure[GraphConstants.DIM] = value
        return self

    @property
    def layer_mask(self):
        return self.structure[GraphConstants.LAYER_MASK]

    @layer_mask.setter
    def layer_mask(self, value):
        self.structure[GraphConstants.LAYER_MASK] = value
        return self


    @property
    def visibility(self):
        return self.structure[GraphConstants.VISIBILITY]

    @visibility.setter
    def visibility(self, value: float):
        self.structure[GraphConstants.VISIBILITY] = value
        return self

    @property
    def selected(self):
        return self.structure[graphconstants.SELECTED]

    @selected.setter
    def selected(self, value: bool):
        self.structure[GraphConstants.SELECTED] = value
        return self
    
    @property
    def layer_visibility(self):
        return self.structure[graphconstants.LAYER_VISIBILITY]

    @layer_visibility.setter
    def layer_visibility(self, value: float):
        self.structure[GraphConstants.LAYER_VISIBILITY] = value
        return self