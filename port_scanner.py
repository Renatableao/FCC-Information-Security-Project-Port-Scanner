import socket
import ipaddress
from common_ports import *
import re

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    
    try: 
      ip = socket.gethostbyname(target)
      for port in range(port_range[0], port_range[1] + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        # returns an error indicator
        result = s.connect_ex((ip,port))
        if result ==0:
            open_ports.append(port)
        s.close()

    except KeyboardInterrupt:
        return "Exiting Program !!!!"
    except socket.gaierror:
        if re.search('[a-zA-Z]', target):
          return "Error: Invalid hostname"
        return "Error: Invalid IP address"
    except socket.error:
        return "Error: Invalid IP address"


    if verbose:
      
      try:
        host = socket.gethostbyaddr(ip)[0]
      except socket.error:
        host = None
        
      if host:
        ip = "{0} ({1})".format(host, ip)

      display = "Open ports for {0}\nPORT     SERVICE\n".format(ip)
      
      for port in open_ports:
        service = ports_and_services[port]
        display += "{:<8} {}".format(port, service)
        if open_ports.index(port) != len(open_ports) -1:
          display += "\n"
      
      return display

    return(open_ports)