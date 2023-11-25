#!/usr/bin/env python3

import sys
import json
import ipaddress
import urllib.request

def is_valid_ip(ip):
  try:
    ipaddress.ip_address(ip)
    return True
  except ValueError:
    return False

if len(sys.argv) > 1:
  if sys.argv[1].strip() == "":
    print("No IP address given.")
    exit()
  else:
    ip=sys.argv[1]
    if is_valid_ip(ip):
      url = ("http://ip-api.com/json/")
      response = urllib.request.urlopen(url + ip)
      data = response.read()
      values = json.loads(data)
      print("IP       : " + values['query'])
      print("Status   : " + values['status'])
      print("Region   : " + values['regionName'])
      print("Country  : " + values['country'])
      print("City     : " + values['city'])
      print("ISP      : " + values['isp'])
      print("Lat,Lon  : " + str(values['lat']) + "," + str(values['lon']))
      print("Zipcode  : " + values['zip'])
      print("TimeZone : " + values['timezone'])
      print("AS       : " + values['as'])
    else:
      print("Not a valid IP address.")
      exit()
else:
  print("No arguments were passed.")
  exit()
