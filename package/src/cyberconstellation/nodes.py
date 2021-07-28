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
import uuid

from cyberconstellation.typecheck import typecheck

import random
import time

# pylint: disable=R0902
class NodeParent:
    """
    Parent class consolidating properties and methods for graph nodes (both node and transaction).
    """

    @typecheck(str)
    def __init__(self, annotation: str):
        """
        Default constructor

        Parameters:
        annotation (str): CSV header prefix
        """

        self.__annotation = annotation
        self.__identifier = random.randint(0, int(time.time()))
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

        for prop, _ in self.__dict__.items():
            if re.sub(r"(^_[A-Za-z]+__)", "", prop) == name:
                return False

        setattr(self, name, value)

        return True

    def get_property(self, name: str):
        """
        Get property

        Parameters:
        name (str): Name of property

        Returns:
        str:Returning value
        """

        return getattr(self, name)

    def compress(self) -> dict:
        """
        Compress properties into dict for easier CSV handling.

        Returns:
        dict:Returning bool
        """

        compressed = {}

        for key, value in self.__dict__.items():
            if value in [ None, self.annotation ]:
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
        Get node identifier

        Returns:
        str:Returning value
        """

        return self.__identifier

    @identifier.setter
    @typecheck(str)
    def identifier(self, value: str):
        """
        Set node identifier

        Parameters:
        value (str): Identifier
        """

        self.__identifier = value

    @property
    def type(self) -> str:
        """
        Get node type

        Returns:
        str:Returning value
        """

        return self.__type

    @type.setter
    @typecheck(str)
    def type(self, value: str):
        """
        Set node identifier

        Parameters:
        value (str): Identifier
        """

        self.__type = value

    @property
    def source(self) -> str:
        """
        Get node source

        Returns:
        str:Returning value
        """

        return self.__source

    @source.setter
    @typecheck(str)
    def source(self, value: str):
        """
        Set node source

        Parameters:
        value (str): Source
        """

        self.__source = value

    @property
    def label(self) -> str:
        """
        Get node label

        Returns:
        str:Returning Label
        """

        return self.__label

    @label.setter
    @typecheck(str)
    def label(self, value: str):
        """
        Set node label

        Parameters:
        value (str): Label
        """

        self.__label = value

    @property
    def color(self) -> str:
        """
        Get node color

        Returns:
        str:Returning value
        """

        return self.__color

    @color.setter
    @typecheck(str)
    def color(self, value: str):
        """
        Set node color

        Parameters:
        value (str): Color string or HEX code
        """

        self.__color = value

    @property
    def dim(self) -> bool:
        """
        Get node dim setting

        Returns:
        str:Returning value
        """

        return self.__dim

    @dim.setter
    @typecheck(bool)
    def dim(self, value: bool):
        """
        Set node dim setting

        Parameters:
        value (bool): dim on/off
        """

        self.__dim = value

    @property
    def layer_mask(self) -> float:
        """
        Get node layer_mask (bitmask identifying the layers this node belongs to)

        Returns:
        float:Returning value
        """

        return self.__layer_mask

    @layer_mask.setter
    @typecheck(float)
    def layer_mask(self, value: float):
        """
        Set node layer_mask (bitmask identifying the layers this node belongs to)

        Parameters:
        value (float): Bitmask
        """

        self.__layer_mask = value

    @property
    def visibility(self) -> float:
        """
        Get node visibility

        Returns:
        float:Returning value
        """

        return self.__visibility

    @visibility.setter
    @typecheck(float)
    def visibility(self, value: float):
        """
        Get node visibility

        Parameters:
        value (float): Bitmask
        """

        self.__visibility = value

    @property
    def selected(self) -> bool:
        """
        Get selected state of node

        Returns:
        bool:Returning value
        """

        return self.__selected

    @selected.setter
    @typecheck(bool)
    def selected(self, value: bool):
        """
        Set node visibility

        Parameters:
        value (bool): State
        """

        self.__selected = value

    @property
    def layer_visibility(self) -> float:
        """
        Get node visibility given the layer it belongs to

        Returns:
        float:Returning value
        """

        return self.__layer_visibility

    @layer_visibility.setter
    @typecheck(float)
    def layer_visibility(self, value: float):
        """
        Set node visibility given the layer it belongs to

        Parameters:
        value (float): Value
        """

        self.__layer_visibility = value

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
    @typecheck(str)
    def raw(self, value: str) -> Node:
        """
        Set node raw value

        Parameters:
        value (str): Value

        Returns:
        Node:Returning self
        """
        self.__raw = value

    @property
    def background_icon(self) -> str:
        """
        Get background icon

        Returns:
        str:Returning value
        """
        return self.__background_icon

    @background_icon.setter
    @typecheck(str)
    def background_icon(self, value: str):
        """
        Set background icon

        Parameters:
        value (str): Value
        """
        self.__background_icon = value

    @property
    def icon(self) -> str:
        """
        Get icon

        Returns:
        str:Returning value
        """
        return self.__icon

    @icon.setter
    @typecheck(str)
    def icon(self, value: str):
        """
        Set icon

        Parameters:
        value (str): Value
        """
        self.__icon = value

    @property
    def nradius(self) -> float:
        """
        Get nradius

        Returns:
        float:Returning value
        """
        return self.__nradius

    @nradius.setter
    @typecheck(float)
    def nradius(self, value: float):
        """
        Get nradius

        Parameters:
        value (float): Value
        """
        self.__nradius = value

    @property
    def pinned(self) -> bool:
        """
        Get pinned state

        Returns:
        bool:Returning value
        """
        return self.__pinned

    @pinned.setter
    @typecheck(bool)
    def pinned(self, value: bool):
        """
        Set pinned state

        Parameters:
        value (bool): Value
        """
        self.__pinned = value

    @property
    def x(self) -> float:
        """
        Get X coordinate

        Returns:
        float:Returning value
        """
        return self.__x

    @x.setter
    @typecheck(float)
    def x(self, value: float):
        """
        Set X coordinate

        Parameters:
        value (float): Value
        """
        self.__x = value

    @property
    def x2(self) -> float:
        """
        Get X2 coordinate

        Returns:
        float:Returning value
        """
        return self.__x2

    @x2.setter
    @typecheck(float)
    def x2(self, value: float):
        """
        Set X2 coordinate

        Parameters:
        value (str): Value
        """
        self.__x2 = value

    @property
    def y(self) -> float:
        """
        Get Y coordinate

        Returns:
        float:Returning value
        """
        return self.__y

    @y.setter
    @typecheck(float)
    def y(self, value: float):
        """
        Set Y coordinate

        Parameters:
        value (float): Value
        """
        self.__y = value

    @property
    def y2(self) -> float:
        """
        Get Y2 coordinate

        Returns:
        float:Returning value
        """
        return self.__y2

    @y2.setter
    @typecheck(float)
    def y2(self, value: float):
        """
        Set Y2 coordinate

        Parameters:
        value (float): Value
        """
        self.__y2 = value

    @property
    def z(self) -> float:
        """
        Get Z coordinate

        Returns:
        float:Returning value
        """
        return self.__z

    @z.setter
    @typecheck(float)
    def z(self, value: float):
        """
        Set Z coordinate

        Parameters:
        value (float): Value
        """
        self.__z = value

    @property
    def z2(self) -> float:
        """
        Get Z2 coordinate

        Returns:
        float:Returning value
        """
        return self.__z2

    @z2.setter
    @typecheck(float)
    def z2(self, value: float):
        """
        Set Z2 coordinate

        Parameters:
        value (float): Value
        """
        self.__z2 = value

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
    @typecheck(str)
    def datetime(self, value: str):
        """
        Set datetime

        Parameters:
        value (str): datestring
        """
        self.__datetime = value

    @property
    def activity(self) -> str:
        """
        Get activity

        Returns:
        str:Returning value
        """
        return self.__activity

    @activity.setter
    @typecheck(str)
    def activity(self, value: str):
        """
        Get activity

        Parameters:
        value (str): activity
        """
        self.__activity = value

    @property
    def directed(self) -> bool:
        """
        Get directed state

        Returns:
        str:Returning value
        """
        return self.__directed

    @directed.setter
    @typecheck(bool)
    def directed(self, value: bool):
        """
        Set directed state

        Parameters:
        value (bool): State
        """
        self.__directed = value

    @property
    def line_style(self) -> str:
        """
        Get line style

        Returns:
        str:Returning value
        """
        return self.__line_style

    @line_style.setter
    @typecheck(str)
    def line_style(self, value: str):
        """
        Set line style

        Parameters:
        value (str): Style
        """
        self.__line_style = value

    @property
    def width(self) -> float:
        """
        Get line width

        Returns:
        float:Returning value
        """
        return self.__width

    @width.setter
    @typecheck(float)
    def width(self, value: float):
        """
        Set line width

        Parameters:
        value (str): Value
        """
        self.__width = value
