
 
import requests
import time
import urllib3
import os
import sys
from random import randint
from bs4 import BeautifulSoup
from collections import Counter
#Version
version = 2.0
#Show
def showoff():
    print("´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´´´´´¶´´´´´´´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´¶´´´¶´´´´´´´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´¶´´¶¶´´´´´´´´´¶¶´´¶´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶¶´´´´´´´¶¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´¶¶´´´´´´¶¶´´´¶¶¶´´´´´¶¶¶´´´¶¶´´´´´´¶¶´´´´´´´´´´´´")
    print("´´´´´´´´´´´¶¶´´´´´´¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶´´´´´´¶¶´´´´´´´´´´´")
    print("´´´´´´´´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶¶´´´´´´´´´´")
    print("´´´´´´´¶´´¶¶¶´´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´´´¶¶¶¶´´´¶¶¶¶´´¶´´´´´´´")
    print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
    print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
    print("´´´´´´´¶¶´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶´¶¶´´´´´´´")
    print("´´´´´´¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶´´´´´´")
    print("´´´´´¶¶¶¶´´¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´¶¶¶¶´´´´´")
    print("´´´´¶¶¶¶´´´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´¶¶¶¶´´´´")
    print("´´´¶¶¶¶´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶´´´´")
    print("´´´¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶´´´´")
    print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´")
    print("´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´")
    print("´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´")
    print("´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´")
    print("´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´")
    print("´´´´´¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶¶¶´´´´´")
    print("´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´")
    print("´´´´´´¶¶¶¶¶¶¶´´´´´´´´..´´´´´¶¶¶¶¶¶¶¶¶´´´´´..´´´´´´´´¶¶¶¶¶¶´´´")
    print("´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´")
    print("´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´")
    print("´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´¶¶¶´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´¶¶´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´¶¶´´´´´´´´´´´´´´´´´´")
    print("´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´¶¶¶¶¶´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´")
    print("\n")
    print("╔═══╦═╗╔═╦════╦═══╦═══╦═══╦════╦══╦═══╦═╗─╔╗")
    print("║╔══╩╗╚╝╔╣╔╗╔╗║╔═╗║╔═╗║╔═╗║╔╗╔╗╠╣╠╣╔═╗║║╚╗║║")
    print("║╚══╗╚╗╔╝╚╝║║╚╣╚═╝║║─║║║─╚╩╝║║╚╝║║║║─║║╔╗╚╝║")
    print("║╔══╝╔╝╚╗──║║─║╔╗╔╣╚═╝║║─╔╗─║║──║║║║─║║║╚╗║║")
    print("║╚══╦╝╔╗╚╗─║║─║║║╚╣╔═╗║╚═╝║─║║─╔╣╠╣╚═╝║║─║║║")
    print("╚═══╩═╝╚═╝─╚╝─╚╝╚═╩╝─╚╩═══╝─╚╝─╚══╩═══╩╝─╚═╝")
    print("\n")
    print(f"VERSION : {version}")
    print('\n')
    print("▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄")
    print("░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ")
    print('\n\n')
    time.sleep(1)
    print("1. [*] MAKE FULL HOST FILE")
    print("2. [*] EXTRACT SUBDOMAINS ONLY")
    print("3. [*] DARK SEARCH WITH MATCHING IDENTITIES FOR GAMMING HOST ONLY")
    print("4. [*] IPS ")
    print("5. [*] EXIT\n\n")
    while True:
        getvs = input("[*] CHOICE IS YOUR OWN: ")
        if getvs.isnumeric():
            getvs_int = int(getvs)
            if getvs_int == 1:
                run = HOST()
                break
            elif getvs_int == 2:
                run = Subdomains()
                break
            elif getvs_int == 3:
                run = DarkSearch()
                break
            elif getvs_int == 4:
                run = IPSearch()
                break
            elif getvs_int == 5:
                sys.exit(0)
                break
            else:
                print("[*] ENTER NUMBERS IN GIVEN RANGE")
        else:
            print("[*] MAKE SURE YOU ENTER NUMERIC VALUES")


