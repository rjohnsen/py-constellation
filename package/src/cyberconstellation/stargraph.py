from __future__ import division
from __future__ import print_function

import ast
import json
import math
import pprint
import sys
import zipfile
from jinja2 import Template
import pkgutil
import random
import time

# Converted from https://github.com/constellation-app/constellation/blob/47e17cb76a0f1a88a86bd2c086802e84d3bd9a43/docs/source/graph/i_o/python-writer.rst
# Doc specification https://constellation.readthedocs.io/en/latest/graph/i_o/file-format.html

class StarGraph:
    def __init__(self):
        self.document = None
        self.nodes = {}
        self.edges = []

    def append_node(self, src, dst):
        if not src.identifier in self.nodes.keys():
            self.nodes[src.identifier] = src

        if not dst.identifier in self.nodes.keys() == False:
            self.nodes[dst.identifier] = dst

        self.edges.append({
            "tx_id_": random.randint(0, int(time.time())),
            "vx_src_": src.identifier,
            "vx_dst_": dst.identifier,
            "tx_dir_:": True
        })

    def build(self):
        # Read template
        file_structure = Template(pkgutil.get_data(__name__, "templates/starfilev2.tpl").decode('UTF-8'))

        # Calculate placement
        vertex_count = len(self.nodes)
        inc_angle = 360 / vertex_count
        radius = (vertex_count*3) / (2 * math.pi)

        count = 1
        for _, node in self.nodes.items():
            node.x = float(radius * math.cos(math.radians(count * inc_angle)))
            node.y = float(radius * math.sin(math.radians(count * inc_angle)))
            node.z = float(0)
            count += 1

        with zipfile.ZipFile('test2.star', 'w') as zipped_f:
            rendered = file_structure.render(nodes=self.nodes.values(), transactions=self.edges)
            zipped_f.writestr("graph.txt", rendered)

        with open('something.txt', 'w') as out:
            out.write(rendered)

