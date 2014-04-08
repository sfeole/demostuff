#!/usr/bin/env python3

import sys
import subprocess
import argparse
 
def get_net_info(interface):
    myaddress = subprocess.getoutput("/sbin/ifconfig %s" % interface)\
                .split("\n")[1].split()[1][5:]
    if myaddress == "CAST":
        print ("Please Confirm that your Network Device is Configured")
        sys.exit()
    else:
        return (myaddress)
 
def main():
#Parser Code
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface',
                        help="Select the interface you wish to use",
                        choices=['eth0', 'wlan0'],
                        required=True)
    args = parser.parse_args()
 
    print (get_net_info("%s" % args.interface))
 
if __name__ == "__main__":
    sys.exit(main())
