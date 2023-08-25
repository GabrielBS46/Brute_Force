import os

root = os.getuid()

if root == 0:
    # Path of list it password storage Wi-fi
    #dir = os.listdir('/etc/NetworkManager/system-connections/')
    path = '/etc/NetworkManager/system-connections/'
    dir = os.listdir(path)

    # List all file in directory
    for arq in dir:    
        arq = (path + arq)
        # Open one in one for location position of string "id" and "psk"
        with open(arq,'r', errors='ignore') as f:
            name = f.read()
            letter = name.splitlines()
            ssid = letter[1]
            ssid = ssid.replace('Auto ',"")
            psw = letter[13]
            print (f'O ssid é {ssid[3:]} e a senha é {psw[4:]}\n')
else:
    print("Please use as root")
    print("The files in /etc/NetworkManager/system-connections/ have permission of read and write with user root !!!")
    exit(1)