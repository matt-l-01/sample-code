# CS3700 - Project 2 - Matthew Love
## High-level Approach
A basic FTP client to connect to an FTP server and conduct operations based on the given commands: ls, mkdir, rm, rmdir, cp, and mv. These commands work parallel to their linux equivalents.

My program implements the required features through the data and control channels that are opened depending on the context of the operation to conduct. After opening the control channel, logging in, and setting the correct settings, the program is ready to process the command. It reads the parsed argument for the operation and constructs a command to send to the server depending on the necessary arguments the server requests.

This client supports uploading and downloading of files from the client to server and vice versa. The program will also delete the file locally when using the mv command to move a file from local to the server.

## Challenges
In terms of challenges, my main challenge was handling the recevied data from the data channel without error. After debugging and testing, I was able to do so correctly.

## How I Tested
I tested the program locally on my machine by connecting to the 3700 network FTP server (ftp.3700.network). I ran the commands through my command line and viewed output there as well. I did this with both when uploading/downloading files and regular commands to receive data. I also used multiple debugging print statements which are no longer in the final version. The printing of the received messages from the control channel also aided in testing and debugging.