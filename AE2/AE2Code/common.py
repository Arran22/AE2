import sys
import socket
import os
import base64
import json

class common():

	def status_report(self, message):
		print(f'({self.ip}: {self.port}) - {message}', flush=True)

	def __init__(self, socket, type, ip, port):
		self.port = port
		self.ip = ip

		self.status_report(f"Initialising common - {type}...")

		self.client_or_server = {
			'client': 'client_data',
			'server': 'server_data'
		}

		self.connection_weakness = 4.0
		self.type = type
		self.socket = socket
		self.socket.settimeout(self.connection_weakness)

	def check_file_exists(self, filename):
		if os.path.exists(filename):
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
		
		data = b""
		try:
			while True:
				data_section = self.socket.recv(1024)
				if not data_section:
					self.status_report("No more data to receive")
					break
				data +=data_section
				self.status_report(f"{str(len(data_section))} bytes of data received")
		except socket.timeout:
			self.status_report("Timed out: No more data to receive")
		
		json_data = data.decode()
		data = json.loads(json_data)
		return data

	def send_data(self, transfer_data):
		try:
			data = json.dumps(transfer_data)
			self.status_report(f"Sending data " + transfer_data["action"])
			self.socket.sendall((data).encode('utf-8'))
			self.socket.sendall(b"")
		except json.decoder.JSONDecodeError:
			self.status_report(f"Invalid data form JSON: {data}")
		except socket.error as e:
			self.status_report(f"Error: Socket Error: {e}")
		except Exception as e:
			self.status_report(f"Error: {e}")

	def send_file(self, filename):
		self.status_report("Sending file...")

		transfer_data = {}

		try:
			with open(os.path.join(self.client_or_server[self.type], filename), 'rb') as d:
				filedata = d.read()
		except:
			self.status_report(f"Error: File cannot be found: {filename}")
			return
		
		transfer_data = {
			"action" : "send_file",
			"filename" : filename,
			"filedata" : base64.b64encode(filedata).decode()
			}
		

		self.send_data(transfer_data)
	
	def receive_file(self, transfer_data):
		self.status_report("Receiving file...")

		try:
			filename = os.path.join(self.client_or_server[self.type], filename)
			file_content = base64.b64decode(filedata)
		except json.decoder.JSONDecodeError:
			self.status_report(f"Invalid data in JSON: " + transfer_data["filedata"])

		filename = self.check_file_exists(filename)

		with open(filename, 'wb') as file:
			file.write(file_content)

class client(common):

	def __init__(self, socket, ip, port):
		super().__init__(socket, 'client', ip, port)

	def request_list(self):
		self.status_report("Requesting list...")

		transfer_data = {
		"action" : "get_list"
		}

		self.send_data(transfer_data)
	
	def receive_list(self, files):
		self.status_report("Receiving list...")

		self.status_report("Files stored in server:")
		for file in files:
			self.status_report(file)

	def request_file(self, filename):
		self.status_report("Requesting file...")

		transfer_data = {
		"action" : 'get_file',
		"filename" : filename
		}

		self.send_data(transfer_data)

class server_controller(common):

	def __init__(self, socket, ip, port):
		super().__init__(socket, 'server', ip, port)

	def send_list(self):
		self.status_report("Sending list...")

		transfer_data = {
		"action" : "send_list",
		"files" : os.listdir(self.client_or_server[self.type])
		}

		self.send_data(transfer_data)

