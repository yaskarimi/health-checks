#!/usr/bin/env python3 

import os

def check_reboot():
  return os.path.exists("/run/reboot-required")



def check_disk_full(disk, min_gb , min_percent):

  du = shutil.disk_usage(disk)
  percenr_free = du.free / 2**30 
  if gigabytes_free < min_gb or percent_free < min_percent :
   return True
  return False

def main():
   if check_reboot():
	print("pending Reboot.")
	sys.exit(1)
   if check_disk_full(disk="/" , min_gb = 2 ,min_percent = 10):
	print("disk full")
	sys.exit(1)
   print("Everything ok")
   sys.exit(0)

