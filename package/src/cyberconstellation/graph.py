"""
GraphCSV module

Utility module for preparing CSV output of nodes
"""

import csv

from cyberconstellation.nodes import Node, Transaction

class GraphCSV(list):
    """
    Class representing a structure for holding nodes for CSV output
    """
    def append_nodeset(self, source: Node, destination: Node, transaction: Transaction):
        """
        Append node set to CSV structure

        Parameters:
        source (Node): Start node
        destination (Node): Destination node
        transaction(Transaction): Transaction node
        """
        merged = {
            **source.compress(),
            **destination.compress(),
            **transaction.compress()
        }

        self.append(merged)

    def write_csv(self, out_file: str):
        """
        Write node structure to CSV

        Parameters:
        out_file (str): Output filepath
        """
        headers = self[0].keys()

        with open(out_file, 'w') as csv_out:
            csv_writer = csv.DictWriter(csv_out, headers, delimiter=",")
            csv_writer.writeheader()
            csv_writer.writerows(self)
