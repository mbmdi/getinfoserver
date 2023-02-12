
#pip install ipwhois
#pip install whois
#pip install socket
from ipwhois import IPWhois
import socket
domain=input("please eneter Domain : ")
ip=socket.gethostbyname(domain)
print(f"""
      --------------
       ip:{ip}
      --------------
      """)
info = IPWhois(ip)
info=info.lookup_whois()
print("""
      -------
      server information:
      -------
      """)
print(info)


#https://github.com/mbmdi