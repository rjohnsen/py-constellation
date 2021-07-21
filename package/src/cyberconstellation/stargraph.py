from __future__ import division
from __future__ import print_function

import json
import math
import pprint
import sys
import zipfile

# Converted from https://github.com/constellation-app/constellation/blob/47e17cb76a0f1a88a86bd2c086802e84d3bd9a43/docs/source/graph/i_o/python-writer.rst
# Doc specification https://constellation.readthedocs.io/en/latest/graph/i_o/file-format.html

class StarGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.graph = []

    def append_node(self, src, dst):
        if not src.identifier in self.nodes.keys():
            self.nodes[src.identifier] = src

        if not dst.identifier in self.nodes.keys() == False:
            self.nodes[dst.identifier] = dst

        self.edges.append({
            "vx_src_": src.identifier,
            "vx_dst_": dst.identifier,
            "tx_dir_:": True
        })

    def __attr(self, label, type, descr, default=None):
        a = {
            #'mod_count': 0,
            'label': label,
            'type': type,
            'descr': descr
        }
        if default is not None:
            a['default'] = default

        return a

    def build(self):
        vertex_count = len(self.nodes)
        inc_angle = 360 / vertex_count
        radius = (vertex_count*3) / (2 * math.pi)


        vx_attrs = [
            self.__attr('x', 'float', 'x coord', 0),
            self.__attr('y', 'float', 'y coord', 0),
            self.__attr('z', 'float', 'z coord', 0),
            self.__attr('Name', 'string', 'Node name'),
            self.__attr('background_icon', 'icon', 'icon'),
            self.__attr('color', 'color', 'color')
        ]

        tx_attrs = []

        vx_data = []
        count = 0
        for _, node in self.nodes.items():
            name = node.label

            x = radius * math.cos(math.radians(count * inc_angle))
            y = radius * math.sin(math.radians(count * inc_angle))
            count += 1

            color = 'Yellow' if x>0 else 'Blue'
            vx = {
                'vx_id_': node.identifier,
                'Name': node.label,
                'x': x,
                'y': y,
                'z': 0,
                'background_icon': 'Background.Round Circle',
                'color': node.color
            }

            vx_data.append(vx)

        labels_data = {'bottom' : [{'attr':'Name', 'color':'Green'}]}

        graph = [
           {
                "version" : 2,
                "versionedItems" : {
                    "date" : 1,
                    "au.gov.asd.tac.constellation.schema.InteractiveSchemaFactory" : 4,
                    "datetime" : 1,
                    "graph_labels_transactions" : 1,
                    "blaze" : 1,
                    "graph_labels_nodes" : 1,
                    "time" : 1,
                    "time_zone" : 1,
                    "visual_state" : 1,
                    "au.gov.asd.tac.constellation.schema.AnalyticSchemaFactory" : 3
                },
                "schema" : "au.gov.asd.tac.constellation.schema.AnalyticSchemaFactory",
                "global_mod_count" : 359,
                "structure_mod_count" : 0,
                "attribute_mod_count" : 0
            },
            {
                'graph': [
                    {
                        'attrs':[self.__attr('color', 'color', 'color', 'Black')]
                    }, 
                    {
                        'data':[]
                    }
                ]
            },
            {
                'vertex': [
                    {
                        'attrs':vx_attrs
                    },
                    {
                        'data':vx_data
                    }
                ]
            },
            {
                'transaction': [
                    {
                        'attrs':tx_attrs
                        },
                        {  
                            'data':self.edges
                        }
                    ]
                },
            {
                'meta': [
                    {
                        'attrs':[
                            self.__attr('labels', 'labels', 'labels')
                        ]
                    },
                    {
                        'data':[
                            {
                                'labels':labels_data
                            }
                        ]
                    }
                ]
            }
        ]

        with zipfile.ZipFile('test.star', 'w') as zipped_f:
            zipped_f.writestr("graph.txt", json.dumps(graph, indent=2))






