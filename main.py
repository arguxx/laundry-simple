from user import get_user_details, greeting
from transaction import process_transaction
from utils import print_divider

def main():
    print("Selamat datang di 03 Coin Laundry")
    weight, name, phone_number = get_user_details()
    print_divider()
    greeting(name)
    process_transaction(weight, name, phone_number)

if __name__ == "__main__":
    main()
