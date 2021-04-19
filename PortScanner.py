import socket
import struct
import binascii

while True:
    from socket import *
    
    print('----------------------------------------------------------------')
    print('  ____            _     ____                                  ')
    print(' |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ ')
    print(" | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|")
    print(' |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   ')
    print(' |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|   ')
    print('')
    print('----------------------------------------------------------------\n')

    choice = input(f'Which function would you like to do, Press 1-4 \n1 Search ports on Local Host \n2 Search ports on Target Machine \n3 Help \n4 Quit \n\nInput: ')
    if choice == '1':
        server_address = '127.0.0.1'
        start = int(input('Enter Port Start Range: '))
        end = int(input('Enter Port End Range: '))
        try:
            for i in range(start, end + 1):
                s = socket(AF_INET, SOCK_STREAM)
                result = s.connect_ex((server_address, i))

                if result == 0 :
                    print ('Port %d: OPEN' % (i,))
                else:
                    print ('Port %d: CLOSED' % (i,))
                s.close
        except:
            print('Scanner is blocked. WinError 10061. Select Option 3 for more information.\n')
        
    elif choice == '2':
        server_address = str(input('Enter target IP address : '))
        start = int(input('Enter Port Start Range: '))
        end = int(input('Enter Port End Range: '))
        try:
            for i in range(start, end + 1):
                s = socket(AF_INET, SOCK_STREAM)
                result = s.connect_ex((server_address, i))

                if result == 0 :
                    print ('Port %d: OPEN' % (i,))
                else:
                    print ('Port %d: CLOSED' % (i,))
                s.close
        except:
            print('Scanner is blocked. WinError 10061. Select Option 3 for more information.\n')
            
    elif choice == '3':
        print('Option 1 will use IP address 127.0.0.1 for scans. \nOption 2 will use the traget IP address.\n\nIf you are looking for a individual port pick pick the number before the port and after the port.\n\nFor example, if you are looking for port 443. Type 442 for the start of range and 444 for the end of the range.\n\nIf you are reciveing WinError 10061 make sure you have: \n *Windows Defender is turned off.\n *Tagert IP address is Online and can recive a ping.\n *Network Domain or Organization does not allow port scanners.\n\nFor more help please refer to StackOverflow for resolutions.\n  ')
    elif choice == '4':
        break
    else:
        print('Please select fromt the options above.')
