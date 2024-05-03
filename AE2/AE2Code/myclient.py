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

def send_request(socket):
	

def main():
	# Create the socket with which we will connect to the server
	cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# The server's address is a tuple, comprising the server's IP address or hostname, and port number
	srv_addr = (sys.argv[1], int(sys.argv[2])) # sys.argv[x] is the x'th argument on the command line

	# Convert to string, to be used shortly
	srv_addr_str = str(srv_addr)

	""" 
	Enclose the connect() call in a try-except block to catch
	exceptions related to invalid/missing command-line arguments, 
	port number out of range, etc. Ideally, these errors should 
	have been handled separately.
	"""
	try:
		print("Connecting to " + srv_addr_str + "... ")

		"""
		Connect our socket to the server. This will actually bind our socket to
		a port on our side; the port number will most probably be in the
		ephemeral port number range and may or may not be chosen at random
		(depends on the OS). The connect() call will initiate TCP's 3-way
		handshake procedure. On successful return, said procedure will have
		finished successfully, and a TCP connection to the server will have been
		established.
		"""
		cli_sock.connect(srv_addr)
		
		print("Connected. Now chatting...")
	except Exception as e:
		# Print the exception message
		print(e)
		# Exit with a non-zero value, to indicate an error condition
		exit(1)

	"""
	Surround the following code in a try-except block to account for
	socket errors as well as errors related to user input. Ideally
	these error conditions should be handled separately.
	"""
	try:
		# checks the input instruction valid
		instr, filename = check_instruction_valid(cli_sock, srv_addr)

		#calls the function related to the instruciton
		functions = 

	finally:
		"""
		If an error occurs or the server closes the connection, call close() on the
		connected socket to release the resources allocated to it by the OS.
		"""
		cli_sock.close()

	# Exit with a zero value, to indicate success
	exit(0)
