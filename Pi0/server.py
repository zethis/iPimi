import socketserver
import subprocess
from subprocess import Popen, PIPE, run

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        key = self.data.decode("utf-8")
        print(key)
        subprocess.getoutput("echo '{}' | sendkeys /dev/hidg0 keyboard".format(key))
        #p = run(['/usr/bin/sendkeys', '/dev/hidg0', 'keyboard'], input="b", text=True)
        #p = Popen(['/usr/bin/sendkeys', '/dev/hidg0', 'keyboard'], shell=True, stdin=PIPE).stdin


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 10000

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


