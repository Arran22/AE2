import socket
import sys
from common import server_controller

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen(5)
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)

print("Server listening...")

# Loop forever (or at least for as long as no fatal errors occur)
while True:

	try:
		print("Waiting for new client... ")
		
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr) # Translate the client address to a string (to be used shortly)
		hostname = 'localhost'
		server = server_controller(cli_sock, socket.gethostbyname(hostname), sys.argv[1])

		print(f"Client " + cli_addr_str +  "connected...")
		
		transfer_data = server.grab_data()

		# Ensure data is not null
		if transfer_data is not None:
			
			# check for action type
			if transfer_data["action"] == "get_list":
				print("Action: get list")
				server.get_list()
			elif transfer_data["action"] == "send_file":
				print("Action: send file")
				print(filename)
			elif transfer_data["action"] == "get_file":
				print("Action: get file")
				server.send_file(transfer_data['filename'])
			else:
				print(f"Server side error occured performing: {transfer_data['action']}")
		else:
			print("No data received from client")

	finally:
		print("Operation done, closing connection...")
		cli_sock.close()