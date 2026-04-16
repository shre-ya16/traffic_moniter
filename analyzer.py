ip_count = {}

with open("access.log", "r") as file:
    for line in file:
        ip = line.split()[0]

        if ip in ip_count:
            ip_count[ip] += 1
        else:
            ip_count[ip] = 1

print("\nTraffic Summary:\n")

for ip, count in ip_count.items():
    print(f"{ip} -> {count} requests")