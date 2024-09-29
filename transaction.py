import string
import random
from datetime import datetime
from utils import print_divider

def get_random_nota(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def calculate_total(weight, diskon, bayar):
    harga = weight * 5000
    total_bayar = harga - diskon
    kembali = bayar - total_bayar
    return harga, kembali

def process_transaction(weight, name, phone_number):
    status = "lunas"
    bayar = int(input("Masukkan Pembayaran: "))
    diskon = 0

    nota = get_random_nota()
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"Status: {status}")
    print(f"No. Nota: {nota}")
    print(f"Tgl. Transaksi: {current_time}")

    total_harga, kembali = calculate_total(weight, diskon, bayar)
    print(f"Diskon: {diskon}")
    print(f"Total: {total_harga}")
    print(f"BAYAR: {bayar}")
    print(f"Kembali: {kembali}")
    print_divider()
