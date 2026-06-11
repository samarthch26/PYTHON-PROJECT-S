"""
STORE MANAGEMENT SYSTEM
Entity:-
Customer  ( cid,cname,cadd,cmob )
Product   (pid,pname,price,pdesc)
Orders    ( cid , pid , qty)
Menu Options:-
1. Add Customer
2. View All Customers
3. Delete A Customer
4. Add Product
5. View All Products
6. Update Price Of A Product
7. Place An Order
8. View All Orders
9. View Orders By CID
0. Exit

"""
# IMPORTING REQUIRED LIBRARIES
import pickle

# A METHOD TO ADD A CUSTOMER INFORMATION
def addCustomer():
    cid = input("\n\t    Enter Customer ID : ")
    cname = input("\t    Enter Customer Name : ")
    cadd = input("\t    Enter Customer Address : ")
    cmob = input("\t    Enter Customer Mobile : ")
    cus = {cid:[cname,cadd,cmob]}
    file = open('customer.bin','ab')
    pickle.dump(cus,file)
    file.close()
    print("\n\t    Customer Addedd Successfully!")

# A METHOD TO VIEW ALL CUSTOMERS
def viewCustomers():
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            for cid,detail in data.items():
                print("\n\t    Customer ID :",cid)
                print("\t    Customer Name :",detail[0])
                print("\t    Customer Address :",detail[1])
                print("\t    Customer Mobile :",detail[2])
    except:
        print("\n\t    Here is all your customers")
    file.close()

# A METHOD TO DELETE A CUSTOMER
def deleteCustomer():
    file = open('customer.bin','rb')
    cid = input("Enter Customer ID To Delete : ")
    cus = dict()
    try:
        while True:
            data = pickle.load(file)
            cus.update(data)
    except:
        pass
    file.close()
    try:
        cus.pop(cid)
        file = open('customer.bin','wb')
        for data in cus.items():
            pickle.dump({data[0]:data[1]},file)
        file.close()
        print("\n\t    Customer Deleted Successfully!")
    except:
        print("\n\t    Customer Not Found!")

# A METHOD TO ADD A PRODUCT INFORMATION
def addProduct():
    file = open('product.bin','ab')
    pid = input("\n\t    Enter Product ID : ")
    pname = input("\t    Enter Product Name : ")
    price = input("\t    Enter Product Price : ")
    pdesc = input("\t    Enter Product Description : ")
    data = {pid:[pname,price,pdesc]}
    pickle.dump(data,file)
    print("\n\t    Product Addedd Successfully!")
    file.close()

# A METHOD TO VIEW ALL PRODUCTS
def viewProducts():
    file = open('product.bin' , 'rb')
    try:
        print("\n\tPID\tPname\tPrice\tAbout Product")
        while True:
            data = pickle.load(file)
            for pid,data in data.items():
                print(f"\t{pid}\t{data[0]}\t{data[1]}\t{data[2]}")
    except:
        print("\n\t    Here is your all products...")
    file.close()

# A MEHTOD TO UPDATE THE PRICE OF A PRODUCT
def updatePrice():
    file = open('product.bin','rb')
    pro = dict()
    try:
        while True:
            pro.update( pickle.load(file) )
    except:
        pass
    file.close()
    pid = input("\n\t    Enter Product ID To Update Price : ")
    if pro.get(pid,False):
        print("\n\t    Product Name :",pro[pid][0])
        print("\t    Product Old Price :",pro[pid][1])
        price = input("\t    Enter New Price : ")
        pro.update({pid:[pro[pid][0],price,pro[pid][2]]})
        file = open('product.bin','wb')
        for row in pro.items():
            pickle.dump({row[0]:row[1]},file)
        file.close()
        print("\n\t    Product Price Updated!")
    else:
        print("\n\t    Product ID Not Found!")

# A METHOD TO GET CUSTOMER INFO USING CID
def getCustomer(cid):
    file = open('customer.bin','rb')
    cus = dict()
    try:
        while True:
            data = pickle.load(file)
            if list(data.keys())[0]==cid:
                cus.update(data)
    except:
        pass
    file.close()
    return cus
    
