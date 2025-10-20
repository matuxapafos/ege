# from ipaddress import ip_network
#
# net = ip_network('120-i31-231/e1e12-3-0123e',0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin[-8:].count('0') % 3 !=0:
#         count += 1
# pritn(count)

# from ipaddress import ip_network
#
# net = ip_network('192.168.31.80/255.255.255.240', 0)
# len = []
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     print(ip_bin)
#     print(ip_bin.count('1'))
#
# from ipaddress import ip_network
# for m in range(33):
#     net = ip_network(f'241.185.253.57/{m}',0)
#
#     if str(net.network_address) == '241.185.252.0':
#         print(32-m)


# from ipaddress import ip_network
#
# net = ip_network('112.154.133.208/255.255.252.0', 0)
# count = 0
# for ip in net:
#     ip_b = bin(int(ip))[2:].zfill(32)
#     if ip_b[:16].count('1') <= ip_b[-16:].count('0'):
#         if ip_b[-16:].count('0') % 2 != 0:
#             count += 1
# print(count)


# from ipaddress import ip_network
#
# for m in range(33):
#     net1 = ip_network(f'157.127.182.76/{m}',0)
#     net2 = ip_network(f'157.127.190.80/{m}', 0)
#
#     if net1.network_address != net2.network_address:
#         print(m)

# from ipaddress import ip_network
# count = 0
# for m in range(33):
#     net = ip_network(f'208.207.230.65/{m}', 0)
#
#     if str(net.network_address) == '208.207.224.0':
#         print(m)

# from ipaddress import ip_network
#
# for m in range(33):
#     net = ip_network(f'215.181.200.27/{m}', 0)
#
#     if str(net.network_address) == '215.181.192.0':
#         print(net.netmask)

# from ipaddress import ip_network
# count = 0
# net = ip_network('101.157.240.0/255.255.252.0', 0)
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#
#     if b[:16].count('1') > b[-16:].count('1'):
#         count += 1
# print(count)

# from ipaddress import ip_network
#
# net = ip_network('101.157.240.0/255.255.252.0', 0)
# count = 0
# for ip in net:
#     b = bin(int(ip))[2:].zfill(32)
#     if b[:16].count('1') > b[-16:].count('1'):
#             count += 1
# print(count)

# from ipaddress import ip_network
#
# for m in range(33):
#     net = ip_network(f'111.91.200.28/{m}', 0)
#     if str(net.network_address) == '111.91.192.0':
#         print(32-m)

# from ipaddress import *
#
# for m in range(33):
#     net = ip_network(f'158.116.11.146/{m}', 0)
#     if str(net.netmask) == '158.116.0.0':
#         print(m)

# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'215.181.200.27/{m}', 0)
#     if str(net.network_address) == '215.181.192.0':
#         print(net.netmask)

# from ipaddress import *
# net = ip_network('112.208.0.0/255.255.128.0', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1') % 11 == 0:
#         count += 1
# print(count)

# from ipaddress import *
# for m in range(33):
#     net = ip_network(f'20.24.110.42/{m}', 0)
#     if str(net.network_address) == '20.24.96.0':
#         print(net.netmask)

# from ipaddress import *
# net = ip_network('172.16.160.0/255.255.240.0', 0)
# c = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1') % 3 != 0:
#         c += 1
# print(c)


from ipaddress import *

for m in range(33):
    net1 = ip_network(f'118.187.59.255/{m}', 0)
    net2 = ip_network(f'118.187.65.115/{m}', 0)
    if net1.network_address != net2.network_address:
        print(m)