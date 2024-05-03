import sys
import socket
import os
import base64

class common():

	def status_report(self, message):
		print(f'({self.ip}: {self.port}) - {message}', flush=True)

	def __init__(self, socket, type, ip, port):
		self.port = port
		self.ip = ip

		self.status_report("Initialising common - " + type + "...")

		self.client_or_server = {
			'client': 'client_data',
			'server': 'server_data'
		}

		self.connection_weakness = 4.0
		self.type = type
		self.socket = socket
		self.socket.settimeout(self.allowance)

	def check_file_exists(self, filename):
		if os.pathy.exists(filename):
			self.status_report("File path validated...")
			base_filename, file_extension = os.path.splitext(filename)
			index=1
			while os.path.exists(filename):
				self.status_report("Indexing files...")
				filename = f"{base_filename}({i}){file_extension}"
				index +=1
		self.status_report(f"Filename saved: {base_filename}")
		return filename

	def grab_data(self):
		self.status_report("Grabbing data...")
		
		try:
			while True:
				data = self.socket.recv()
				if not data:
					self.status_report("No more data to receive")
					break
				self.status_report(str(len(data)) + " bytes of data received")
		except socket.timeout:
			self.status_report("Timed out: No more data to receive")
		
		return data

	def send_data(self, action):
		try:
			self.status_report("Sending data " + action)
			self.socket.sendall(data.encode('utf-8'))
		except socket.error as e:
			self.status_report(f"Error: Socket Error: {e}")
		except Exception as e:
			self.status_report(f"Error: {e}")

	def send_file(self, data):
		self.status_report("Sending file...")

		try:
			with open(os.path.join(self.client_or_server[self.type], filename), 'rb') as d:
				filedata = d.read()
		except:
			self.status_report(f"Error: File cannot be found: {filename}")
			return

		action = send_file
		filedata = base64.b64encode(filedata).decode()

		self.send_data(action, filename, filedata)
	
	def receive_file(self, action, filename, filedata):
		self.status_report("Receiving file...")
	
		filename = os.path.join(self.client_or_server[self.typeb], filename)
		file_content = base64.b64decode(filedata)

		filename = self.check_file_exists(filename)

		with open(filename, 'wb') as file:
			file.write(file_content)







# def socket_to_screen(socket, sock_addr):
# 	"""Reads data from a passed socket and prints it on screen.

# 	Returns either when a newline character is found in the stream or the connection is closed.
#         The return value is the total number of bytes received through the socket.
# 	The second argument is prepended to the printed data to indicate the sender.
# 	"""
# 	print(sock_addr + ": ", end="", flush=True) # Use end="" to avoid adding a newline after the communicating partner's info, flush=True to force-print the info

# 	data = bytearray(1)
# 	bytes_read = 0

# 	"""
# 	 Loop for as long as data is received (0-length data means the connection was closed by
# 	 the client), and newline is not in the data (newline means the complete input from the
# 	 other side was processed, as the assumption is that the client will send one line at
# 	 a time).
# 	"""
# 	while len(data) > 0 and "\n" not in data.decode():
# 		"""
# 		 Read up to 4096 bytes at a time; remember, TCP will return as much as there is
# 		 available to be delivered to the application, up to the user-defined maximum,
# 		 so it could as well be only a handful of bytes. This is the reason why we do
# 		 this in a loop; there is no guarantee that the line sent by the other side
# 		 will be delivered in one recv() call.
# 		"""
# 		data = socket.recv(4096)

# 		print(data.decode(), end="") # Use end="" to avoid adding a newline per print() call
# 		bytes_read += len(data)
# 	return bytes_read

# def keyboard_to_socket(socket):
# 	"""Reads data from keyboard and sends it to the passed socket.
	
# 	Returns number of bytes sent, or 0 to indicate the user entered "EXIT"
# 	"""
# 	print("You: ", end="", flush=True) # Use end="" to avoid adding a newline after the prompt, flush=True to force-print the prompt

# 	# Read a full line from the keyboard. The returned string will include the terminating newline character.
# 	user_input = sys.stdin.readline()
# 	if user_input == "EXIT\n": # The user requested that the communication is terminated.
# 		return 0

# 	# Send the whole line through the socket; remember, TCP provides no guarantee that it will be delivered in one go.
# 	bytes_sent = socket.sendall(str.encode(user_input))
# 	return bytes_sent

