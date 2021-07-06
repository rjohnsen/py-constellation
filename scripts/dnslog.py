from kernel.models.graphcsv import GraphCSV
from kernel.models.node import Node
from kernel.models.transaction import Transaction
from kernel.lib.icons import Icons

import csv

def run(log_path: str):
    with open(log_path, "r") as log_file:
        graphcsv = GraphCSV()

        for line in csv.reader(log_file, delimiter="\t"):
            source_ip = line[2]
            destination_ip = line[4]
            protocol = line[6]
            dns_req = line[5]

            #--- 

            source_node = Node("src")
            source_node.source = source_ip
            source_node.icon = Icons.LAPTOP

            destination_node = Node("dst")
            destination_node.source = destination_ip
            destination_node.icon = Icons.LAPTOP

            transaction = Transaction("trans")
            transaction.label = dns_req

            graphcsv.append_nodeset(
                source_node,
                destination_node,
                transaction
            )

        graphcsv.write_csv("dnslog.csv")

if __name__ == "__main__":
    run("logs/dns.log")