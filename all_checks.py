#!/usr/bin/env python3 

import os
import sys 


def check_reboot():
  return os.path.exists("/run/reboot-required")



def check_disk_full(disk, min_gb , min_percent):

  du = shutil.disk_usage(disk)
  percent_free = 100 * du.free / du.total
  gigabytes_free = du.free / 2**30 
  if gigabytes_free < min_gb or percent_free < min_percent :
   return True
  return False

def check_root_full():
  return check_disk_full(disk = "/" , min_gb = 1 , min_percent =10)


def main():
   if check_reboot():
     print("pending Reboot.")
     sys.exit(1)
   if check_root_full():
     print("root partition full")
     sys.exit(1)
   print("Everything ok")
   sys.exit(0)

main()
