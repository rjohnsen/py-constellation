from kernel.constants.graphconstants import GraphConstants
from kernel.constants.transaction import Transaction as TRCon
from kernel.models.nodeparent import NodeParent

class Transaction(NodeParent):
    def __init__(self, annotation: str):
        super().__init__(
            annotation,
            [
                GraphConstants.DATETIME,
                GraphConstants.ACTIVITY,
                GraphConstants.DIRECTED,
                GraphConstants.LINE_STYLE,
                GraphConstants.WIDTH
            ]
        )

    @property
    def datetime(self):
        return self.structure[graphconstants.DATETIME]

    @datetime.setter
    def datetime(self, value):
        self.structure[GraphConstants.DATETIME] = value
        return self

    @property
    def activity(self):
        return self.structure[graphconstants.ACTIVITY]

    @activity.setter
    def activity(self, value: str):
        self.structure[GraphConstants.ACTIVITY] = value
        return self

    @property
    def directed(self):
        return self.structure[graphconstants.DIRECTED]

    @directed.setter
    def directed(self, value):
        self.structure[GraphConstants.DIRECTED] = value
        return self

    @property
    def line_style(self):
        return self.structure[graphconstants.LINE_STYLE]

    @line_style.setter
    def line_style(self, value: str):
        self.structure[GraphConstants.LINE_STYLE] = value
        return self

    @property
    def width(self):
        return self.structure[graphconstants.WIDTH]

    @width.setter
    def width(self, value):
        self.structure[GraphConstants.WIDTH] = value
        return self