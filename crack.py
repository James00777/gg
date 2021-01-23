#!/usr/bin/python
# -*- coding: utf-8

import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Tes.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;91m|', '\x1b[1;93m/', '\x1b[1;92m\xe2\x94\x80', '\x1b[1;94m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;96mJames404 ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo = """		
\033[1;91m╋╋┏┳━━━┳━┓┏━┳━━━┳━━━┓
\033[1;92m╋╋┃┃┏━┓┃┃┗┛┃┃┏━━┫┏━┓┃
\033[1;93m╋╋┃┃┃╋┃┃┏┓┏┓┃┗━━┫┗━━┓
\033[1;94m┏┓┃┃┗━┛┃┃┃┃┃┃┏━━┻━━┓┃
\033[1;95m┃┗┛┃┏━┓┃┃┃┃┃┃┗━━┫┗━┛┃
\033[1;96m┗━━┻┛╋┗┻┛┗┛┗┻━━━┻━━━┛
💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   TRICKER-JAMES.☕
           💕💕         JAMES-HACKER 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕
\x1b[1;94m---------------------------------------------------
\x1b[1;91m➣ HACKING IS NOT CRIME IT’S A GAME AGAINST OF THE SYSTEM 
\x1b[1;92m➣ BANGLADESH BLACK HAT HACKER
\x1b[1;93m➣     AUTHOR : JAMES-HACKER
\x1b[1;94m➣       FROM : DHAKA,NARAYANGANJ 
\x1b[1;95m➣   WHATSAPP : +96598064347
\x1b[1;96m➣    WARNING : DON’T USE ILLEGAL WAY
\x1b[1;97m➣    WARNING : ONLY EDUCATIONAL PURPOSE 
\x1b[1;91m➣    WARNING : DON'T COPY MY SCRIPT
\x1b[1;92m➣    WARNING : IF YOU GET TO FACE PROBLEM CLONING TIME
\x1b[1;93m➣    WARNING : USE PROXY US SUPAR VPN FOR CLONING  
\x1b[1;94m---------------------------------------------------""" 
logo1 = """		
\033[1;91m╋╋┏┳━━━┳━┓┏━┳━━━┳━━━┓
\033[1;92m╋╋┃┃┏━┓┃┃┗┛┃┃┏━━┫┏━┓┃
\033[1;93m╋╋┃┃┃╋┃┃┏┓┏┓┃┗━━┫┗━━┓
\033[1;94m┏┓┃┃┗━┛┃┃┃┃┃┃┏━━┻━━┓┃
\033[1;95m┃┗┛┃┏━┓┃┃┃┃┃┃┗━━┫┗━┛┃
\033[1;96m┗━━┻┛╋┗┻┛┗┛┗┻━━━┻━━━┛
💕🍃🌹🍃💕
💕.•°``°•.¸.•°``°•.💕
   (   🍃 🌹 🍃   ) 💕
 💕`•.¸   💗   ¸.•` 💕 
     💕° •.¸¸.•° 💕   TRICKER-JAMES.☕
           💕💕         JAMES-HACKER 🍃🌻🍃
             💕     💕🍃🌹🍃💕  .💘
                    💕.•°``°•.¸.•°``°•.💕
                   💕(  🍃 🌹 🍃   ) 💕
                     💕`•.¸   💗   ¸.•` 💕
                          💕° •.¸¸.•° 💕
                                💕💕
                                  💕
\x1b[1;94m---------------------------------------------------
\x1b[1;91m➣ HACKING IS NOT CRIME IT’S A GAME AGAINST OF THE SYSTEM 
\x1b[1;92m➣ BANGLADESH BLACK HAT HACKER
\x1b[1;93m➣     AUTHOR : JAMES-HACKER
\x1b[1;94m➣       FROM : DHAKA,NARAYANGANJ 
\x1b[1;95m➣   WHATSAPP : +96598064347
\x1b[1;96m➣    WARNING : DON’T USE ILLEGAL WAY
\x1b[1;97m➣    WARNING : ONLY EDUCATIONAL PURPOSE 
\x1b[1;91m➣    WARNING : DON'T COPY MY SCRIPT
\x1b[1;92m➣    WARNING : IF YOU GET TO FACE PROBLEM CLONING TIME
\x1b[1;93m➣    WARNING : USE PROXY US SUPAR VPN FOR CLONING  
\x1b[1;94m---------------------------------------------------""" 
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
CorrectUsername = 'BLACK404'
CorrectPassword = 'JAMES404'
loop = 'true'
while loop == 'true':
    os.system('clear')
    print logo1
    jalan('')
    jalan('\x1b[1;92mHave You Get Username And Password...')
    jalan(' For Login Tools? If you dont have it, its just okay')
    jalan('  Later Diverted')
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    username = raw_input('\x1b[1;96m{\x1b[1;93m\xe2\x98\x86\x1b[1;96m} \x1b[1;97mUsername \x1b[1;96m>>>> \x1b[1;92m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;96m{\x1b[1;93m\xe2\x98\x86\x1b[1;96m} \x1b[1;97mPassword \x1b[1;96m>>>> \x1b[1;92m')
        if password == CorrectPassword:
            print 'Orang Yang Paling Gans Adalah ' + username
            loop = 'false'
        else:
            print 'Upps Salah:('
            os.system('xdg-open https://www.facebook.com/groups/1534351163432432/?ref=share')
            os.system('clear')
    else:
        print 'Upps Salah:('
        os.system('xdg-open https://www.facebook.com/Apni.bapka.account7')
        os.system('clear')

def pertanyaan():
    os.system('clear')
    nama = raw_input('\n\x1b[1;97mYour name? \x1b[1;91m: \x1b[1;92m')
    if nama == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mWhats your name?!'
        time.sleep(1)
        pertanyaan()
    else:
        os.system('clear')
        jalan('\x1b[1;97mHello! \x1b[1;92m' + nama + ' \x1b[1;97mThanks For Useing My Tools\nAnd Always Pray For Me\nAll Comand I Give You Free\nDont Asking Money Any Other Person It’s Spam: \x1b[1;96mhttps://www.facebook.com/Apni.bapka.account7')
        time.sleep(1)
        masuk()


def masuk():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;92m01\x1b[1;97m} Login Via Token Facebook'
    print '\x1b[1;97m{\x1b[1;92m02\x1b[1;97m} Login Via Cokies Facebook'
    print '\x1b[1;97m{\x1b[1;92m03\x1b[1;97m} All Tutorial Hack Facebook'
    print '\x1b[1;97m{\x1b[1;92m04\x1b[1;97m} Joined Group Facebook'
    print '\x1b[1;97m{\x1b[1;92m05\x1b[1;97m} Update Tools'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;90m>>> \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mLihat menu dong ajg!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '3' or msuk == '03':
        kontol()
    elif msuk == '4' or msuk == '04':
        join_grup()
    elif msuk == '5' or msuk == '05':
        yayanxd()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mLihat menu dong ajg!'
        pilih_masuk()


def join_grup():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[1;92mYou Will Be Directed to The Facebook Group')
    os.system('xdg-open https://www.facebook.com/groups/1534351163432432/?ref=share')
    time.sleep(2)
    masuk()


def tokenz():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('\x1b[1;92mPlease wait a moment to install the script...')
    os.system('python2. __C__.py')


def cookie():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[1;92mThese Tools Use Python3 Language')
    jalan('       \x1b[1;92mPlease Be Patient Installing Materials...')
    os.system('pkg update && pkg upgrade')
    os.system('pkg install git curl python')
    os.system('pkg install ruby')
    os.system('gem install lolcat')
    os.system('termux-setup-storage')
    os.system('pip install mechanize requests bs4 futures')
    os.system('pip install colorama')
    os.system('python. __K__.py')


def kontol():
    os.system('clear')
    print logo
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    jalan('        \x1b[1;92mYou will be directed to Fb Page')
    os.system('xdg-open https://www.facebook.com/apki.James.baba007/')
    time.sleep(2)
    masuk()


def yayanxd():
    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mUpdating the Script ...\x1b[1;93m')
    os.system('git pull')
    raw_input('\n\x1b[1;94m{\x1b[1;97m<Press Enter To Continue>\x1b[1;94m}')
    os.system('python2 crack.py')


if __name__ == '__main__':
    pertanyaan()
