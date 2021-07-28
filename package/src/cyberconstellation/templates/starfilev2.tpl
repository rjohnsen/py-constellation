[ {
  "version" : 2,
  "versionedItems" : {
    "date" : 1,
    "datetime" : 1,
    "graph_labels_transactions" : 1,
    "au.gov.asd.tac.constellation.graph.schema.VisualSchemaFactory" : 5,
    "blaze" : 1,
    "graph_labels_nodes" : 1,
    "au.gov.asd.tac.constellation.graph.schema.AnalyticSchemaFactory" : 4,
    "time" : 1,
    "time_zone" : 1,
    "visual_state" : 1
  },
  "schema" : "au.gov.asd.acsc.constellation.schema.cyberschema.CyberSchemaFactory",
  "global_mod_count" : 287,
  "structure_mod_count" : 28,
  "attribute_mod_count" : 28
}, {
  "graph" : [ {
    "attrs" : [ {
      "label" : "3d_display",
      "type" : "boolean",
      "descr" : "Whether or not the graph is being displayed in 3D",
      "default" : true,
      "mod_count" : 0
    }, {
      "label" : "blaze_opacity",
      "type" : "float",
      "descr" : "The opacity of blazes on the graph",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "blaze_size",
      "type" : "float",
      "descr" : "The size of blazes on the graph",
      "default" : 0.30000001192092896,
      "mod_count" : 0
    }, {
      "label" : "layer_bitmask_selected",
      "type" : "long",
      "descr" : "The layers currently enabled for display",
      "default" : "1",
      "mod_count" : 0
    }, {
      "label" : "camera",
      "type" : "camera",
      "descr" : "The camera used to view and navigate around the graph",
      "default" : "Camera[eye: 3f[0,000000,0,000000,10,000000]; centre: 3f[0,000000,0,000000,0,000000]; up: 3f[0,000000,1,000000,0,000000]]",
      "mod_count" : 13
    }, {
      "label" : "max_transactions",
      "type" : "integer",
      "descr" : "The maximum number of transactions to draw",
      "default" : 8.0,
      "mod_count" : 0
    }, {
      "label" : "node_color_reference",
      "type" : "vertex_attribute_name",
      "descr" : "The name of the node attribute that will determine node colors",
      "mod_count" : 0
    }, {
      "label" : "node_labels_bottom",
      "type" : "graph_labels_nodes",
      "descr" : "The labels beneath nodes",
      "default" : "",
      "mod_count" : 1
    }, {
      "label" : "draw_directed_transactions",
      "type" : "boolean",
      "descr" : "Whether or not the transactions being added in draw mode are directed",
      "default" : true,
      "mod_count" : 0
    }, {
      "label" : "draw_flags",
      "type" : "draw_flags",
      "descr" : "The graph elements to draw.",
      "default" : "31",
      "mod_count" : 0
    }, {
      "label" : "node_labels_top",
      "type" : "graph_labels_nodes",
      "descr" : "The labels above nodes",
      "default" : "",
      "mod_count" : 1
    }, {
      "label" : "highlight_color",
      "type" : "color",
      "descr" : "The highlight color of the graph",
      "default" : "Cherry",
      "mod_count" : 0
    }, {
      "label" : "connection_opacity",
      "type" : "float",
      "descr" : "The opacity of connections on the graph",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "mix_color",
      "type" : "color",
      "descr" : "The colour to use for edges and links that contain transactions with a variety of colours.",
      "default" : "Clouds",
      "mod_count" : 0
    }, {
      "label" : "visible_above_threshold",
      "type" : "boolean",
      "descr" : "Whether or not the graph is visible even when the maximum number of nodes is exceeded.",
      "default" : true,
      "mod_count" : 0
    }, {
      "label" : "visibility_threshold",
      "type" : "integer",
      "descr" : "The maximum number of nodes to display",
      "default" : 50000.0,
      "mod_count" : 0
    }, {
      "label" : "background_color",
      "type" : "color",
      "descr" : "The background color of the graph",
      "default" : "Night Sky",
      "mod_count" : 0
    }, {
      "label" : "transaction_labels",
      "type" : "graph_labels_transactions",
      "descr" : "The labels on transactions",
      "default" : "",
      "mod_count" : 1
    }, {
      "label" : "decorators",
      "type" : "decorators",
      "descr" : "The decorators on nodes",
      "default" : ";;;;",
      "mod_count" : 1
    }, {
      "label" : "connection_mode",
      "type" : "connection_mode",
      "descr" : "The mode in which to display connections on the graph (transaction, edge or link).",
      "default" : "EDGE",
      "mod_count" : 0
    }, {
      "label" : "transaction_color_reference",
      "type" : "transaction_attribute_name",
      "descr" : "The name of the transaction attribute that will determine transaction colors",
      "mod_count" : 0
    }, {
      "label" : "drawing_mode",
      "type" : "boolean",
      "descr" : "Whether or not the graph is in drawing mode (as opposed to the normal selection mode)",
      "default" : false,
      "mod_count" : 0
    } ]
  }, {
    "data" : [ {
      "camera" : {
        "look_at_eye" : [ 0.0, 0.0, 16.0 ],
        "look_at_centre" : [ 0.0, 0.0, 0.0 ],
        "look_at_up" : [ 0.0, 1.0, 0.0 ],
        "look_at_rotation" : [ 0.0, 0.0, 0.0 ],
        "look_at_previous_eye" : [ 0.0, 0.0, 10.0 ],
        "look_at_previous_centre" : [ 0.0, 0.0, 0.0 ],
        "look_at_previous_up" : [ 0.0, 1.0, 0.0 ],
        "look_at_previous_rotation" : [ 0.0, 0.0, 0.0 ],
        "frame" : {
          "origin" : [ 0.0, 0.0, 0.0 ],
          "forward" : [ 0.0, 0.0, 1.0 ],
          "up" : [ 0.0, 1.0, 0.0 ]
        },
        "bounding_box" : {
          "is_empty" : true
        },
        "visibility_low" : 0.0,
        "visibility_high" : 1.0,
        "mix_ratio" : 0
      },
      "node_labels_bottom" : [ {
        "attribute_name" : "Label",
        "color" : {
          "name" : "LightBlue"
        },
        "radius" : 1.0
      } ],
      "node_labels_top" : [ ],
      "highlight_color" : {
        "name" : "Cherry"
      },
      "mix_color" : {
        "name" : "Clouds"
      },
      "background_color" : {
        "name" : "Night Sky"
      },
      "transaction_labels" : [ {
        "attribute_name" : "Count",
        "color" : {
          "name" : "LightBlue"
        },
        "radius" : 1.0
      } ],
      "decorators" : {
        "north_west" : "Geo.Country",
        "north_east" : "pinned",
        "south_east" : null,
        "south_west" : null
      }
    } ]
  } ]
}, {
  "vertex" : [ {
    "attrs" : [ {
      "label" : "Raw",
      "type" : "raw",
      "descr" : "The raw identifier and type of this node",
      "default" : "",
      "mod_count" : 24
    }, {
      "label" : "layer_visibility",
      "type" : "float",
      "descr" : "The visibility of the vertex given the layers it belongs to",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "layer_mask",
      "type" : "long",
      "descr" : "Bitmask identifying the layers this vertex belongs to",
      "default" : "1",
      "merger" : "au.gov.asd.tac.constellation.graph.mergers.BitwiseOrGraphAttributeMerger",
      "mod_count" : 0
    }, {
      "label" : "icon",
      "type" : "icon",
      "descr" : "The icon of the vertex",
      "default" : "",
      "mod_count" : 20
    }, {
      "label" : "Type",
      "type" : "vertex_type",
      "descr" : "The type of this node",
      "mod_count" : 19
    }, {
      "label" : "x",
      "type" : "float",
      "descr" : "The x coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 4
    }, {
      "label" : "y",
      "type" : "float",
      "descr" : "The y coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 4
    }, {
      "label" : "z",
      "type" : "float",
      "descr" : "The z coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 0
    }, {
      "label" : "nradius",
      "type" : "float",
      "descr" : "The radius of the vertex",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "Label",
      "type" : "string",
      "descr" : "The label of the vertex",
      "mod_count" : 24
    }, {
      "label" : "dim",
      "type" : "boolean",
      "descr" : "Specifies whether the vertex is displayed in a dimmed state",
      "default" : false,
      "mod_count" : 0
    }, {
      "label" : "Identifier",
      "type" : "string",
      "descr" : "The identifier of the node",
      "mod_count" : 19
    }, {
      "label" : "selected",
      "type" : "boolean",
      "descr" : "Is the vertex selected?",
      "default" : false,
      "mod_count" : 0
    }, {
      "label" : "visibility",
      "type" : "float",
      "descr" : "The visibility of the vertex",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "x2",
      "type" : "float",
      "descr" : "The alternative x coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 0
    }, {
      "label" : "pinned",
      "type" : "boolean",
      "descr" : "Is the vertex position pinned?",
      "default" : false,
      "mod_count" : 0
    }, {
      "label" : "color",
      "type" : "color",
      "descr" : "The color of the vertex",
      "mod_count" : 20
    }, {
      "label" : "Source",
      "type" : "string",
      "descr" : "The source of this node",
      "mod_count" : 16
    }, {
      "label" : "background_icon",
      "type" : "icon",
      "descr" : "The background icon of the vertex",
      "default" : "Background.Flat Square",
      "mod_count" : 0
    }, {
      "label" : "y2",
      "type" : "float",
      "descr" : "The alternative y coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 0
    }, {
      "label" : "z2",
      "type" : "float",
      "descr" : "The alternative z coordinate of the vertex",
      "default" : 0.0,
      "mod_count" : 0
    } ],
    "key" : [ "Identifier", "Type" ]
  }, {
    "data" : [ 
        {%- for node in nodes -%}
        {
            "vx_id_" : {{node.identifier}},
            "Raw" : {
                "rawIdentifier" : "{{ node.raw }}",
                "rawType" : "Network"
            },
            "icon" : "{{ node.icon }}",
            "Type" : {
                "Name" : "{{ node.type }}",
                "Description" : "A node representing a type which is not currently part of the analytic schema",
                "Color" : {
                    "name" : "{{ node.color }}"
                },
                "Foreground Icon" : "Unknown",
                "Background Icon" : "Background.Flat Square",
                "Properties" : { },
                "Incomplete" : false
            },
            "x" : {{node.x}},
            "y" : {{node.y}},
            "z" : {{node.z}},
            "Label" : "{{ node.label }}",
            "Identifier" : "{{ node.identifier }}",
            "color" : {
                "name" : "{{ node.color }}"
            },
            "Source" : "{{ node.source }}",
            "background_icon" : "Background.Flat Square"
        }, 
        {%- endfor -%}
    ]
  } 
  ]
}, {
  "transaction" : [ {
    "attrs" : [ {
      "label" : "Label",
      "type" : "string",
      "descr" : "The label of the transaction",
      "mod_count" : 8
    }, {
      "label" : "Activity",
      "type" : "string",
      "descr" : "The type of activity this transaction represents",
      "mod_count" : 0
    }, {
      "label" : "dim",
      "type" : "boolean",
      "descr" : "Specified whether the transaction is displayed in a dimmed state",
      "default" : false,
      "mod_count" : 0
    }, {
      "label" : "Identifier",
      "type" : "string",
      "descr" : "The identifier of the transaction",
      "mod_count" : 7
    }, {
      "label" : "selected",
      "type" : "boolean",
      "descr" : "Is the transaction selected?",
      "default" : false,
      "mod_count" : 0
    }, {
      "label" : "layer_visibility",
      "type" : "float",
      "descr" : "The visibility of the transaction given the layers it belongs to",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "visibility",
      "type" : "float",
      "descr" : "The visibility of the transaction",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "layer_mask",
      "type" : "long",
      "descr" : "Bitmask identifying the layers this transaction belongs to",
      "default" : "1",
      "merger" : "au.gov.asd.tac.constellation.graph.mergers.BitwiseOrGraphAttributeMerger",
      "mod_count" : 0
    }, {
      "label" : "color",
      "type" : "color",
      "descr" : "The color of the transaction",
      "mod_count" : 8
    }, {
      "label" : "Source",
      "type" : "string",
      "descr" : "The source of the transaction",
      "mod_count" : 3
    }, {
      "label" : "directed",
      "type" : "boolean",
      "descr" : "Is the transaction directed?",
      "default" : false,
      "mod_count" : 4
    }, {
      "label" : "line_style",
      "type" : "line_style",
      "descr" : "The line style of the transaction",
      "default" : "SOLID",
      "mod_count" : 8
    }, {
      "label" : "Type",
      "type" : "transaction_type",
      "descr" : "The type of the transaction",
      "mod_count" : 7
    }, {
      "label" : "width",
      "type" : "float",
      "descr" : "The width of the transaction",
      "default" : 1.0,
      "mod_count" : 0
    }, {
      "label" : "DateTime",
      "type" : "datetime",
      "descr" : "The datetime at which this transaction occurred",
      "mod_count" : 3
    } ],
    "key" : [ "Identifier", "Type", "DateTime", "Source" ]
  }, {
    "data" : [ 
      {%- for transaction in transactions -%}
      {
      "tx_id_" : {{transaction["tx_id_"]}},
      "vx_src_" : {{transaction["vx_src_"]}},
      "vx_dst_" : {{transaction["vx_dst_"]}},
      "tx_dir_" : true,
      "Label" : "Communication",
      "Identifier" : {{transaction["tx_id_"]}},
      "color" : {
        "name" : "Green"
      },
      "directed" : true,
      "Type" : {
        "Name" : "Communication",
        "Description" : "A transaction representing a communication between two entities, eg. a phone made a call to another phone",
        "Color" : {
          "name" : "Green"
        },
        "Style" : "SOLID",
        "Directed" : true,
        "Properties" : { },
        "Incomplete" : false
      }
    },
    {%- endfor -%}
    ]
  } 
  ]
}, {
  "meta" : [ {
    "attrs" : [ ]
  }, {
    "data" : [ { } ]
  } ]
} ]