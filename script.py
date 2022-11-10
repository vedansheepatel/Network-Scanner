#Network Scanner - Vedanshee Patel 
#Scan active hosts in the local area network  

#import scapy package
import scapy.all as scapy

# set the IP Address for the destination
#/24 to scan addresses ranging from 1.0 - 255
ip_target = "192.168.2.201/24"

# create ARP packet
arp_packet=scapy.ARP()

# make the arp packet destination = target ip address
arp_packet.pdst = ip_target

# create the Ether broadcast packet
broadcast_packet = scapy.Ether()
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
broadcast_packet.dst = "ff:ff:ff:ff:ff:ff"

# combine the ether frame and arp request 
request = broadcast_packet/arp_packet

#send to network to recieve the responses
result = scapy.srp(request, timeout=3, verbose=0)[0]

# create a list of clients
clients = []

# fill list of clients with the response packets
for sent, received in result:
    # add the ip and mac address to client list 
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))