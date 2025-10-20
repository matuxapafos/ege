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


# from ipaddress import *
#
# for m in range(33):
#     net1 = ip_network(f'118.187.59.255/{m}', 0)
#     net2 = ip_network(f'118.187.65.115/{m}', 0)
#     if net1.network_address != net2.network_address:
#         print(m)


## ПОДБОРКА

# 1 Задача
# from ipaddress import *
# list = []
# for m in range(33):
#     net1 = ip_network(f'121.171.5.70/{m}', 0)
#     net2 = ip_network(f'121.171.5.107/{m}', 0)
#     if net1==net2:
#         list.append(net1.num_addresses)
# print(min(list))

# 2 Задача
# from ipaddress import *
#
# for m in range(33):
#     net = ip_network(f'20.24.110.42/{m}', 0)
#     if str(net.network_address) == '20.24.96.0':
#         print(m)

# 3 Задача
# from ipaddress import *
#
# for m in range(33):
#     net = ip_network(f'174.213.57.95/{m}', 0)
#     if str(net.network_address) == '174.213.0.0':
#         if m % 2 == 0:
#             print(m)

# 4 Задача

# from ipaddress import *
#
# for m in range(33):
#     net1 = ip_network(f'61.58.73.42/{m}', 0)
#     net2 = ip_network(f'61.58.75.136/{m}', 0)
#     if net1.network_address == net2.network_address:
#         # print(m)
#         count = 0
#         if m == 22:
#             for ip in net1.hosts():
#
#                 ip_bin = bin(int(ip))[2:].zfill(32)
#                 if ip_bin.count('1') % 2 == 1:
#                     count += 1
#         print(count)

# 5 задача
# from ipaddress import *
# for a in range(256):
#     c = 0
#     k = 0
#     net = ip_network(f'248.112.{a}.35/255.255.255.240', 0)
#     for ip in net:
#         c += 1
#         ip_bin = bin(int(ip))[2:].zfill(32)
#         if ip_bin[0:16].count('0') <= ip_bin[16:32].count('0'):
#             k += 1
#     if c == k:
#         print(a)

# 6 задача
# from ipaddress import *
#
# for m in range(33):
#     net = ip_network(f'117.73.208.27/{m}', 0)
#     if str(net.network_address) == '117.73.192.0':
#         print(32-m)

#7 задача

# from ipaddress import *
# net = ip_network('171.128.0.0/255.128.0.0', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin[0:16].count('1') < ip_bin[16:32].count('1'):
#         count += 1
# print(count)


# 8 задача
# from ipaddress import *
#
# net = ip_network('73.148.145.65/255.224.0.0', 0)
#
# for ip in net.hosts():
#     print(ip)

# 9 задача

# from ipaddress import *
#
# for m in range(33):
#     net1 = ip_network(f'151.172.115.121/{m}', 0)
#     net2 = ip_network(f'151.172.115.156/{m}', 0)
#     if net1 != net2:
#         print(m)

# 10 задача

# from ipaddress import *
#
# net = ip_network('212.192.32.96/255.255.255.224', 0)
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if '111' not in ip_bin[-8:] and '000' not in ip_bin[-8:]:
#         count += 1
# print(count)

# 11 задача

# from ipaddress import *
#
# net = ip_network('192.168.160.0/255.255.224.0', 0)
#
# count = 0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1') == 19:
#         count+=1
# print(count)


# 12 задача

# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'101.96.170.244/{m}', 0)
#     net2 = ip_network(f'101.96.126.212/{m}', 0)
#     if net1 != net2:
#         print(32-m)

# 13 задача

# from ipaddress import *
# net = ip_network('172.16.168.0/255.255.248.0', 0 )
# c =0
# for ip in net:
#     ip_bin = bin(int(ip))[2:].zfill(32)
#     if ip_bin.count('1') % 5 != 0:
#         c +=1
# print(c)


# 14 задача

# from ipaddress import *
# for m in range(33):
#     net1 = ip_network(f'134.181.67.112/{m}', 0)
#     net2 = ip_network(f'134.181.94.117/{m}', 0)
#     if net1.network_address == net2.network_address:
#         print(net1.netmask)


# 15 задача

# from ipaddress import *
#
# net = ip_network('102.162.200.51/255.255.255.0', 0)
#
# for ip in net.hosts():
#     print(ip)