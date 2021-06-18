from scapy.all import*
for pkt in sniff(iface='Wi-Fi', count =5):
       print('Packet: ' + str(pkt.summary()) + '\n');