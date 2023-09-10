from transaction import *
import datetime
import random


def get_txn_id():
    """
    Function used to get transaction ID
    Format transaction ID: TRddmmyy-xxx
    - TR: 2 required character in the beginning of ID
    - dd: 2 digit based on transaction date [01-31]
    - mm: 2 digit based on transaction month [01-12]
    - yy: 2 digit based on transaction year (without century)
    - xxx: 3 digit random number

    :return: string which represents transaction ID in format TRddmmyy-xxx
    """
    curr_date = datetime.datetime.now()
    txn_id = "TR{}-{:03d}".format(curr_date.strftime("%d%m%y"), random.randint(0, 999))

    return txn_id


def menu(txn):
    """
    Showing the available menu option and choosing the menu during the transaction

    :param txn: dictionary from the ongoing transaction
    """

    # Display the available menu option
    print("""
    MENU:
    1. Tambah Item
    2. Ubah Nama Item
    3. Ubah Jumlah Item
    4. Ubah Harga Item
    5. Hapus Item
    6. Hapus Semua Item
    7. Cek Keranjang Belanja
    8. Hitung Total Belanja
    9. Check-out
    0. Batal
    """)

    # Get the menu option from user
    # Loop until the user chooses between option in range of 0 to 9
    while True:
        try:
            opt = int(input("Pilihan menu [0-9]: "))
            if opt < 0 or opt > 9:
                print("Pilihan menu tidak tersedia!")
            else:
                break
        except ValueError:
            print("Jumlah item harus berupa angka bulat!")

    # Option 1: Tambah Item
    # Adding new item into the transaction
    if opt == 1:
        try:
            # Get the item's name from user
            item_name = input("Masukkan nama item yang hendak dipesan: ")

            # Get the quantity of the item from user
            # Loop to make sure that the inputted quantity is in integer type
            while True:
                try:
                    item_qty = int(input("Masukkan jumlah item yang hendak dipesan: "))
                except ValueError:
                    print("Jumlah item harus berupa angka bulat!")
                else:
                    break

            # Get the price of the item from user
            # Loop to make sure that the inputted price is in float type
            while True:
                try:
                    item_price = float(input("Masukkan harga item yang hendak dipesan: "))
                except ValueError:
                    print("Harga item harus berupa angka bulat atau desimal!")
                else:
                    break

            # Call add_item function
            txn.add_item(item_name, item_qty, item_price)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 2: Ubah Nama Item
    # Change the item name which has been added previously in the transaction
    elif opt == 2:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()

            # Get the item's name which is going to be changed from user
            item_name = input("Masukkan nama item yang hendak diubah [case sensitive]: ")

            # Get the new name for the item from user
            name_new = input("Masukkan nama baru item: ")

            # Call function update_item_name() to change the name of the item
            txn.update_item_name(item_name, name_new)
        except KeyError:
            print("""
            GAGAL!
            Data item tidak tersedia!
            """)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 3: Ubah Jumlah Item
    # Change the quantity of the item which has been added previously in the transaction
    elif opt == 3:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()

            # Get the item's name which is going to be changed from user
            item_name = input("Masukkan nama item yang jumlahnya hendak diubah [case sensitive]: ")

            # Get the new quantity of the item from user
            # Loop to make sure that the inputted quantity is in integer type
            while True:
                try:
                    qty_new = int(input("Masukkan jumlah baru item: "))
                except ValueError:
                    print("Jumlah item harus berupa angka bulat!")
                else:
                    break

            # Call function update_item_qty() to change the quantity of the item
            txn.update_item_qty(item_name, qty_new)
        except KeyError:
            print("""
            GAGAL!
            Data item tidak tersedia!
            """)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 4: Ubah Harga Item
    # Change the item's price which has been added previously in the transaction
    elif opt == 4:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()

            # Get the item's name which is going to be changed from user
            item_name = input("Masukkan nama item yang jumlahnya hendak diubah [case sensitive]: ")

            # Get the new price of the item from user
            # Loop to make sure that the inputted price is in float type
            while True:
                try:
                    price_new = float(input("Masukkan jumlah baru item: "))
                except ValueError:
                    print("Harga item harus berupa angka bulat atau desimal!")
                else:
                    break

            # Call function update_item_price() to change the price of the item
            txn.update_item_price(item_name, price_new)
        except KeyError:
            print("""
            GAGAL!
            Data item tidak tersedia!
            """)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 5: Hapus Item
    # Delete specific item which has been added previously in the transaction
    elif opt == 5:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()

            # Get the item's name which is going to be deleted from user
            item_name = input("Masukkan nama item yang hendak diubah [case sensitive]: ")

            # Call function delete_item() to delete the specific item
            txn.delete_item(item_name)
        except KeyError:
            print("""
            GAGAL!
            Data item tidak tersedia!
            """)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 6: Hapus Semua Item
    # Delete all item which has been added previously in the transaction
    elif opt == 6:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()

            while True:
                # Ask for confirmation from user before deleting all items
                choice = input("Anda yakin ingin menghapus semua item dalam keranjang [Y/N]: ")

                # If yes, then all item in the transaction will be deleted
                if choice in ['Y', 'y']:
                    txn.reset_transaction()
                    break
                # Else if no, then user will be directed back to the main menu of the transaction
                elif choice in ['N', 'n']:
                    break
                else:
                    print("Opsi yang Anda masukkan tidak ada dalam pilihan!")
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 7: Cek Keranjang Belanja
    # Display all items that have been added in the transaction
    elif opt == 7:
        try:
            # Call function check_order() to display all items that have been added in the transaction
            txn.check_order()
        except ValueError or KeyError or TypeError:
            print("""
            TERDAPAT KESALAHAN INPUT
            """)
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 8: Hitung Total Belanja
    # Calculate and display the total price of the transaction (including discount, if any)
    elif opt == 8:
        try:
            # Call total_price() to calculate total price of the transaction & discount (if any)
            # Followed by displaying the total price which the user has to pay
            txn.total_price()
        finally:
            # Display confirmation to get back to the main menu of the transaction
            input("Tekan tombol apa saja untuk melanjutkan >>")
            print("\n\n\n")
            menu(txn)

    # Option 9: Check-out
    # Checking-out the transaction
    elif opt == 9:
        # Call function check_order() to display all items that have been added in the transaction
        txn.check_order()

        # Get flag (0 or 1) by calling checkout() function
        # 0 indicating that there is no item inputted yet in the transaction
        # 1 indicating that there is at least one item inputted in the transaction
        flag = txn.checkout()

        # If there is item(s) in the transaction, the user can check out
        if flag == 1:
            while True:
                # Call total_price() to calculate total price of the transaction & discount (if any)
                # Followed by displaying the total price which the user has to pay
                txn.total_price()

                # Ask for confirmation from user before doing check-out
                choice = input("Apakah Anda ingin melakukan checkout? [Y/N]: ")

                # If yes, then transaction is processed
                if choice in ['Y', 'y']:
                    return print("""
                    BERHASIL!
                    Transaksi Anda telah berhasil

                    Terima kasih telah berbelanja di Supermarket XYZ
                    """)
                # Else if no, then the check-out is not processed
                # User will be directed back to the main menu of transaction
                elif choice in ['N', 'n']:
                    menu(txn)
                else:
                    print("Opsi yang Anda masukkan tidak ada dalam pilihan!")
        else:
            print("""
            Anda perlu memasukkan item untuk bisa melakukan checkout!
            """)

        # Display confirmation to get back to the main menu of the transaction
        input("Tekan tombol apa saja untuk melanjutkan >>")
        print("\n\n\n")
        menu(txn)

    # Option 0: Batal
    # An option if the user intends to cancel the transaction
    else:

        while True:
            # Ask for confirmation from user before doing the cancellation
            choice = input("Apakah Anda ingin membatalkan transaksi? [Y/N]: ")

            # If yes, then transaction is cancelled
            if choice in ['Y', 'y']:
                return print("""
                Transaksi Anda dibatalkan!
                """)
            # Else if no, then the user will be directed back to the main menu of transaction
            elif choice in ['N', 'n']:
                menu(txn)
            else:
                print("Opsi yang Anda masukkan tidak ada dalam pilihan!")


