from tabulate import tabulate


class Transaction:
    def __init__(self):
        """
        Method for making new transaction in the class Transaction.

        :order_info: dictionary which stores item data (including the details) in the transaction
        """

        self.order_info = dict()

    def check_order(self):
        """
        Function used to display all items that have been previously added in the transaction

        :return: display details of all items in the transaction
        """

        if len(self.order_info) == 0:
            return print("""
            ===== KERANJANG KOSONG =====
            """)
        else:
            item_details = [[i + 1, name] + details for i, (name, details) in enumerate(self.order_info.items())]

            table_head = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]

            # Display confirmation that all items added is in accordance with the system
            print("""
            Info!
            Seluruh detail pesanan yang Anda masukkan sudah sesuai dengan sistem!
            """)
            # Display details of all items in the transaction
            return print(tabulate(item_details, headers=table_head, tablefmt="grid"))

    def add_item(self, name, qty, price):
        """
        Function used to add new item (including the details) in the transaction

        :param name: string which stores the item name of the added item
        :param qty: integer which stores the item quantity of the added item
        :param price: float which stores  the item price of the added item
        :return: display confirmation that the item has been succesfully added
        """

        # Add the item detail into the dictionary
        # The item detail's format: key = nama; value = quantity, harga, total harga
        # Total harga = quantity * harga item
        self.order_info.update({name: [qty, price, (lambda q, p: q * p)(qty, price)]})

        # Display confirmation that the item has been succesfully added (including the details item)
        return print("""
        BERHASIL!
        Item berikut sudah masuk ke dalam keranjang
        Nama Item   : {}
        Jumlah Item : {}
        Harga Item  : Rp{:.2f}
        """.format(name, qty, price))

    def update_item_name(self, name_old, name_new):
        """
        Function used to change the name of the item

        :param name_old: string which stores the name of the item that is going to be changed
        :param name_new: string which stores the new name of the item
        :return: display confirmation that the item's name has been succesfully changed
        """

        # Temporary store the details of the item (excluding the name) which is going to be changed
        temp = self.order_info[name_old]

        # Delete the data (including the details) with the old name from the transaction
        # Followed by adding new data using the details that already stored in the temporary variable
        # New data = key: name_new, value = temp
        self.order_info.pop(name_old)
        self.order_info.update({name_new: temp})

        # Display confirmation that the item's name has been succesfully changed
        return print("""
        BERHASIL!
        Nama item "{}" telah diubah menjadi "{}"
        """.format(name_old, name_new))

    def update_item_qty(self, name, qty_new):
        """
        Function used to change the quantity of the item

        :param name: string which stores the name of the item that is going to be changed
        :param qty_new: integer which stores the new quantity of the item
        :return: display confirmation that the item's quantity has been succesfully changed
        """

        # Change the item's quantity and the item's total price from the value list for the intended item
        # Both are accessed based on the index where each detail is stored in the value list of the item:
        # order_info[name][0] = quantity of the item in this transaction
        # order_info[name][2] = item total price = price * quantity
        self.order_info[name][0] = qty_new
        self.order_info[name][2] = (lambda q, p: q * p)(qty_new, self.order_info[name][1])

        # Display confirmation that the item's quantity has been succesfully changed
        return print("""
        BERHASIL!
        Jumlah item "{}" dalam keranjang telah diubah menjadi {} buah
        """.format(name, qty_new))

    def update_item_price(self, name, price_new):
        """
        Function used to change the price of the item

        :param name: string which stores the name of the item that is going to be changed
        :param price_new: float which stores the new price of the item
        :return: display confirmation that the item's price has been succesfully changed
        """

        # Change the item's price and the item's total price from the value list for the intended item
        # Both are accessed based on the index where each detail is stored in the value list of the item:
        # order_info[nama_item][1] = price of the item in this transaction
        # order_info[nama_item][2] = item total price = price * quantity
        self.order_info[name][1] = price_new
        self.order_info[name][2] = (lambda q, p: q * p)(self.order_info[name][0], price_new)

        # Display confirmation that the item's price has been succesfully changed
        return print("""
        BERHASIL!
        Harga item "{}" telah diubah menjadi Rp{:.2f}
        """.format(name, price_new))

    def delete_item(self, name):
        """
        Function used to delete specific item from the transaction

        :param name: string which stores the name of the item that is going to be deleted
        :return: display confirmation that the item has been succesfully deleted
        """

        # Delete the details of the specific item from the transaction
        self.order_info.pop(name)

        # Display confirmation that the specific item has been succesfully deleted
        return print("""
        BERHASIL!
        Item "{}" telah dihapus dari keranjang
        """.format(name))

    def reset_transaction(self):
        """
        Function used to delete all item from the transaction

        :return: display confirmation that the all item has been succesfully deleted
        """

        # Delete the details of the all item from the transaction
        self.order_info.clear()

        # Display confirmation that all item has been succesfully deleted
        return print("""
        BERHASIL!
        Semua item dalam keranjang telah dihapus
        """)

    def total_price(self):
        """
        Function used to calculate and display the total price of the transaction
        (including discount, if any)

        :return: Display the total price and discount (if any)
        """

        # Set total = 0 as a starting point before add up all the item's total price
        total = 0

        # Add up all the item's total price
        for price in self.order_info:
            total += self.order_info[price][2]

        # If the total price of the transaction is more than Rp500.000,00,
        # the total price is reduced by 10% discount
        if total > 500_000:
            total = (lambda t, d: t - (t * d))(total, 0.10)
            print("""
            Anda mendapatkan diskon 10% atas pembelian di atas Rp500.00,00
            Total belanja Anda setelah dipotong diskon Rp{:.2f}
            """.format(total))
        # If the total price of the transaction is more than Rp300.000,00,
        # the total price is reduced by 8% discount
        elif total > 300_000:
            total = (lambda t, d: t - (t * d))(total, 0.08)
            print("""
            Anda mendapatkan diskon 8% atas pembelian di atas Rp300.000,00
            Total belanja yang harus dibayarkan adalah Rp{:.2f}
            """.format(total))
        # If the total price of the transaction is more than Rp200.000,00,
        # the total price is reduced by 5% discount
        elif total > 200_000:
            total = (lambda t, d: t - (t * d))(total, 0.05)
            print("""
            Anda mendapatkan diskon 5% atas pembelian di atas Rp200.000,00
            Total belanja yang harus dibayarkan adalah Rp{:.2f}
            """.format(total))
        # If the total price of the transaction is equal or less than Rp200.000,00,
        # the total price is normal
        else:
            print("""
            Total belanja yang harus dibayarkan adalah Rp{:.2f}
            """.format(total))

    def checkout(self):
        if len(self.order_info) == 0:
            return 0
        else:
            return 1
