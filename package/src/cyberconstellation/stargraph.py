from __future__ import division
from __future__ import print_function

import json
import math
import pprint
import sys
import zipfile
import jinja2

import pkgutil

# Converted from https://github.com/constellation-app/constellation/blob/47e17cb76a0f1a88a86bd2c086802e84d3bd9a43/docs/source/graph/i_o/python-writer.rst
# Doc specification https://constellation.readthedocs.io/en/latest/graph/i_o/file-format.html

class StarGraph:
    def __init__(self):
        self.document = None

    def append_node(self, src, dst):
        None

    def build(self):
        # Read template
        file_structure = json.loads(pkgutil.get_data(__name__, "templates/starfilev2.tpl"))

        with zipfile.ZipFile('test2.star', 'w') as zipped_f:
            zipped_f.writestr("graph.txt", json.dumps(file_structure))

        






