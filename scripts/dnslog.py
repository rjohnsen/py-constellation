from kernel.models.graphcsv import GraphCSV

from kernel.nodes.models import Node, Transaction, NodeParent
from kernel.constants.transaction import Transaction as TRCon
from kernel.lib.icons import Icons

import ipaddress
import csv

def set_icon(ip: str) -> str:
    if ipaddress.ip_address(ip).is_global:
        return Icons.SERVER
    
    return Icons.LAPTOP

def run(log_path: str):
    with open(log_path, "r") as log_file:
        graphcsv = GraphCSV()

        for line in csv.reader(log_file, delimiter="\t"):
            #
            # Prepare variables for easy access
            # 
            source_ip = line[2]
            destination_ip = line[4]
            protocol = line[6]
            dns_req = line[5]

            #
            # Source node
            # 
            source_node = Node("src")
            source_node.source = "Imported"
            source_node.label = source_ip
            source_node.icon = set_icon(source_ip)
            source_node.identifier = f'Node {source_ip}'
            source_node.raw = f'{source_node.identifier} <Network>'
            source_node.color = "blue"

            #
            # Destination node
            #
            destination_node = Node("dst")
            destination_node.source = "Imported"
            destination_node.label = destination_ip
            destination_node.icon = set_icon(destination_ip)
            destination_node.identifier = f'Node {destination_ip}'
            destination_node.raw = f'{destination_node.identifier} <Network>'
            destination_node.color = "orange"

            # 
            # Transactions
            # 
            transaction = Transaction("trans")
            transaction.label = protocol
            transaction.directed = True
            transaction.type = "Network"
            transaction.line_style = TRCon.LINE_STYLE_DOTTED
            transaction.color = "green"
            #
            # Connect the graph
            # 
            graphcsv.append_nodeset(
                source_node,
                destination_node,
                transaction
            )

        graphcsv.write_csv("dnslog.csv")

if __name__ == "__main__":
    run("logs/dns.log")