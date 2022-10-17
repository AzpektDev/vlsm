print("Enter ip adress with mask (e.g. 192.168.10.0/27)")
ipwm = input()
print("Enter how many subnets you need")
subnets = int(input())
print("Enter how many hosts per subnet")
hosts = int(input())
ip, mask = ipwm.split("/")

mask = int(mask)

if mask < 8:
    print("Invalid mask (must be 8 or greather)")
    exit(-1)

ip = ip.split(".")
for x in range(len(ip)):
    ip[x] = int(ip[x])

for x in range(len(ip)):
    ip[x] = bin(ip[x])[2:].zfill(8)

ip = "".join(ip)

netmask = "1" * mask + "0" * (32 - mask)
netmask = netmask[0:8] + "." + netmask[8:16] + "." + netmask[16:24] + "." + netmask[24:32]

def calculate_and(n1, n2):
    result = ""
    for x in range(len(n1)):
        if n1[x] == "1" and n2[x] == "1":
            result += "1"
        else:
            result += "0"
    result = result[0:8] + "." + result[8:16] + "." + result[16:24] + "." + result[24:32]
    return result

calculated_and = calculate_and(ip, netmask)

subnets_bits = 0
while subnets > 2 ** subnets_bits:
    subnets_bits += 1

hosts_bits = 0
while hosts >= 2 ** hosts_bits:
    hosts_bits += 1

with open('output.txt', 'w') as output_file:
    for x in range(subnets):
        network_adress = ip[0:mask] + bin(x)[2:].zfill(subnets_bits) + "0" * (32 - mask - subnets_bits)
        network_adress = network_adress[0:8] + "." + network_adress[8:16] + "." + network_adress[16:24] + "." + network_adress[24:32]
        network_adress = network_adress.split(".")
        for y in range(len(network_adress)):
            network_adress[y] = int(network_adress[y], 2)
        network_adress = ".".join(str(x) for x in network_adress)
        
        broadcast_adress = ip[0:mask] + bin(x)[2:].zfill(subnets_bits) + "1" * (32 - mask - subnets_bits)
        broadcast_adress = broadcast_adress[0:8] + "." + broadcast_adress[8:16] + "." + broadcast_adress[16:24] + "." + broadcast_adress[24:32]
        broadcast_adress = broadcast_adress.split(".")
        for y in range(len(broadcast_adress)):
            broadcast_adress[y] = int(broadcast_adress[y], 2)
        broadcast_adress = ".".join(str(x) for x in broadcast_adress)

        first_host = ip[0:mask] + bin(x)[2:].zfill(subnets_bits) + "0" * (32 - mask - subnets_bits)
        first_host = first_host[0:8] + "." + first_host[8:16] + "." + first_host[16:24] + "." + first_host[24:32]
        first_host = first_host.split(".")
        for y in range(len(first_host)):
            first_host[y] = int(first_host[y], 2)
            if y == 3:
                first_host[y] += 1
        first_host = ".".join(str(x) for x in first_host)
        
        last_host = ip[0:mask] + bin(x)[2:].zfill(subnets_bits) + "1" * (32 - mask - subnets_bits)
        last_host = last_host[0:8] + "." + last_host[8:16] + "." + last_host[16:24] + "." + last_host[24:32]
        last_host = last_host.split(".")
        for y in range(len(last_host)):
            last_host[y] = int(last_host[y], 2)
            if y == 3:
                last_host[y] -= 1
        last_host = ".".join(str(x) for x in last_host)
        
        output_file.write(f'Subnet {x+1} | Network adress: {network_adress} | Broadcast adress: {broadcast_adress} | Hosts: {first_host} - {last_host}\n')

print("Done! Check output.txt")
        
output_file.close()