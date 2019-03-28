"""A set of libraries that are useful to both the proxy and regular servers."""

# This code uses Python 2.7. These imports make the 2.7 code feel a lot closer
# to Python 3. (They're also good changes to the language!)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# THe Python socket API is based closely on the Berkeley sockets API which
# was originally written for the C programming language.
#
# https://en.wikipedia.org/wiki/Berkeley_sockets
#
# The API is more flexible than you need, and it does some quirky things to
# provide that flexibility. I recommend tutorials instead of complete
# descriptions because those can skip the archaic bits. (The API was released
# more than 35 years ago!)
import socket

import time

# Read this many bytes at a time of a command. Each socket holds a buffer of
# data that comes in. If the buffer fills up before you can read it then TCP
# will slow down transmission so you can keep up. We expect that most commands
# will be shorter than this.
COMMAND_BUFFER_SIZE = 256


def CreateServerSocket(port):
    """Creates a socket that listens on a specified port.

    Args:
    port: int from 0 to 2^16. Low numbered ports have defined purposes. Almost
        all predefined ports represent insecure protocols that have died out.
    Returns:
    An socket that implements TCP/IP.
    """

    #############################################
    #TODO: Implement CreateServerSocket Function
    #############################################
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(10)   # Listens for connections
    return server_socket

def ConnectClientToServer(server_sock):
    # Wait until a client connects and then get a socket that connects to the
    # client.
    

    #############################################
    #TODO: Implement CreateClientSocket Function
    #############################################
    return server_sock.accept()



def CreateClientSocket(server_addr, port):
    """Creates a socket that connects to a port on a server."""

    #############################################
    #TODO: Implement CreateClientSocket Function
    #############################################
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((server_addr, port))
    return socket

def ReadCommand(sock):
    """Read a single command from a socket. The command must end in newline."""

    #############################################
    #TODO: Implement ReadCommand Function
    #############################################
    command_line = sock.recv(COMMAND_BUFFER_SIZE).decode()
    return command_line


def ParseCommand(command):
    """Parses a command and returns the command name, first arg, and remainder.

    All commands are of the form:
      COMMAND arg1 remaining text is called remainder
    Spaces separate the sections, but the remainder can contain additional spaces.
    The returned values are strings if the values are present or `None`. Trailing
    whitespace is removed.

    Args:
    command: string command.
    Returns:
    command, arg1, remainder. Each of these can be None.
    """
    args = command.strip().split(' ')
    command = None
    if args:
        command = args[0]
    arg1 = None
    if len(args) > 1:
        arg1 = args[1]
    remainder = None
    if len(args) > 2:
        remainder = ' '.join(args[2:])
    return command, arg1, remainder

class TimeStore(object):
    #extra credit
    def __init__(self, value):
        self.value = value;
        self.timestamp = time.time();
        return

class KeyValueStore(object):
    """A dictionary of strings keyed by strings.

    The values can time out once they get sufficiently old. Otherwise, this
    acts much like a dictionary.
    """
  
    def __init__(self):
        ###########################################
        #TODO: Implement __init__ Function
        ###########################################
        self.storage = {}
        self.has_been_set = False
        return

    def GetValue(self, key, max_age_in_sec=None):
        """Gets a cached value or `None`.

        Values older than `max_age_in_sec` seconds are not returned.

        Args:
          key: string. The name of the key to get.
          max_age_in_sec: float. Maximum time since the value was placed in the
            KeyValueStore. If not specified then values do not time out.
        Returns:
          None or the value.
        """
        # Check if we've ever put something in the cache.

        ###########################################
        #TODO: Implement GetValue Function
        ###########################################
#        value, stored_time = self.storage.get(key, (None, None))
#        if value and (not max_age_in_sec or (time.time() - stored_time) <= max_age_in_sec):
#            return value
#        else:
#            return None
#extra credit implementation included
        if self.has_been_set:
            if max_age_in_sec is None:
                if key in self.storage :
                    return (self.storage[key]).value
                else:
                    return None
            else:
                current_time = time.time()
                if key in self.storage.keys():
                    pair = self.storage[key]
                    if (current_time - pair.timestamp) <= max_age_in_sec:
                        return (self.storage[key]).value
                    else:
                        return None
                else:
                    return None
        else:
            return None

    def StoreValue(self, key, value):
        """Stores a value under a specific key.

        Args:
          key: string. The name of the value to store.
          value: string. A value to store.
        """

        ###########################################
        #TODO: Implement StoreValue Function
        ###########################################
#        self.storage[key] = (value, time.time())
        if not(key is None) and not(value is None):
            self.storage[key] = TimeStore(value)
            self.has_been_set = True
            return 0
        else:
            return 1


    def Keys(self):
        """Returns a list of all keys in the datastore."""

        ###########################################
        #TODO: Implement Keys Function
        ###########################################
        return list(self.storage.keys())
