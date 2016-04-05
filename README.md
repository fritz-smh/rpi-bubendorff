Purpose
=======

This repository will help you to control some Bubendorff shutting rollers with a raspberry.

![Alt text](soldering_01.jpg?raw=true "Yi camera")

![Alt text](full.jpg?raw=true "Yi camera")

Prerequisites
=============

    # pip install RPi.GPIO

Install
=======

* Clone this repository
* Create a script vr_xxxxx.py for your rolling shutter and set the appropriate pin configuration and times in seconds.
* Test it


Usage with Domogik
==================

To use it with www.domogik.org, follow the below instructions.

In this release, the librabry can be only called thanks to a dedicated python script called over ssh.

First, if you already didn't do it, generate on the Domogik server, the ssh keys. Example :

    $ ssh-keygen 
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/domogik/.ssh/id_rsa): 
    Created directory '/home/domogik/.ssh'.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/domogik/.ssh/id_rsa.
    Your public key has been saved in /home/domogik/.ssh/id_rsa.pub.
    The key fingerprint is:
    aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa domogik@domogikserver
    The key's randomart image is:
    +---[RSA 2048]----+
    |         ++S+o.  |
    |        .o+ o    |
    |  S+o.    .O +   |
    |         .. B =  |
    |        S .  = = |
    |  S+o.   o    = .|
    |  B     .      + |
    |       S+o.   E  |
    | B               |
    +-----------------+

Then, copy the keys on the rpi:

    $ ssh-copy-id pi@192.168.1.180
    The authenticity of host '192.168.1.180 (192.168.1.180)' can't be established.
    ECDSA key fingerprint is aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa:aa.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '192.168.1.180' (ECDSA) to the list of known hosts.
    pi@192.168.1.180's password: 
    Now try logging into the machine, with "ssh 'pi@192.168.1.180'", and check in:
    
      ~/.ssh/authorized_keys
    
    to make sure we haven't added extra keys that you weren't expecting.
    
Create a script to manage your rolling shutters. Example : 

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
    
        # 22 => close (time = 20s)
        # 18 => open (time = 22s)
        vr1 = Bubendorff(22, 18, 22, 20)  
        if sys.argv[1] == "open":
            vr1.open()
        else:
            vr1.close()
        print("1")

You can check the sample files:

* vr_cuisine.py
* vr_salle_a_manger.py
* vr_tous

Then install on Domogik the **plugin script** from : https://github.com/vdomos/domogik-plugin-script

Create a device **Script OnOff** and set the parameters (change login, password, script path and name) :

* command : sshpass -p "raspberry" ssh pi@192.168.1.180 "python /home/pi/git/rpi-bubendorff/vr_cuisine.py open"
* command0 : sshpass -p "raspberry" ssh pi@192.168.1.180 "python /home/pi/git/rpi-bubendorff/vr_cuisine.py close"

Restart the plugin and test the on/off commands.


