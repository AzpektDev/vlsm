# ipwm = input("Ip with mask: ")
print("Enter ip adress with mask (e.g. 192.168.10.0/27)")
ipwm = input()
ip, mask = ipwm.split("/")

mask = int(mask)

if mask < 8:
    print("Invalid mask (must be 8 or greather)")
    exit(-1)

ip = ip.split(".")
for x in range(len(ip)):
    ip[x] = int(ip[x])

# for x in range(len(ip)):
#     ip[x] = bin(ip[x])[2:].zfill(8)

# ip = ".".join(ip)

bityzmienne = 32 - mask
bitynzmienne = 32 - bityzmienne
oktetystale = int(bitynzmienne / 8)
oktetyzmienne = int(bityzmienne / 8)

numer_podsieci_s = 0
numer_podsieci_f = 0
if mask >= 9 and mask <= 15:
    siec = mask - 8
    ips = 32 - mask
    print(f'{ip[0]}.*.*.*/{mask}')
    for x in range(2**siec):
        numer_podsieci_f = 2**(ips - 16) * (x + 1)
        print(f'#{x + 1} | Network adress: {ip[0]}.{numer_podsieci_s}.0.0 Broadcast: {ip[0]}.{numer_podsieci_f - 1}.255.255 Usable host range: {ip[0]}.{numer_podsieci_s}.0.1 - {ip[0]}.{numer_podsieci_f - 1}.255.254')
        numer_podsieci_s = numer_podsieci_f
elif mask >= 17 and mask <= 23:
    siec = mask - 16
    ips = 32 - mask
    print(f'{ip[0]}.{ip[1]}.*.*/{mask}')
    for x in range(2**siec):
        numer_podsieci_f = 2**(ips - 8) * (x + 1)
        print(f'#{x + 1} | Network adress: {ip[0]}.{ip[1]}.{numer_podsieci_s}.0 Broadcast: {ip[0]}.{ip[1]}.{numer_podsieci_f - 1}.255 Usable host range: {ip[0]}.{ip[1]}.{numer_podsieci_s}.0 - {ip[0]}.{ip[1]}.{numer_podsieci_f - 1}.254')
        numer_podsieci_s = numer_podsieci_f
elif mask >= 25 and mask <= 31:
    siec = mask - 24
    ips = 32 - mask
    print(f'{ip[0]}.{ip[1]}.{ip[2]}.*/{mask}')
    for x in range(2**siec):
        numer_podsieci_f = 2**ips * (x + 1)
        print(f'#{x + 1} | Network adress: {ip[0]}.{ip[1]}.{ip[2]}.{numer_podsieci_s} Broadcast: {ip[0]}.{ip[1]}.{ip[2]}.{numer_podsieci_f - 1} Usable host range: {ip[0]}.{ip[1]}.{ip[2]}.{numer_podsieci_s + 1} - {ip[0]}.{ip[1]}.{ip[2]}.{numer_podsieci_f - 2}')
        numer_podsieci_s = numer_podsieci_f
elif mask == 8:
    siec = 1
    ips = 32 - mask
    print(f'#1 | Network adress: {ip[0]}.0.0.0 Broadcast: {ip[0]}.255.255.255 Usable host range: {ip[0]}.0.0.1 - {ip[0]}.255.255.254')
elif mask == 16:
    siec = 1
    ips = 32 - mask
    print(f'#1 | Network adress: {ip[0]}.{ip[1]}.0.0 Broadcast: {ip[0]}.{ip[1]}.255.255 Usable host range: {ip[0]}.{ip[1]}.0.1 - {ip[0]}.{ip[1]}.255.254')
elif mask == 24:
    siec = 1
    ips = 32 - mask
    print(f'#1 | Network adress: {ip[0]}.{ip[1]}.{ip[2]}.0 Broadcast: {ip[0]}.{ip[1]}.{ip[2]}.255 Usable host range: {ip[0]}.{ip[1]}.{ip[2]}.1 - {ip[0]}.{ip[1]}.{ip[2]}.254')
elif mask == 32:
    siec = 1
    ips = 1
    print(f'#1 | Network adress: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} Broadcast: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]} Usable host range: N/A')

print(f'Network count: {2**siec} IP\'s: {2**ips} Usable hosts: {2**ips - 2}')
    
#TODO: eng