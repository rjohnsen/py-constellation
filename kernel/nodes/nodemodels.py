"""
Nodes module

Module consists of three node classes

* NodeParent - inerrited in node implementations
* Node - regular node
* Transaction - transaction node

For implementing your own nodes, please inherit from NodeParent.

All documentation must be regarded as "best effort" due to varying documentation in the
Constallation-app project.
"""

from __future__ import annotations
import re

# pylint: disable=R0902
class NodeParent:
    """
    Parent class consolidating properties and methods for graph nodes (both node and transaction).
    """

    def __init__(self, annotation: str):
        """
        Default constructor

        Parameters:
        annotation (str): CSV header prefix
        """
        self.__annotation = annotation
        self.__identifier = None
        self.__type = None
        self.__source = None
        self.__label = None
        self.__color = None
        self.__dim = None
        self.__layer_mask = None
        self.__selected = None
        self.__layer_visibility = None

    def add_property(self, name: str, value: str) -> bool:
        """
        Add custom property

        Parameters:
        name (str): Name of property
        value (str): Value of property

        Returns:
        str:Returning bool
        """
        if name in self.__dict__.keys():
            return False

        setattr(self, name, value)
        return True

    def compress(self) -> dict:
        """
        Compress properties into dict for easier CSV handling.

        Returns:
        dict:Returning bool
        """
        compressed = {}

        for key, value in self.__dict__.items():
            if value is None:
                continue

            new_key = f"{self.annotation}.{re.sub(r'(^_[A-Za-z]+__)', '', key)}".lower()

            compressed[new_key] = value

        return compressed

    @property
    def annotation(self) -> str:
        """
        Get property 'annotation'. Annotation is prefixed to column headers in CSV output.

        Returns:
        str:Returning value
        """

        return self.__annotation

    @property
    def identifier(self) -> str:
        """
        Get node identifer

        Returns:
        str:Returning value
        """

        return self.__identifier

    @identifier.setter
    def identifier(self, value: str) -> NodeParent:
        """
        Set node identifer

        Parameters:
        value (str): Identifier

        Returns:
        NodeParent:Returning self
        """
        self.__identifier = value
        return self

    @property
    def type(self) -> str:
        """
        Get node type

        Returns:
        str:Returning value
        """
        return self.__type

    @type.setter
    def type(self, value: str) -> NodeParent:
        """
        Set node identifer

        Parameters:
        value (str): Identifier

        Returns:
        NodeParent:Returning self
        """
        self.__type = value
        return self

    @property
    def source(self) -> str:
        """
        Get node source

        Returns:
        str:Returning value
        """
        return self.__source

    @source.setter
    def source(self, value: str) -> NodeParent:
        """
        Set node source

        Parameters:
        value (str): Source

        Returns:
        NodeParent:Returning self
        """
        self.__source = value
        return self

    @property
    def label(self) -> str:
        """
        Get node label

        Returns:
        str:Returning Label
        """
        return self.__label

    @label.setter
    def label(self, value: str) -> NodeParent:
        """
        Set node label

        Parameters:
        value (str): Label

        Returns:
        NodeParent:Returning self
        """
        self.__label = value
        return self

    @property
    def color(self) -> str:
        """
        Get node color

        Returns:
        str:Returning value
        """
        return self.__color

    @color.setter
    def color(self, value: str) -> NodeParent:
        """
        Set node color

        Parameters:
        value (str): Color string or HEX code

        Returns:
        NodeParent:Returning self
        """
        self.__color = value
        return self

    @property
    def dim(self) -> bool:
        """
        Get node dim setting

        Returns:
        str:Returning value
        """
        return self.__dim

    @dim.setter
    def dim(self, value: bool) -> NodeParent:
        """
        Set node dim setting

        Parameters:
        value (bool): dim on/off

        Returns:
        NodeParent:Returning self
        """
        self.__dim = value
        return self

    @property
    def layer_mask(self) -> float:
        """
        Get node layer_mask (bitmask identifying the layers this node belongs to)

        Returns:
        float:Returning value
        """
        return self.__layer_mask

    @layer_mask.setter
    def layer_mask(self, value: float) -> NodeParent:
        """
        Set node layer_mask (bitmask identifying the layers this node belongs to)

        Parameters:
        value (float): Bitmask

        Returns:
        NodeParent:Returning self
        """
        self.__layer_mask = value
        return self

    @property
    def visibility(self) -> float:
        """
        Get node visibility

        Returns:
        float:Returning value
        """
        return self.__visibility

    @visibility.setter
    def visibility(self, value: float) -> NodeParent:
        """
        Get node visibility

        Parameters:
        value (float): Bitmask

        Returns:
        NodeParent:Returning self
        """
        self.__visibility = value
        return self

    @property
    def selected(self) -> bool:
        """
        Get selected state of node

        Returns:
        bool:Returning value
        """
        return self.__selected

    @selected.setter
    def selected(self, value: bool) -> NodeParent:
        """
        Set node visibility

        Parameters:
        value (bool): State

        Returns:
        NodeParent:Returning self
        """
        self.__selected = value
        return self

    @property
    def layer_visibility(self) -> float:
        """
        Get node visibility given the layer it belongs to

        Returns:
        float:Returning value
        """

        return self.__layer_visibility

    @layer_visibility.setter
    def layer_visibility(self, value: float):
        """
        Set node visibility given the layer it belongs to

        Parameters:
        value (float): Value

        Returns:
        NodeParent:Returning self
        """
        self.__layer_visibility = value
        return self

