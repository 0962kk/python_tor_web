import socks, socket
from urllib.request import urlopen


url = "http://whoer.net"
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150, True)
socket.socket = socks.socksocket
socket.create_connection = create_connection

contents = urlopen(url).read()
print(contents)
