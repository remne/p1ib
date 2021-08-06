import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

UDP_PORT = 8888
UDP_IP = get_ip_address()

print("")
print("Open url http://p1ib.local/ and go to the settings page. ")
print("Enable \"Remote Debug Log\". Fill in IP-field with {ip} and port-field {port}".format(ip=UDP_IP, port=UDP_PORT))
print("")
print("You might need to disable your firewall on your computer to be able to receive the udp packages sent by the p1ib device.")
print("")
print("")
print("When it is working, then there should come up lots of text here. Wait at least 30 seconds, then press CTRL+C to quit.")
print("You will find a filename 'p1ib.log' in the same directory as this file with the logging results.")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

line = 0

try:
    f = open("p1ib.log", "a")
    while True:
        data, addr = sock.recvfrom(1024)
        s = "{:8d}:{}".format(line, data.decode("utf-8"))
        print(s, end='')
        f.write(s)
        f.flush()
        line += 1
except KeyboardInterrupt:
    f.close()
