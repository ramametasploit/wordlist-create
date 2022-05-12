import requests, os
import sys
import itertools
import threading
import time
import sys
sleep = time.sleep


blue="\033[34;1m"
green="\033[32;1m"
purple="\033[35;1"
cyan="\033[ 36;1m"
merah="\033[31;1m"
putih="\033[37;1m"
kuning="\033[1;33m"

os.system("clear")
os.system("figlet wordlist")
print
print (merah+'Author   : etichal heker')
print (merah+'Team     : mct')
print (putih+'Test     : localhost:8080')
print (putih+'youtube  : rama metasploit')
print 
print (green+'__________________________________________________')
print
print
print ("pilih menu anda")
print
print ("1.menambahkan diawal wordlist")
print ("2.menambahkan diakhir wordlist")
print ("3.batalkan dan keluar")
print 
pilih = raw_input("pilihan =>>")

if pilih == '1':
    os.system("clear")
file = raw_input(kuning+"your file id --> ")
file = open(file, "r")
text = raw_input("text: ")
for buka in file.readlines():
    buka = buka.strip("\n").strip("\r")
    print (text+(putih+"" +buka))
print
print ("wordlist anda sukses dibuat copy paste untuk kombinasi yang akurat")
print
sys.exit()

if pilih == '2':
    os.system("clear")
file = raw_input(kuning+"your file id --> ")
file = open(file, "r")
text = raw_input("text: ")
for buka in file.readlines():
    buka = buka.strip("\n").strip("\r")
    print ((putih+"" +buka)+text)
    sys.exit()