# pylint: disable=R0904,C0103,R0903
class Node(NodeParent):
    """
    Class representing a Node in graph
    """
    def __init__(self, annotation: str):
        """
        Default constructor

        Parameters:
        annotation (str): CSV header prefix
        """
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
    def raw(self) -> str:
        """
        Get node raw value

        Returns:
        str:Returning value
        """
        return self.__raw

    @raw.setter
    def raw(self, value: str) -> Node:
        """
        Set node raw value

        Parameters:
        value (str): Value

        Returns:
        Node:Returning self
        """
        self.__raw = value
        return self

    @property
    def background_icon(self) -> str:
        """
        Get background icon

        Returns:
        str:Returning value
        """
        return self.__background_icon

    @background_icon.setter
    def background_icon(self, value: str) -> Node:
        """
        Set background icon

        Parameters:
        value (str): Value

        Returns:
        Node:Returning self
        """
        self.__background_icon = value
        return self

    @property
    def icon(self) -> str:
        """
        Get icon

        Returns:
        str:Returning value
        """
        return self.__icon

    @icon.setter
    def icon(self, value: str) -> Node:
        """
        Set icon

        Parameters:
        value (str): Value

        Returns:
        Node:Returning self
        """
        self.__icon = value
        return self

    @property
    def nradius(self) -> float:
        """
        Get nradius

        Returns:
        float:Returning value
        """
        return self.__nradius

    @nradius.setter
    def nradius(self, value: float) -> Node:
        """
        Get nradius

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__nradius = value
        return self

    @property
    def pinned(self) -> bool:
        """
        Get pinned state

        Returns:
        bool:Returning value
        """
        return self.__pinned

    @pinned.setter
    def pinned(self, value: bool) -> Node:
        """
        Set pinned state

        Parameters:
        value (bool): Value

        Returns:
        Node:Returning self
        """
        self.__pinned = value
        return self

    @property
    def x(self) -> float:
        """
        Get X coordinate

        Returns:
        float:Returning value
        """
        return self.__x

    @x.setter
    def x(self, value: float) -> Node:
        """
        Set X coordinate

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__x = value
        return self

    @property
    def x2(self) -> float:
        """
        Get X2 coordinate

        Returns:
        float:Returning value
        """
        return self.__x2

    @x2.setter
    def x2(self, value: float) -> Node:
        """
        Set X2 coordinate

        Parameters:
        value (str): Value

        Returns:
        Node:Returning self
        """
        self.__x2 = value
        return self

    @property
    def y(self) -> float:
        """
        Get Y coordinate

        Returns:
        float:Returning value
        """
        return self.__y

    @y.setter
    def y(self, value: float) -> Node:
        """
        Set Y coordinate

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__y = value
        return self

    @property
    def y2(self) -> float:
        """
        Get Y2 coordinate

        Returns:
        float:Returning value
        """
        return self.__y2

    @y2.setter
    def y2(self, value: float) -> Node:
        """
        Set Y2 coordinate

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__y2 = value
        return self

    @property
    def z(self) -> float:
        """
        Get Z coordinate

        Returns:
        float:Returning value
        """
        return self.__z

    @z.setter
    def z(self, value: float) -> Node:
        """
        Set Z coordinate

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__z = value
        return self

    @property
    def z2(self) -> float:
        """
        Get Z2 coordinate

        Returns:
        float:Returning value
        """
        return self.__z2

    @z2.setter
    def z2(self, value: float) -> Node:
        """
        Set Z2 coordinate

        Parameters:
        value (float): Value

        Returns:
        Node:Returning self
        """
        self.__z2 = value
        return self

class Transaction(NodeParent):
    """
    Class representing a Transaction in graph
    """
    def __init__(self, annotation: str):
        """
        Default constructor

        Parameters:
        annotation (str): CSV header prefix
        """
        super().__init__(annotation)

        self.__datetime = None
        self.__activity = None
        self.__directed = None
        self.__line_style = None
        self.__width = None

    @property
    def datetime(self) -> str:
        """
        Get datetime

        Returns:
        str:Returning value
        """
        return self.__datetime

    @datetime.setter
    def datetime(self, value: str) -> Transaction:
        """
        Set datetime

        Parameters:
        value (str): datestring

        Returns:
        Transaction:Returning self
        """
        self.__datetime = value
        return self

    @property
    def activity(self) -> str:
        """
        Get activity

        Returns:
        str:Returning value
        """
        return self.__activity

    @activity.setter
    def activity(self, value: str) -> Transaction:
        """
        Get activity

        Parameters:
        value (str): activity

        Returns:
        Transaction:Returning self
        """
        self.__activity = value
        return self

    @property
    def directed(self) -> bool:
        """
        Get directed state

        Returns:
        str:Returning value
        """
        return self.__directed

    @directed.setter
    def directed(self, value: bool) -> Transaction:
        """
        Set directed state

        Parameters:
        value (bool): State

        Returns:
        Transaction:Returning self
        """
        self.__directed = value
        return self

    @property
    def line_style(self) -> str:
        """
        Get line style

        Returns:
        str:Returning value
        """
        return self.__line_style

    @line_style.setter
    def line_style(self, value: str) -> Transaction:
        """
        Set line style

        Parameters:
        value (str): Style

        Returns:
        Transaction:Returning self
        """
        self.__line_style = value
        return self

    @property
    def width(self) -> float:
        """
        Get line width

        Returns:
        float:Returning value
        """
        return self.__width

    @width.setter
    def width(self, value: float) -> Transaction:
        """
        Set line width

        Parameters:
        value (str): Value

        Returns:
        Transaction:Returning self
        """
        self.__width = value
        return self
