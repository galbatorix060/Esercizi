from scapy.all import *
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse

iPkt = 0

def process_packet(packet):

    global iPkt
    iPkt += 1
    print("Ho letto un pkt sulla tua macchina " + str(iPkt))

    if not packet.haslayer(IP):
        return
    ip_layer = "IP_SRC: " + packet[IP].src+" IP_DST: " + packet[IP].dst + " " + str(packet[IP].proto) + " " + str(packet[IP].len)
    print(ip_layer)

    if packet[IP].proto == 6:
        print("TCP_SRC_PORT: " + str(packet[TCP].sport) + " TCP_DST_PORT: " + str(packet[TCP].dport))
    if packet[TCP].sport == 433 or packet[TCP].dport == 443:
        print("E' un protocollo TLS")
    if packet[TCP].sport == 80 or packet[TCP].dport == 80:
        print("E' un protocollo HTTP")
    if packet[TCP].dport == 80:
        print("E' una request\n\n\n")
        if packet.haslayer(HTTPResponse):
            print(packet[HTTPResponse].show())
    if packet[TCP].sport == 80:
        print("E' una response\n\n\n")
        if packet.haslayer(HTTPRequest):
            print(packet[HTTPRequest].show())


sniff(iface="wlp3s0", filter="tcp", prn= process_packet)

