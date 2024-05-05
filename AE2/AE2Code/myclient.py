import socket
import sys
import time
from common import client

# Create the socket with which we will connect to the server
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server's address is a tuple, comprising the server's IP address or hostname, and port number
srv_addr = (sys.argv[1], int(sys.argv[2])) # sys.argv[x] is the x'th argument on the command line
operation = sys.argv[3]
filename = sys.argv[4]

# Convert to string, to be used shortly
srv_addr_str = str(srv_addr)

client = client(cli_sock, sys.argv[1], sys.argv[2])

try:
	client.status_report(f"\nEstablishing connection to {srv_addr_str}...")
		
	cli_sock.connect(srv_addr)

	client.status_report("Connection established.")

	try:
		if operation == "list":
			client.request_list()
			client.recieve_list(client.grab_data())

			time.sleep(client.connection_weakness)
			
		elif operation == 'get':
			filename = sys.argv[4]
			client.request_file(filename)

			time.sleep(client.connection_weakness)

			client.receive_file(client.grab_data())	
			
		elif operation == "put":
			client.send_file(filename)

		else:
			client.status_report("Error: Invalid operation...")
			# Exit with a non zero value, to indicate an error condition
			exit(1)
	
	except Exception as e:
		# Print the exception message
		client.status_report(f"Error: {e}")
		

	finally:
		"""
		If an error occurs or the server closes the connection, call close() on the
		connected socket to release the resources allocated to it by the OS.
		"""
		cli_sock.close()

except Exception as e:
	# Print the exception message
	client.status_report(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)

exit()
