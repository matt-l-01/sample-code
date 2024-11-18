# FTP client
#
# This program is a simple FTP client that can be used to
# download files from an FTP server.  It is not a complete
# implementation of the FTP protocol, but it does support
# the basic commands needed to download files.
#
# Usage: python3 3700ftp.py <server> <port> <username> <password> <command> <file>
#
# The <server> argument is the hostname or IP address of the
# FTP server.  The <port> argument is the port number of the
# FTP server.  The <username> and <password> arguments are
# the username and password to use when logging in to the
# FTP server.  The <command> argument is the FTP command to
# execute.  The <file> argument is the name of the file to
# download from the FTP server.
#
# The only supported command is "get".  The get command
# downloads the specified file from the FTP server and
# saves it to the local disk.
#
# The program will print out the response from the FTP
# server after each command is sent.
#
# The program will print out the contents of the file
# after it is downloaded.
#
# The program will print out an error message if the
# server returns an error code.
#
# The program will print out an error message if the
# command line arguments are invalid.
#
# The program will print out an error message if the
# specified file cannot be opened for writing.
#
# The program will print out an error message if the
# specified file cannot be read from the FTP server.
#
# The program will print out an error message if the
# specified file cannot be written to the local disk.
#
# The program will print out an error message if the
# connection to the FTP server cannot be established.
#
# The program will print out an error message if the
# connection to the FTP server is lost.
#
# The program will print out an error message if the
# connection to the FTP server is closed.
#
# The program will print out an error message if the
# connection to the FTP server is reset.
#
# The program will print out an error message if the
# connection to the FTP server times out.
#
# The program will print out an error message if the
# connection to the FTP server is refused.
#
# The program will print out an error message if the
# connection to the FTP server is aborted.
#
# The program will print out an error message if the
# connection to the FTP server is interrupted.
#
# The program will print out an error message if the
# connection to the FTP server is not connected.
