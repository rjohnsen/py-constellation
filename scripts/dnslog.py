"""
Demo DNS log parser

A demo on how to parse DNS log into Constellation-app supported CSV
"""

# pylint: disable=E0401

import ipaddress
import csv
from tqdm import tqdm

from cyberconstellation.nodes import Node, Transaction
from cyberconstellation.icons import Icons
from cyberconstellation.graph import GraphCSV

import cyberconstellation.constants as constants

def set_icon(ip_addr: str) -> str:
    """
    Set icon for IP

    Parameters:
    value (str): IP

    Returns:
    str:Icon name
    """

    if ipaddress.ip_address(ip_addr).is_global:
        return Icons.SERVER

    return Icons.LAPTOP

def run(log_path: str):
    """
    Run parser

    Parameters:
    value (str): Path to log
    """
    with open(log_path, "r") as log_file:
        graphcsv = GraphCSV()
        reader = csv.reader(log_file, delimiter="\t")
        output_filename = "dnslog.csv"

        print("DNS Log parser DEMO - Roger Johnsen, 2021")
        print(f"Processing '{log_path}'\n")

        count = 0

        for line in tqdm(reader):
            # Prepare variables for easy access
            source_ip = line[2]
            destination_ip = line[4]
            protocol = line[6]

            # Source node
            source_node = Node("src")
            source_node.source = "Imported"
            source_node.label = source_ip
            source_node.icon = set_icon(source_ip)
            source_node.identifier = f'Node {source_ip}'
            source_node.raw = f'{source_node.identifier} <Network>'
            source_node.color = "blue"

            # Destination node
            destination_node = Node("dst")
            destination_node.source = "Imported"
            destination_node.label = destination_ip
            destination_node.icon = set_icon(destination_ip)
            destination_node.identifier = f'Node {destination_ip}'
            destination_node.raw = f'{destination_node.identifier} <Network>'
            destination_node.color = "orange"

            # Transactions
            transaction = Transaction("trans")
            transaction.label = protocol
            transaction.directed = True
            transaction.type = constants.TRANSACTION_TYPE_COMMUNICATION
            transaction.line_style = constants.TRANSACTION_LINE_STYLE_DASHED
            transaction.color = "green"

            # Connect the graph
            graphcsv.append_nodeset(
                source_node,
                destination_node,
                transaction
            )

            if count > 2:
                break

            count += 1

        graphcsv.write_csv(output_filename)

        print(f"\nProcessing done and results written to '{output_filename}'!")

if __name__ == "__main__":
    run("logs/dns.log")
