from utils import print_divider

def get_user_details():
    weight = int(input("Berat (dalam Kg): "))
    name = input("Atas nama: ")
    phone_number = input("Nomor telpon: ")
    return weight, name, phone_number

def display_user_info(name, phone_number):
    print(f"Pelanggan: {name}")
    print(f"No. Telp: {phone_number}")

def greeting(name):
    print_divider('=')
    print(f"Kepada yang terhormat Bapak/Ibu {name},")
    print("Terima kasih telah melakukan transaksi laundry di kios 03 Coin Laundry.")
    print_divider('-')