from scapy.all import rdpcap

packets = rdpcap('./exfiltration_activity_pctf_challenge.pcapng')
for packet in packets:
    if packet.haslayer('ICMP'):
        print(chr(packet['IP'].ttl),end="")