# A METHOD TO GET PRODUCT INFO USING PID
def getProduct(pid):
    file = open('product.bin','rb')
    pro = dict()
    try:
        while True:
            data = pickle.load(file)
            if list(data.keys())[0]==pid:
                pro.update(data)
    except:
        pass
    file.close()
    return pro

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\t    Enter Customer ID : ")
    cus = getCustomer(cid)
    if len(cus)!=0:
        print("\t    Customer Name :",cus[cid][0])
        print("\t    Customer Address :",cus[cid][1])
        pid = input("\t    Enter Product ID : ")
        pro = getProduct(pid)
        if len(pro)!=0:
            print("\t    Product Name :",pro[pid][0])
            print("\t    Product Price :",pro[pid][1])
            qty = input("\t    Enter Quantity : ")
            print("\t    Total Bill :",float(pro[pid][1])*float(qty))
            file = open('orders.bin','ab')
            data = [cid,pid,qty]
            pickle.dump(data,file)
            file.close()
            print("\n\t    Order Placed Successfully!")
        else:
            print("\n\t    Product Not Found on This ID")
    else:
        print("\n\t    Customer Not Found on This ID")

# A METHOD TO VIEW ALL ORDERS
def viewAllOrders():
    file = open("orders.bin",'rb')
    i = 1000
    try:
        while True:
            i += 1
            data = pickle.load(file)
            cus = getCustomer( data[0] )
            pro = getProduct( data[1] )
            qty = data[2]
            print("\n\tOrder No.",i)
            print("\t    Customer Name :",cus[data[0]][0])
            print("\t    Customer Address :",cus[data[0]][1])
            print("\t    Customer Mobile :",cus[data[0]][2])
            print("\t    Product Name :",pro[data[1]][0])
            print("\t    Product Price :",pro[data[1]][1])
            print("\t    About Product :",pro[data[1]][2])
            print("\t    Quantity :",qty)
            print("\t    Total Bill :",float(pro[data[1]][1])*float(qty))
            print("\t    --------------------------------")
    except:
        print("\n\t    Here is your all orders.")
    file.close()

# A METHOD TO VIEW ORDERS OF A PARTICULAR CUSTOMER BY CID
def viewOrdersByCID():
    file = open("orders.bin",'rb')
    cid = input("\n\t    Enter Customer ID : ")
    i = 1000
    try:
        while True:
            data = pickle.load(file)
            if data[0]==cid:
                i += 1
                cus = getCustomer( data[0] )
                pro = getProduct( data[1] )
                qty = data[2]
                print("\n\tOrder No.",i)
                print("\t    Customer Name :",cus[data[0]][0])
                print("\t    Customer Address :",cus[data[0]][1])
                print("\t    Customer Mobile :",cus[data[0]][2])
                print("\t    Product Name :",pro[data[1]][0])
                print("\t    Product Price :",pro[data[1]][1])
                print("\t    About Product :",pro[data[1]][2])
                print("\t    Quantity :",qty)
                print("\t    Total Bill :",float(pro[data[1]][1])*float(qty))
                print("\t    --------------------------------")
    except:
        print("\n\t    Here is your all orders.")
    file.close()
   
# DASHBOARD
while True:
    print("\n\t    STORE MANAGEMENT SYSTEM")
    print('''
            1. Add Customer
            2. View All Customers
            3. Delete A Customer
            4. Add Product
            5. View All Products
            6. Update Price Of A Product
            7. Place An Order
            8. View All Orders
            9. View Orders By CID
            0. Exit
    ''')
    ch = int(input("\t    Enter Your Choice : "))
    if ch==0:
        print("\n\t\tTHANK YOU!")
        break
    elif ch==1:
        addCustomer()
        input("\t    Press Enter To Continue...")
    elif ch==2:
        viewCustomers()
        input("\t    Press Enter To Continue...")
    elif ch==3:
        deleteCustomer()
        input("\t    Press Enter To Continue...")
    elif ch==4:
        addProduct()
        input("\t    Press Enter To Continue...")
    elif ch==5:
        viewProducts()
        input("\t    Press Enter To Continue...")
    elif ch==6:
        updatePrice()
        input("\t    Press Enter To Continue...")
    elif ch==7:
        placeAnOrder()
        input("\t    Press Enter To Continue...")
    elif ch==8:
        viewAllOrders()
        input("\t    Press Enter To Continue...")
    elif ch==9:
        viewOrdersByCID()
        input("\t    Press Enter To Continue...")
    else:
        input("\n\t    Wrong Entered!\n")
        input("\t    Press Enter To Continue...")