def main():
    """
    Function that acts as the entry point of the supermarket's self-service program
    User (customer) will get a transaction ID before doing the transaction
    """

    # Displaying the welcome message
    print("""
    *** SELAMAT DATANG DI SUPERMARKET XYZ ***
    """)

    # Call get_txn_id() function to get transaction ID
    input("Tekan tombol apa saja untuk mendapatkan kode transaksi >>")
    print("""
    ID transaksi Anda = {}
    """.format(get_txn_id()))

    input("Tekan tombol apa saja untuk mulai berbelanja >>")
    print("\n\n\n")
    # Create new object transaction by calling Transaction() class
    trnsct_123 = Transaction()
    # Call menu() function to go to the transaction menu
    menu(trnsct_123)

    while True:
        # Ask whether the user want to do another transaction
        choice = input("Apakah Anda ingin melakukan transaksi lain? [Y/N]: ")
        # If yes, then the user will be back to the beginning of main() function
        if choice in ['Y', 'y']:
            main()
        # Else if no, then the user will be directed to quit the program
        elif choice in ['N', 'n']:
            break
        else:
            print("Opsi yang Anda masukkan tidak ada dalam pilihan!")

    # Display message saying thank you
    print("""
    *** TERIMA KASIH ATAS KUNJUNGANNYA ***
    """)


if __name__ == "__main__":
    main()
