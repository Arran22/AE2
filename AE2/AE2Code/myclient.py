import socket
import sys
from common import socket_to_screen, keyboard_to_socket

def check_instruction_valid(cli_sock, srv_addr):
	errors = []
	instruction = sys.argv[3]

	if instruction == "list":
		return (instruction, None)	
	check_file_exists(instruction, sli_sock, srv_addr)

def check_valid_file(instruction, cli_sock, errors, srv_addr):

	filename = sys.argv[4]

	
def check_file_exists(side, filename):
	if side == "client":
		path = "client_data"
	else:
		path = "server_data"

	files = [f for f in listdir(path) if isfile(join(path, f))]
	if filename in files:
		return True, path+"/"+filename
	else:
		return false, path+"/"+filename


def main():
	# Create the socket with which we will connect to the server
	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# The server's address is a tuple, comprising the server's IP address or hostname, and port number
	srv_addr = (sys.argv[1], int(sys.argv[2])) # sys.argv[x] is the x'th argument on the command line
	operation = sys.argv[3]
	filename = sys.argv[4]

	# Convert to string, to be used shortly
	srv_addr_str = str(srv_addr)

	client = controller_client(cli_sock, sys.argv[1], sys.argv[2])

	""" 
	Enclose the connect() call in a try-except block to catch
	exceptions related to invalid/missing command-line arguments, 
	port number out of range, etc. Ideally, these errors should 
	have been handled separately.
	"""
	try:
		client.status_report("\nEstablishing connection to " + srv_addr_str + "...")
		
		cli_sock.connect(srv_addr)

		client.status_report("Connection established.")

		try:
			if operation == "list":
				client.request_list()
				client.recieve_list(client.fetch_data())

				timeout.sleep(client.connection_weakness)
			
			elif operation == 'get':
				client.request_file(filename)
				client.receive_file(client.fetch_data())

				timeout.sleep(client.connection_weakness)
			
			elif operation == "put":
				client.send_file(filename)

			else:
				client.status_report("Error: Invalid operation...")
				# Exit with a non zero value, to indicate an error condition
				exit(1)
	
		except Exception as e:
			# Print the exception message
			client.status_report("Error: ", e)
		

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
