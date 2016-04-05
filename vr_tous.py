#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from bubendorff import Bubendorff

def usage():
    print("Error : bad parameters!")
    print("Usage : {0} [open|close]".format(sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    if sys.argv[1] not in ['open', 'close']:
        usage()

    vr1 = Bubendorff(22, 18, 22, 20)  
    vr2 = Bubendorff(26, 24, 22, 20)  
    if sys.argv[1] == "open":
        vr1.open()
        vr2.open()
    else:
        vr1.close()
        vr2.close()
    print("1")
