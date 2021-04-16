#!/usr/bin/env python
import netfilterqueue
import subprocess


def process_packet(packet):
    print(packet)
    packet.drop()  # packet.accept() for accepting and forwarding the packets OR packet.drop() for dropping the packets


try:
    print("Formatting iptables rules...")
    subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

except KeyboardInterrupt:
    print("\nResetting iptables rules to original...")
    subprocess.call("iptables --flush", shell=True)
    print("Exiting...")
