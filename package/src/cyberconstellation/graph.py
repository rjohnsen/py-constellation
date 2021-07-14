from cyberconstellation.nodes import Node, Transaction

import csv

class GraphCSV(list):
    def append_nodeset(self, source: Node, destination: Node, transaction: Transaction):
        merged = {
            **source.compress(),
            **destination.compress(),
            **transaction.compress()
        }

        self.append(merged)

    def write_csv(self, out_file: str):
        headers = self[0].keys()
        
        with open(out_file, 'w') as csv_out:
            csv_writer = csv.DictWriter(csv_out, headers, delimiter=",")
            csv_writer.writeheader()
            csv_writer.writerows(self)
