from scapy.all import *

def process_packet(pkt):
    print("Ho letto un pkt sulla tua macchina")

sniff(iface="wlp3s0", filter="tcp", prn= process_packet)