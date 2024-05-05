Name: Arran Daly Student ID: 29669440D

===============================Application-Level Protocol=================================

The application level protocol for this project allows for effective communication between the client and the server, allowing users to upload and download files, and list the contents of the data directory. For this, I use the Transmission Control Protocol (TCP), which allows the delivery of bytes between applications.

Supported Operations and Message Formats

Uploading a file (put)
Downloading a file (get)
Listing contents of directory (list)

I used a request, send, receive format to accomplish these operations. My data is transferred in chunks of 1024 bytes, in json format. I used 3 classes in my common file, one for function used both by server and client, one acts a a client controller and another as the server controller. I also added a check to ensure that the file requested to be sent exists in the first place.

=======================================Design Decisions===================================

I opted for request, send receive format, all separated into various functions to make handling each process simpler. My data is transferred in chunks of 1024 bytes to prevent timing out while sending data

I originally decided to go with the method of converting the data into a string., however i couldnt seem to get this to work as intended, so i opted to convert using json file, which i then convert to a string. 

For error handling, i went with using a standardised function to display all errors, this function prints the ip, port and error message. This way i could also use this function to provide status updates when completing each process

I used classes in my common file to give myself a better visulaisation of how the client and server interact and what functions are external, however, this also allowed me to creat instances of my client and server classes in the client and server files, which made referencing the common functions simpler

=======================================Status Report===================================
My program currently is non functional, it cannot seem to find the file to transfer in the first place and i ran out of time to debug this issue, however, my program in theory should run if that issue were to be resolved.