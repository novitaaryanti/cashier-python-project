# Super Cashier Project



## A. Background
Super Cashier is a self-service cashier project written in Python. The main goal of this project is to make a system for customers to check out their items after they are done shopping. By providing this self-service cashier system, customers can shop more conveniently.

**Note:** The project's interface is in Indonesian



## B. Objectives
This project is built to implement Object-Oriented Programming (OOP) concepts in Python and the coding best practices in Python, such as defensive programming.



## C. Requirements & Program Flow
This program contains two modules, which are `main.py` and `transaction.py`
1. Module `main.py` includes function `main()` as the main menu of the program, function `menu()` as the transaction menu, and function `get_txn_id()` to generate the transaction ID.
2. Modul `transaction.py` includes all functions to do the task of transaction menu features:
   - Function `add_item()`: add new item into the transaction
   - Function `update_item_name()`: change the item's name which has been added previously in the transaction
   - Function `update_item_qty()`: change the item's quantity which has been added previously in the transaction
   - Function `update_item_price()`: change the item's price which has been added previously in the transaction
   - Function `delete_item()`: delete specific item which has been added previously in the transaction
   - Function `reset_transaction()`: delete all item which has been added previously in the transaction
   - Function `check_order()`: display all items that have been added to the transaction
   - Function `checkout()`: determine whether the customer can check out the transaction

### 1. Create a new transaction cart and generate the transaction ID
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/5ce088fb-19d2-4934-b037-463d424155bd)

Every transaction is unique. To maintain the record of transactions, the program will generate the ID of each transaction using the function `get_txn_id()`. While generating the transaction ID, the program will provide a cart by initializing an object from the module `transaction.py` for the customer to input the items they want to buy. Both will be done in module `main.py`. 

After that, the customer will be directed to the transaction menu by calling the function `menu()`. There are several options which could be chosen by the customers to maintain their items in the cart and to do the checkout process. Every option displays a confirmation of whether the function has successfully done its task, to re-confirm before doing the task, or if the customer gives the program the wrong input. This is also to present the implementation of a good user experience.
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/c1c3124d-6a5a-4c59-abe0-beb41d33c608)


### 2. Add the item's name, quantity, and price
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/eefa778c-7788-405b-8a63-53e47820111a)

The customer can add details of the item, including the name, quantity, and price of the item using the function `add_item()`. This function will also calculate the subtotal price of each item by multiplying the price with the quantity.

### 3. Change the item's name, quantity, or price
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/f0013424-a687-4472-8ab7-0730f805621e)

The customer can change the details of the item. To change the item's name, the customer can choose the option that will lead them to the function `update_item_name()`. To change the item's quantity, the customer can choose the option that will lead them to the function `update_item_qty()`. To change the item's price, the customer can choose the option that will lead them to the function `update_item_price()`.

### 4. Delete a specific item or all item
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/c992d0a7-335a-4641-8316-1db04f14b1c3)

The customer can delete an item or immediately delete all item(s) from the cart. To delete a specific item, the customer can choose the option that will lead them to the function `delete_item()`. To delete all item(s) in the cart, the customer can choose the option that will lead them to the function `reset_transaction()`.

### 5. Display the cart
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/4179daeb-a014-4c3e-bd74-7c68e4100321)

To help the customer do order-checking, the customer can choose the option that will lead them to the function `check_order()`. The cart display will also be provided every time the customer needs to input the details of a specific item to present the implementation of a good user experience as the functions in this program are mostly case-sensitive.

### 6. Display the total price of the transaction & the discount (if any)
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/527ef673-e3bd-4925-8c73-67168a8ac459)

The customer can automatically sum up the price of each item to determine the amount the customer needs to pay using the function `total_price()`. If the result of the sum-up meets a discount condition in which it reaches a point of the specific amount, then the program will automatically calculate the total price after it is reduced by the discount. The discount condition in this program:
| Minimum Total Price    | Discount      |
| ---------------------- | ------------- |
| Rp500.000,00           | 10%           |
| Rp300.000,00           | 8%            |
| Rp200.000,00           | 5%            |

### 7. Option to checkout or cancel the transaction
![image](https://github.com/novitaaryanti/cashier-python-project/assets/138101831/469d9a66-0421-46e4-99a4-48c018eddbde)

The program provides the option if the customer wants to proceed or cancel the transaction. The flow chart above explains the function `checkout()`, which is a simple determinator of whether the customer can proceed to check out the transaction. The customer can only check out if the cart is not empty. The option to check out or cancel the transaction is available in the function `menu()`.



## D. Test Cases

### Test 1: Add Item
#### a. Input several items into the transaction cart
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/a65185cb-d602-461c-a4c8-0b03ecbf20f8" width="500"/>
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/44a7ef36-a31d-4c30-a631-a66f7051ac82" width="500"/>

#### b. Display all items in the transaction cart
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/3682ffd4-85ea-4002-aac6-df5c61bce038" width="500"/>


### Test 2: Delete Item
#### a. Display all items in the transaction cart and delete "Pasta Gigi"
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/d1cd7dfc-f079-4851-aea3-d4a277fcbbaf" width="500"/>

#### b. Display all items in the transaction cart after the deletion
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/d14cb9b0-52fe-403c-a857-4c9a1acea1ac" width="500"/>



### Test 3: Delete All Item (Reset)
#### a. Display all items in the transaction cart and delete all items
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/ca44b86f-0360-431d-9e19-33c53cd9253f" width="500"/>

#### b. Display all items in the transaction cart after the deletion
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/b4e8e7e8-a3e6-4e58-b16b-b62c79348d2d" width="500"/>


### Test 4: Get The Total Price
#### a. Display all items in the transaction cart
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/69373080-d5f4-479c-a209-e89eb8688a52" width="500"/>

#### b. Display the discount (if meets the discount condition) and the total price
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/c0e772ff-0bc0-4a18-86be-3ac8db3f66a7" width="500"/>


### Test 5: Check Out
<img src="https://github.com/novitaaryanti/cashier-python-project/assets/138101831/928942b6-b872-48d8-abf2-c05b8ff94233" width="500"/>



## E. Conclusions
This project covers the minimum requirements of what a self-service cashier needs. As the interface of the program is in Indonesian, this project may be useful if this program is implemented in the supermarket which is based in Indonesia. There is room for improvisation as the program only covers the minimum requirements of a self-service cashier. One of the future works that can be done is connecting the program to the database. If it is connected to the database, the main menu of the program needs to be improved, especially for the function which generates the transaction ID.