class HOST:
    def __init__(self):
        def parse_url(url):
            try:
                host = urllib3.util.url.parse_url(url).host
            except Exception as e:
                print('[*] Invalid domain, type valid One')
                sys.exit(1)
            return host
        def first(getfirst):
            with open(getfirst, 'w') as fs:
                fs.write("99.99.99 ban.com\n999.999 facebook.com\n222.222.222.222 ban.com\n192.168.1.1 broadcasthost\n4.5.6.6 .ban.com\n0.0.0.0 0.0.0.0 com.tencent.ig\n")
                fs.write("255.255.255.255 ban.com\n172.217.6.193 lh5.googleusercontent.com\nfe80::12:34:56:78%eth0 .net\nnfe80::12:34:56:78%eth0 .com\n")
                fs.write("2001:db8:123:456::78 .com\n2001:db8:123:456::78 .net\nah204.236.129.206 10m.com\n54.176.64.1.      ig.com\n54.193.0.3      ig.com\n132.232.173.220    ig.com\n")
                fs.write("52.24.63.252    ig.com\n52.13.255.255    ig.com\n184.72.56.36      ig.com\n127.0.0.1      ig.com\n0.0.0.0    ig.com\n4.5.6.6 ban.com\n0.0.0.0 2.9.9.9 co..tencent.ig\n2.9.9.9.9 cheat.com\n4.4.4.4.4 Facebook.net\n")
                fs.write("9.9.9.9.9 twiter.com\n0.0.0.0 pubgmobile.qq.com\n4.5.6.6 pay.igamecj.com\n4.5.6.6 hkspeed.igamescj.com\n4.5.6.6 .net\n4.5.6.6 .weiyun.com\n0.0.0.0 .actencent.com\n0.0.0.0 .bqqpx.com\n0.0.0.0 .cftres.com\n0.0.0.0 .igcdn.cn\n")
                fs.write('loop  m  loop  mm  m  m loopm\n #  "# #  m"  #  "#  ##  "m m"  #\n#loop" #m#    #mmm#"  # #  # #  #\n #  "m #  #m  #      #mm#  "mm"   #\n\n')
                fs.close()
        def Make_file1(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(subdomain + "," + ast + '\n')
                ss.close()
        def Make_file2(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(ast + " " + subdomain + '\n')
                ss.close()
        def Make_file3(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(ast + " "+ subdomain + '\n')
                ss.close()
        def Make_file4(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(subdomain + "," + ast + '\n')
                ss.close()
        def Last(getlast):
            with open(getlast, 'a') as lw:
                lw.write("\nlocalhost.localdomain\nlocalhost 127.0.0.1\nlocalhost 0.0.0.0\n127.0.0.1 :\n0.0.0.0 :\n")
                lw.close()
        def main():
            subdomains = []    
            attacks = input("[*] How Much Domains You want to put: ")
            domains = []
            d = 1
            if attacks.isnumeric():
                attacks_int = int(attacks)
                while d < attacks_int + 1:
                    gets = input("[*] Input Your " + str(d) + " Domain : ")
                    domains.append(gets)
                    d +=1       
            else:
                sys.exit(1)
            output = str(input("[*] Enter File Name to save: "))
            ad = False
            ac = False
            firstH = False
            print("\n1. [*] WANT TO PUT PREFIXES (IP AT FIRST) MANUALLY")
            print("2. [*] WANT TO PUT LAST IP MANUALLY")
            print("3. [*] USE DEFULT LAST IP AS 0.0.0.1")
            print("4. [*] GENETRATE RANDOM IPS AS PREFIXES")
            print("5. [*} GENETRATE RANDOM IPS AS LAST SETS")
            print("6. [*] RETURN HOME")
            print("7. [*] EXIT\n ")

            while True:
                stram = input("[*] CHOOSE WHAT YOU WANT : ")
                if stram.isnumeric():
                    stram_int = int(stram)
                    if stram_int == 1:
                        ab = input("\n[*] Enter your IP: ")
                        firstH = True
                        break
                    elif stram_int == 2:
                        ab = input("\n[*] Enter your IP: ")
                        if "." in ab:
                            break
                        else:
                           print("[!] WRITE CORRECT IP LIKE 127.0.0.1")
                    elif stram_int == 3:
                        ab = "0.0.0.1"
                        break
                    elif stram_int == 4:
                        ad = True
                        break
                    elif stram_int == 5:
                        ac = True
                        break
                    elif stram_int == 6:
                        showoff()
                        break
                    elif stram_int == 7:
                        sys.exit(1)
                        break
                    else:
                        print("\n[*] PUT NUMBER IN THE GIVEN RANGE\n")
                else:
                    print("\n[*] MAKE SURE TO PUT ONLY INTEGERS\n")
                        
            first(output)
            print("\n")
            print("░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ ")
            print("░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  ")
            print("░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █")
            print("\n\n")
            for t in domains:
                target = parse_url(t)
                try:
                    request = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
                except:
                    print("[*] ####################   CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION     ###################  [*]")
                    sys.exit(1)
                if request.status_code != 200:
                    print(f'[*] Information not Available For that Target: {target}')
                    sys.exit(1)
                for (key,value) in enumerate(request.json()):
                    subdomains.append(value['name_value'])
                print(f"\n[!] **************** TARGET ATTACK : {target} *********************** \n")
                Tries = sorted(set(subdomains))
                if ad or ac == True:
                    ip1 = randint(1,360)
                    ip2 = randint(1,300)
                    ip3 = randint(1,400)
                    ip4 = randint(1,330)
                    ip = ip1 + '.' + ip2 + '.' + ip3 +'.' +ip4
            if ad == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file2(w, output,ip)
            elif ac == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file1(w, output,ip)
            elif firstH == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file3(w, output,ab)
            else:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file4(w, output,ab)
                
            Last(output)
            print("\n\n[!!] DONE EXTRACTION SUBSCRIBE TO MY CHANNEL FOR MORE HACKING TOOLS...........\n")
            try:
                os.startfile(output)
            except:
                pass
                print("╔══╗╔══╗╔╗─╔══╗╔═╗╔═╗")
                print("║═╦╝╚║║╝║║─╠══║║╦╝║╬║")
                print("║╔╝─╔║║╗║╚╗║══╣║╩╗║╗╣")
                print("╚╝──╚══╝╚═╝╚══╝╚═╝╚╩╝")
                print("\n\n")
        if __name__=='__main__':
            main()

#Subdomains only
class Subdomains:
    def __init__(self):
        def parse_url(url):
            try:
                host = urllib3.util.url.parse_url(url).host
            except Exception as e:
                print('[*] Invalid domain, type valid One')
                sys.exit(1)
            return host
        def Make_file(subdomain,output_file):
            with open(output_file, 'a') as ss:
                ss.write(subdomain + '\n')
                ss.close()
        def main():
            subdomains = []    
            attacks = input("[*] How Much Domains You want to put: ")
            domains = []
            d = 1
            if attacks.isnumeric():
                attacks_int = int(attacks)
                while d < attacks_int + 1:
                    gets = input("[*] Input Your " + str(d) + " Domain : ")
                    domains.append(gets)
                    d +=1       
            else:
                sys.exit(1)
            output = str(input("[*] Enter File Name to save: "))
            print("\n")
            print("░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ ")
            print("░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  ")
            print("░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █")
            print("\n\n")
            for t in domains:
                target = parse_url(t)
                try:
                    request = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
                except:
                    print("[*] ####################   CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION     ###################  [*]")
                    sys.exit(1)
                if request.status_code != 200:
                    print('[*] Information not Available For that Target!')
                    sys.exit(1)
                for (key,value) in enumerate(request.json()):
                    subdomains.append(value['name_value'])
                print(f"\n[!] **************** TARGET ATTACK : {target} *********************** \n")
                Tries = sorted(set(subdomains))
            for w in Tries:
                print(f'{w}\n')
                if output is not None:
                    Make_file(w, output)
            print("\n\n[!!] DONE EXTRACTION SUBSCRIBE TO MY CHANNEL FOR MORE HACKING TOOLS...........\n")
            try:
                os.startfile(output)
            except:
                pass
                print("╔══╗╔══╗╔╗─╔══╗╔═╗╔═╗")
                print("║═╦╝╚║║╝║║─╠══║║╦╝║╬║")
                print("║╔╝─╔║║╗║╚╗║══╣║╩╗║╗╣")
                print("╚╝──╚══╝╚═╝╚══╝╚═╝╚╩╝")
                print("\n\n")     
        if __name__=='__main__':
            main()

#darkDeepSearch
class DarkSearch:
    def __init__(self):
        def parse_url(url):
            try:
                host = urllib3.util.url.parse_url(url).host
            except Exception as e:
                print('[*] Invalid domain, type valid One')
                sys.exit(1)
            return host
        def first(getfirst):
            with open(getfirst, 'w') as fs:
                fs.write("99.99.99 ban.com\n999.999 facebook.com\n222.222.222.222 ban.com\n192.168.1.1 broadcasthost\n4.5.6.6 .ban.com\n0.0.0.0 0.0.0.0 com.tencent.ig\n")
                fs.write("255.255.255.255 ban.com\n172.217.6.193 lh5.googleusercontent.com\nfe80::12:34:56:78%eth0 .net\nnfe80::12:34:56:78%eth0 .com\n")
                fs.write("2001:db8:123:456::78 .com\n2001:db8:123:456::78 .net\nah204.236.129.206 10m.com\n54.176.64.1.      ig.com\n54.193.0.3      ig.com\n132.232.173.220    ig.com\n")
                fs.write("52.24.63.252    ig.com\n52.13.255.255    ig.com\n184.72.56.36      ig.com\n127.0.0.1      ig.com\n0.0.0.0    ig.com\n4.5.6.6 ban.com\n0.0.0.0 2.9.9.9 co..tencent.ig\n2.9.9.9.9 cheat.com\n4.4.4.4.4 Facebook.net\n")
                fs.write("9.9.9.9.9 twiter.com\n0.0.0.0 pubgmobile.qq.com\n4.5.6.6 pay.igamecj.com\n4.5.6.6 hkspeed.igamescj.com\n4.5.6.6 .net\n4.5.6.6 .weiyun.com\n0.0.0.0 .actencent.com\n0.0.0.0 .bqqpx.com\n0.0.0.0 .cftres.com\n0.0.0.0 .igcdn.cn\n")
                fs.write('loop  m  loop  mm  m  m loopm\n #  "# #  m"  #  "#  ##  "m m"  #\n#loop" #m#    #mmm#"  # #  # #  #\n #  "m #  #m  #      #mm#  "mm"   #\n\n')
                fs.close()
        def Make_file1(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(subdomain + "," + ast + '\n')
                ss.close()
        def Make_file2(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(ast + " " + subdomain + '\n')
                ss.close()
        def Make_file3(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(ast + " "+ subdomain + '\n')
                ss.close()
        def Make_file4(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                ss.write(subdomain + "," + ast + '\n')
                ss.close()
        def Last(getlast):
            with open(getlast, 'a') as lw:
                lw.write("\nlocalhost.localdomain\nlocalhost 127.0.0.1\nlocalhost 0.0.0.0\n127.0.0.1 :\n0.0.0.0 :\n")
                lw.close()
        def main():
            subdomains = []    
            attacks = input("[*] How Much Domains You want to put: ")
            domains = []
            d = 1
            if attacks.isnumeric():
                attacks_int = int(attacks)
                while d < attacks_int + 1:
                    gets = input("[*] Input Your " + str(d) + " Domain : ")
                    domains.append(gets)
                    d +=1       
            else:
                sys.exit(1)
            output = str(input("[*] Enter File Name to save: "))
            ad = False
            ac = False
            firstH = False
            print("\n1. [*] WANT TO PUT PREFIXES (IP AT FIRST) MANUALLY")
            print("2. [*] WANT TO PUT LAST IP MANUALLY")
            print("3. [*] USE DEFULT LAST IP AS 0.0.0.1")
            print("4. [*] GENETRATE RANDOM IPS AS PREFIXES")
            print("5. [*} GENETRATE RANDOM IPS AS LAST SETS")
            print("6. [*] RETURN HOME")
            print("7. [*] EXIT\n ")

            while True:
                stram = input("[*] CHOOSE WHAT YOU WANT : ")
                if stram.isnumeric():
                    stram_int = int(stram)
                    if stram_int == 1:
                        ab = input("\n[*] Enter your IP: ")
                        firstH = True
                        break
                    elif stram_int == 2:
                        ab = input("\n[*] Enter your IP: ")
                        if "." in ab:
                            break
                        else:
                           print("[!] WRITE CORRECT IP LIKE 127.0.0.1")
                    elif stram_int == 3:
                        ab = "0.0.0.1"
                        break
                    elif stram_int == 4:
                        ad = True
                        break
                    elif stram_int == 5:
                        ac = True
                        break
                    elif stram_int == 6:
                        showoff()
                        break
                    elif stram_int == 7:
                        sys.exit(1)
                        break
                    else:
                        print("\n[*] PUT NUMBER IN THE GIVEN RANGE\n")
                else:
                    print("\n[*] MAKE SURE TO PUT ONLY INTEGERS\n")
                        
            first(output)
            print("\n")
            print("░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ ")
            print("░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  ")
            print("░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █")
            print("\n\n")
            for t in domains:
                target = parse_url(t)
                try:
                    request = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
                    req2 = requests.get(f'https://webiplookup.com/{target}/domain.htm')
                except:
                    print("[*] ####################   CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION     ###################  [*]")
                    sys.exit(1)
                #req2
                try:
                    website = req2.text
                    soup = BeautifulSoup(website, features = "html.parser")
                except:
                    print("[*] GETTING ERROR CHECK YOU INSTALLED (bs4) MODULE PROPERLY?")

                if request.status_code and req2.status_code != 200:
                    print(f'[*] Information not Available For that Target: {target}')
                    sys.exit(1)
                for (key,value) in enumerate(request.json()):
                    subdomains.append(value['name_value'])
                #req2
                for link in soup.find_all("a", attrs={"target": "_blank"}):
                    d = str(link.get_text())
                    if target in d:
                        subdomains.append(d)
                    else:
                        pass
                print(f"\n[!] **************** TARGET ATTACK : {target} *********************** \n")
                Tries = sorted(set(subdomains))
                if ad or ac == True:
                    ip1 = str(randint(1,360))
                    ip2 = str(randint(1,300))
                    ip3 = str(randint(1,400))
                    ip4 = str(randint(1,330))
                    ip = ip1 + '.' + ip2 + '.' + ip3 +'.' +ip4
            if ad == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file2(w, output,ip)
            elif ac == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file1(w, output,ip)
            elif firstH == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file3(w, output,ab)
            else:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file4(w, output,ab)
                
            Last(output)
            print("\n\n[!!] DONE EXTRACTION SUBSCRIBE TO MY CHANNEL FOR MORE HACKING TOOLS...........\n")
            try:
                os.startfile(output)
            except:
                pass
                print("╔══╗╔══╗╔╗─╔══╗╔═╗╔═╗")
                print("║═╦╝╚║║╝║║─╠══║║╦╝║╬║")
                print("║╔╝─╔║║╗║╚╗║══╣║╩╗║╗╣")
                print("╚╝──╚══╝╚═╝╚══╝╚═╝╚╩╝")
                print("\n\n")     
        if __name__=='__main__':
            main()

#allIps
class IPSearch:
    def __init__(self):
        def parse_url(url):
            try:
                host = urllib3.util.url.parse_url(url).host
            except Exception as e:
                print('[*] Invalid domain, type valid One')
                sys.exit(1)
            return host
        def first(getfirst):
            with open(getfirst, 'w') as fs:
                fs.write("99.99.99 ban.com\n999.999 facebook.com\n222.222.222.222 ban.com\n192.168.1.1 broadcasthost\n4.5.6.6 .ban.com\n0.0.0.0 0.0.0.0 com.tencent.ig\n")
                fs.write("255.255.255.255 ban.com\n172.217.6.193 lh5.googleusercontent.com\nfe80::12:34:56:78%eth0 .net\nnfe80::12:34:56:78%eth0 .com\n")
                fs.write("2001:db8:123:456::78 .com\n2001:db8:123:456::78 .net\nah204.236.129.206 10m.com\n54.176.64.1.      ig.com\n54.193.0.3      ig.com\n132.232.173.220    ig.com\n")
                fs.write("52.24.63.252    ig.com\n52.13.255.255    ig.com\n184.72.56.36      ig.com\n127.0.0.1      ig.com\n0.0.0.0    ig.com\n4.5.6.6 ban.com\n0.0.0.0 2.9.9.9 co..tencent.ig\n2.9.9.9.9 cheat.com\n4.4.4.4.4 Facebook.net\n")
                fs.write("9.9.9.9.9 twiter.com\n0.0.0.0 pubgmobile.qq.com\n4.5.6.6 pay.igamecj.com\n4.5.6.6 hkspeed.igamescj.com\n4.5.6.6 .net\n4.5.6.6 .weiyun.com\n0.0.0.0 .actencent.com\n0.0.0.0 .bqqpx.com\n0.0.0.0 .cftres.com\n0.0.0.0 .igcdn.cn\n")
                fs.write('loop  m  loop  mm  m  m loopm\n #  "# #  m"  #  "#  ##  "m m"  #\n#loop" #m#    #mmm#"  # #  # #  #\n #  "m #  #m  #      #mm#  "mm"   #\n')
                fs.write("0.0.0.0 .net\n0.0.0.0 .com\n0.0.0.0 .org\n0.0.0.0 .kr\n0.0.0.0 .xyz\n0.0.0.0 .qq.com\n0.0.0.0 .gtimg.com\n0.0.0.0 .akmized.com\n0.0.0.0 .in\n0.0.0.0 .uk\n0.0.0.0 .qlogo.cn\n0.0.0.0 .twimg.com\n0.0.0.0 .reverse.com\n0.0.0.0 .fbsbx.com\n0.0.0.0 .cnzz.com\n0.0.0.0 .googletamanager.com\n0.0.0.0 .intellitxt.com\n0.0.0.0 .googleapis.com\n0.0.0.0 .fbsbx.com\n0.0.0.0 .app-measurement.com\n0.0.0.0 .ushareit.com\n0.0.0.0 .userapi.com\n0.0.0.0 .1e100.net\n0.0.0.0 .cn\n0.0.0.0 .cnzz\n0.0.0.0 .us\n0.0.0.0 .jp\n0.0.0.0 .tech\n0.0.0.0 .qq\n0.0.0.0 .cn\n")
                fs.write("0.0.0.0 .co\n0.0.0.0 .icu\n0.0.0.0 .vip\n0.0.0.0 .tv\n0.0.0.0 .seedmm\n0.0.0.0 .work\n")
                fs.write('0.0.0.0 45.51.177.92\n0.0.0.0 192.168.43.1\n0.0.0.0 45.40.223.218\n0.0.0.0 20.37.82.36\n0.0.0.0 150.109.124.135\n0.0.0.0 182.254.116.117\n0.0.0.0 49.51.42.152\n0.0.0.0 45.40.223.66\n0.0.0.0 45.40.220.200\n0.0.0.0 2001:db8:123:456::78\n0.0.0.0 2001:db8:123:456::78\n')
                fs.write('0.0.0.0 .gcloudsdk.com\n0.0.0.0 .facebook.com\n0.0.0.0 .igamecj.com\n0.0.0.0 .tdatamaster.com\n0.0.0.0 .gcloudcs.com\n0.0.0.0 .adjust.com\n0.0.0.0 .fbsbx.com\n0.0.0.0 .googleusercontent.com\n0.0.0.0 .proximabeta.com\n0.0.0.0 .pubgmobile.com\n0.0.0.0 .battlegroundsmobile.kr\n0.0.0.0 .qcloud.com\n0.0.0.0 .qq.com\n0.0.0.0 .helpshift.com\n0.0.0.0 .wetest.net\n')
                fs.close()
        def Make_file3(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                for sa in ast:
                    ss.write(sa + " "+ subdomain + '\n')
                ss.close()
        def Make_file4(subdomain,output_file,ast):
            with open(output_file, 'a') as ss:
                ss.write("0.0.0.0 .ff212::ffee::1 #.fe9e6:1::0 ff212::ffee::1 0.0.0.0 .127.0.0.1\n")
                for sa in ast:  
                    ss.write(subdomain + "," + sa + '\n')
                ss.close()
        def Last(getlast,ips,domains):
            with open(getlast, 'a') as lw:
                for s in ips :
                    for w in domains:
                        lw.write(f'\n{s}       localhost\n::1             ip6-localhost\n{s} loop   m mm   mmm    mmm   mm#mm\n #" "#   #"  " #" "#  #" "#    #\n #   #   #     #   #  #   #    #\n "#m"#   #     "#m#"  "#m#"    "mm  m  #\n   ""#loop" #m#    #mmm#"  #  #   #  #    # "\n #   "m #  #m  #       #mm#   "mm"    #\n{s} .{w}\n #    " #   "m #      #    #   ##   mm#mm\n{s} .{w}\nloop  m    loop  mm   m    m loopm\n #   "# #  m"  #   "#   ##   "m  m"   #\n #loop" #m#    #mmm#"  #  #   #  #    #\n{s} .{w}\n#loop" #m#    #mmm#"  #  #   #  #    #\n #   "m #  #m  #       #mm#   "mm"    #\n{s} .{w}\n #    " #   "m #      #    #   ##   mm#mm\n{s} .a{w}\nloop  m    loop  mm   m    m loopm\n #   "# #  m"  #   "#   ##   "m  m"   #\n #loop" #m#    #mmm#"  #  #   #  #    #\n{s} .{w}\n#loop" #m#    #mmm#"  #  #   #  #    #\n #   "m #  #m  #       #mm#   "mm"    #\n #    " #   "m #      #    #   ##   mm#mm\n{s} .{w}\n{s} .{w}\n#loop" #m#    #mmm#"  #  #   #  #    #\n #   "m #  #m  #       #mm#   "mm"    #\n #    " #   "m #      #    #   ##   mm#mm\n{s} .{w}\n#loop" #m#    #mmm#"  #  #   #  #    #\n #   "m #  #m  #       #mm#   "mm"    #\n')
                        lw.write(f'{s} .{w}\n#loop" #m#    #mmm#"  #  #   #  #    #\n#   "m #  #m  #       #mm#   "mm"    #\n')
                lw.write('8.8.8.8 : 49.51.137.169\n8.8.8.8 : 129.226.20.31\n8.8.8.8 : 125.17.143.20\n8.8.8.8 : 157.47.102.145\n8.8.8.8 : 192.168.1.77\n8.8.8.8 : 192.168.1.64\n8.8.8.8 : 176.23.125.6\n8.8.8.8 : 74.125.142.27\n8.8.8.8 : 169.38.138.34\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 169.38.124.176\n8.8.8.8 : 119.28.250.154\n8.8.8.8 : 129.226.20.140\n8.8.8.8 : 119.28.252.24\n8.8.8.8 : 169.38.104.202\n8.8.8.8 : 119.28.244.50\n8.8.8.8 : 49.51.42.99\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 169.38.138.229\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 150.109.124.26\n8.8.8.8 : 150.109.124.161\n')
                lw.write('8.8.8.8 : 169.38.104.245\n8.8.8.8 : 45.40.223.119\n8.8.8.8 : 45.40.223.42\n8.8.8.8 : 169.38.138.212\n8.8.8.8 : 45.40.223.246\n8.8.8.8 : 169.38.104.196\n8.8.8.8 : 45.40.223.55\n8.8.8.8 : 45.40.223.115\n8.8.8.8 : 45.40.220.236\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 150.109.29.150\n8.8.8.8 : 119.28.121.174\n8.8.8.8 : 150.109.124.196\n8.8.8.8 : 45.40.220.178\n8.8.8.8 : 150.109.0.38\n8.8.8.8 : 150.109.0.45\n8.8.8.8 : 150.109.124.67\n8.8.8.8 : 45.40.223.193\n8.8.8.8 : 124.156.62.235\n8.8.8.8 : 119.28.244.50\n8.8.8.8 : 119.28.244.50\n8.8.8.8 : 203.205.137.232\n8.8.8.8 : 203.205.137.242\n8.8.8.8 : 45.40.223.125\n')
                lw.write('8.8.8.8 : 150.109.124.147\n8.8.8.8 : 124.156.50.114\n8.8.8.8 : 150.109.124.127\n8.8.8.8 : 45.40.223.210\n8.8.8.8 : 124.156.40.50\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 124.156.12.224 \n8.8.8.8 : 119.28.252.31\n8.8.8.8 : 119.28.250.62\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 129.226.22.149\n8.8.8.8 : 119.28.249.247\n8.8.8.8 : 124.156.50.69\n8.8.8.8 : 119.28.246.225\n8.8.8.8 : 124.156.40.38\n8.8.8.8 : 124.156.12.103\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 129.226.20.68\n8.8.8.8 : 119.28.252.22\n8.8.8.8 : 119.28.251.21\n8.8.8.8 : 124.156.13.239\n8.8.8.8 : 129.226.22.9\n8.8.8.8 : 169.38.138.214\n8.8.8.8 : 129.226.20.44\n8.8.8.8 : 129.226.22.236\n8.8.8.8 : 169.38.138.194\n8.8.8.8 : 129.226.22.236\n8.8.8.8 : 119.28.252.20\n')
                lw.write('8.8.8.8 : 49.51.66.82\n8.8.8.8 : 124.156.40.170\n8.8.8.8 : 124.156.33.65\n8.8.8.8 : 169.38.104.150\n8.8.8.8 : 119.28.252.80\n8.8.8.8 : 124.156.12.89\n8.8.8.8 : 101.32.80.230\n8.8.8.8 : 169.38.138.157\n8.8.8.8 : 119.28.247.32\n8.8.8.8 : 182.254.116.117\n8.8.8.8 : 119.28.246.125\n8.8.8.8 : 169.38.138.116\n8.8.8.8 : 124.156.13.105\n8.8.8.8 : 129.226.20.46\n8.8.8.8 : 101.32.80.230\n8.8.8.8 : 169.38.138.205\n8.8.8.8 : 119.28.248.210\n8.8.8.8 : 129.226.23.150\n8.8.8.8 : 129.226.22.40\n8.8.8.8 : 169.38.104.191\n8.8.8.8 : 119.28.246.160\n8.8.8.8 : 129.226.20.122\n8.8.8.8 : 169.38.104.223\n8.8.8.8 : 129.226.20.11\n8.8.8.8 : 129.226.20.208\n8.8.8.8 : 169.38.138.229\n8.8.8.8 : 124.156.13.130\n8.8.8.8 : 124.156.34.55\n8.8.8.8 : 45.40.223.226\n')
                lw.write('8.8.8.8 : 49.51.42.152\n8.8.8.8 : 124.156.64.155\n8.8.8.8 : 45.40.223.131\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 129.226.20.54\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 169.38.104.177\n8.8.8.8 : 129.226.22.95\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 129.226.20.124\n8.8.8.8 : 129.226.22.213\n8.8.8.8 : 129.226.22.83\n8.8.8.8 : 129.226.23.57\n8.8.8.8 : 119.28.247.163\n8.8.8.8 : 45.40.220.187\n8.8.8.8 : 45.40.220.200\n8.8.8.8 : 119.28.250.208 \n8.8.8.8 : 129.226.20.66\n8.8.8.8 : 124.156.34.15\n8.8.8.8 : 169.38.138.160\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 129.226.20.54\n8.8.8.8 : 129.226.22.95\n8.8.8.8 : 129.226.22.213\n8.8.8.8 : 119.28.250.208\n8.8.8.8 : 169.38.92.221\n8.8.8.8 : 124.156.34.15\n8.8.8.8 : 150.109.124.251\n8.8.8.8 : 150.109.124.148\n8.8.8.8 : 150.109.124.251\n8.8.8.8 : 150.109.124.148\n8.8.8.8 : 45.40.223.226\n8.8.8.8 : 49.51.42.152\n8.8.8.8 : 45.40.223.131\n')
                lw.write('8.8.8.8 : 124.156.64.155\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 150.109.124.248\n8.8.8.8 : 124.156.34.43\n8.8.8.8 : 45.40.220.207\n8.8.8.8 : 150.109.124.230\n8.8.8.8 : 150.109.124.22\n8.8.8.8 : 169.38.138.119\n8.8.8.8 : 45.40.220.136\n8.8.8.8 : 45.40.220.72\n8.8.8.8 : 169.38.138.2\n8.8.8.8 : 182.254.116.117\n8.8.8.8 : 45.40.220.39\n8.8.8.8 : 150.109.124.52\n8.8.8.8 : 192.168.43.1\n8.8.8.8 : 45.40.223.26\n8.8.8.8 : 124.156.64.161\n8.8.8.8 : 45.40.223.190\n8.8.8.8 : 45.40.220.95\n8.8.8.8 : 124.156.55.106\n8.8.8.8 : 169.38.138.116\n8.8.8.8 : 124.156.13.105\n8.8.8.8 : 101.32.80.230\n8.8.8.8 : 101.32.80.233\n8.8.8.8 : 129.226.23.150\n8.8.8.8 : 169.38.104.191\n8.8.8.8 : 129.226.20.122\n8.8.8.8 : 129.226.20.11\n8.8.8.8 : 129.226.20.208\n8.8.8.8 : 169.38.138.229\n8.8.8.8 : 124.156.13.130\n8.8.8.8 : 124.156.34.55\n8.8.8.8 : 45.40.223.221\n')
                lw.write("\nlocalhost.localdomain\nlocalhost 127.0.0.1\nlocalhost 0.0.0.0\n127.0.0.1 :\n0.0.0.0 :\n")
                lw.close()
        def main():
            subdomains = []    
            attacks = input("[*] How Much Domains You want to put: ")
            domains = []
            ips =['0.0.0.0', '0.0.0.1', '127.0.0.1' , '8.8.8.8' , '8.8.4.4']
            d = 1
            if attacks.isnumeric():
                attacks_int = int(attacks)
                while d < attacks_int + 1:
                    gets = input("[*] Input Your " + str(d) + " Domain : ")
                    domains.append(gets)
                    d +=1       
            else:
                sys.exit(1)
            output = str(input("[*] Enter File Name to save: "))
            firstH = False
            al = False
            print("\n1. [*] WANT TO PUT PREFIXES (IP AT FIRST)")
            print("2. [*] WANT TO PUT LAST IP")
            print("3. [*] RETURN HOME")
            print("4. [*] EXIT\n ")

            while True:
                stram = input("[*] CHOOSE WHAT YOU WANT : ")
                if stram.isnumeric():
                    stram_int = int(stram)
                    if stram_int == 1:
                        firstH = True
                        break
                    elif stram_int == 2:
                        al = True 
                    elif stram_int == 3:
                        showoff()
                        break
                    elif stram_int == 4:
                        sys.exit(1)
                        break
                    else:
                        print("\n[*] PUT NUMBER IN THE GIVEN RANGE\n")
                else:
                    print("\n[*] MAKE SURE TO PUT ONLY INTEGERS\n")
                        
            first(output)
            print("\n")
            print("░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ ")
            print("░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  ")
            print("░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █")
            print("\n\n")
            for t in domains:
                target = parse_url(t)
                try:
                    req2 = requests.get(f'https://webiplookup.com/{target}/domain.htm')
                    reqIP = requests.get(f"https://webiplookup.com/{target}/")
                except:
                    print("[*] ####################   CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION     ###################  [*]")
                    sys.exit(1)
                #req2
                try:
                    website = req2.text
                    soup = BeautifulSoup(website, features = "html.parser")
                    website2 = reqIP.text
                    soup2 = BeautifulSoup(website2, features = "html.parser")
                except:
                    print("[*] GETTING ERROR CHECK YOU INSTALLED (bs4) MODULE PROPERLY?")

                if req2.status_code and reqIP.status_code != 200:
                    print(f'[*] Information not Available For that Target: {target}')
                    sys.exit(1)

                #req2
                for link in soup.find_all("a", attrs={"target": "_blank"}):
                    d = str(link.get_text())
                    if target in d:
                        subdomains.append(d)
                    else:
                        pass
                #ips getting
                for linkIP in soup2.find_all("a", attrs={"target": "_blank"}):
                    IPw = linkIP.get_text()
                    length = Counter(IPw)
                    var = "a","b",'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
                    for (k,v) in length.items():
                        if k == "." and v == 3 and length != var:
                            ips.append(IPw)                
                        else:
                            pass

                time.sleep(4)
                print(f"\n[!] **************** TARGET ATTACK : {target} *********************** \n")
                Tries = sorted(set(subdomains))
                
            if firstH == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file3(w, output,ips)
            elif al == True:
                for w in Tries:
                    print(f'{w}\n')
                    if output is not None:
                        Make_file4(w, output,ips)
                
            Last(output,ips,domains)
            print("\n\n[!!] DONE EXTRACTION SUBSCRIBE TO MY CHANNEL FOR MORE HACKING TOOLS...........\n")
            try:
                os.startfile(output)
            except:
                pass
                print("╔══╗╔══╗╔╗─╔══╗╔═╗╔═╗")
                print("║═╦╝╚║║╝║║─╠══║║╦╝║╬║")
                print("║╔╝─╔║║╗║╚╗║══╣║╩╗║╗╣")
                print("╚╝──╚══╝╚═╝╚══╝╚═╝╚╩╝")
                print("\n\n")     
        if __name__=='__main__':
            main()

