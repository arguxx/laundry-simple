import string
import random
from datetime import datetime

weight = int(input("Berat (dalam Kg) : "))
name = input("atas nama : ")
phone_number = input("nomer telpon : ")
status = "lunas"
bayar = int(input("Masukan Pembayaran : "))
diskon = 0
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def greeting(name):
    print("Kepada yang terhormat Bapak/ibu {}, terimakasih telah melakukan transaksi laundri di kios 03 Coin Laundry, berikut nota transaksi laundry Bapak/Ibu (emoji tangan sopan) : ".format(name))
def division():
    print("---------------")
def head():
    print("03 Coin Laundry\n08123456789\nJl. Sukabirus No.66 Citeureup, Kec. Dayeuhkolot, Kota Bandung, Jawa Barat 40257, Indonesia")
def user(name, phone_number):
    print("Pelanggan : ", name)
    print ("No. Telp : ", phone_number)
def stats(status):
    print("Status : ", status)
    nota = 8
    print_nota = "".join(random.choices(string.ascii_uppercase + string.digits, k = nota))
    print("No. Nota : " + str(print_nota))
    dt = datetime.now()
    dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")
    print("Tgl. Transaksi : ", dt_string)
def detail():
    print("Detail Pesanan : ")
def total(weight, diskon, bayar):
    harga = weight * 5000
    kembali = bayar - harga - diskon
    print("Diskon : ", diskon)
    print("Total : ", harga)
    print("BAYAR : ", bayar)
    print("Kembali : ", kembali)
def estimasi():
    print("1 Hari")
def Karyawan():
    print("kuda")
def catatan():
    print("Catatan : jujur pengen punya pacar")
def sk():
    print("Syarat Ketentuan")
def online():
    print("Nota online dapat dilihat di : instagram.com/argianrp_")


greeting(name)
division()
head()
division()
user(name, phone_number)
division()
stats(status)
division()
detail()
division()
total(weight, diskon, bayar)
division()
estimasi()
division()
Karyawan()
division()
catatan()
division()
sk()
division()
online()
