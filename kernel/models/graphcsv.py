from kernel.models.node import Node
from kernel.models.transaction import Transaction

import csv

class GraphCSV:
    def __init__(self):
        self.csv = []

    def append_nodeset(self, source: Node, destination: Node, transaction: Transaction):
        merged = {
            **source.compress(),
            **destination.compress(),
            **transaction.compress()
        }

        self.csv.append(merged)

    def write_csv(self, out_file: str):
        headers = self.csv[0].keys()
        
        with open(out_file, 'w') as csv_out:
            csv_writer = csv.DictWriter(csv_out, headers, delimiter=",")
            csv_writer.writeheader()
            csv_writer.writerows(self.csv[0:50])
