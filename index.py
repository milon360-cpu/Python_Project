# from admin import username
import re
import os
import time
import mysql.connector

# Database connection 
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="phoneshop"
)
# Main Menu section here 

def mainMenu():
    os.system('cls')
    print("{:>60}".format("*************************************"))
    print("{:>51}".format(f"WELCOME {username}"))
    print("{:>60}".format("*************************************\n"))
    print("1. Add Product")
    print("2. Find Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Show All Product")
    print("6. Logout")
    value = input("Please Enter value between 1 and 6:\t")
    if value == '1': 
        addNewProduct()
    elif value == '2':
       findProduct()
    elif value == '3':
        updateProduct()
    elif value == '4':
        deleteProduct()
    elif value == '5':
        showAllProduct()
    elif value == '6':
        adminMenu()
    else:
        os.system('cls')
        print("Error!! Invalid Input")
        input("Press any key for continue...")
        mainMenu()
# Main Menu section End here 


##########################################################################
# Admin Login and Registration section Started here
def adminMenu():
    os.system("cls")
    print("{:>60}".format("********************************************"))
    print("{:>51}".format("ADMIN LOGIN AND REGISTRATION"))
    print("{:>60}".format("********************************************\n"))
    print("1. Login")
    print("2. Registration")
    print("3. Exist")
    value = input("Please Enter Value 1 or 2 or 3:\t")
    if value == '1':
      loginAdmin()
    elif value == '2':
      registerUser()

    elif value == '3':
        os.system('cls')
        print(f"Thank You {username}")
        exit(1)
    else:
        os.system("cls")
        input("Invalid Input Press Any key for Continue ...")    
        adminMenu()

# Register User 
def registerUser():
     # Email Validation Pattern 
    pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{3}$"
    os.system("cls")
    print("{:>60}".format("*************************************"))
    print("{:>51}".format("ADMIN REGISTRATION"))
    print("{:>60}".format("*************************************\n"))


    # inside Register menu 
    print("1.Login")
    print("2.Exit")
    print("Press any key for Register...\t",end='')
    counter = input()
    if counter == '1':
        loginAdmin()
    elif counter == '2':
        os.system("cls")
        print(f"Thank You {username}")
        exit(1)
    else:
      os.system('cls')
      print("{:>60}".format("*************************************"))
      print("{:>51}".format("ADMIN REGISTRATION"))
      print("{:>60}".format("*************************************\n"))
      name = input("Please Enter Your Name:\t")
      email = input("Please Enter Your Email:\t")
      if re.search(pattern,email):
        cursor = db.cursor()
        cursor.execute("""SELECT email FROM admin WHERE email = %s;""", (email,))
        result = cursor.fetchone()  
        flag = 0
        if result:
            flag = 1
    
            
        if flag == 0:
            password = input("Please Enter Your Password:\t")
            sql = "INSERT INTO admin (name, email, password) VALUES (%s, %s, %s)"
            val = (name,email,password)
            cursor.execute(sql, val)
            db.commit()
            print("Registration Successfully")
            time.sleep(1)
            loginAdmin()
            
        else:
            print("User Already Exist")
            input("Press Any key for Continue...")
            registerUser()
      else:
          print("Invalid Email Address")
          input("Press Any key for Continue...")
          registerUser()
# Login User 
def loginAdmin():
    os.system("cls")
    print("{:>60}".format("********************************"))
    print("{:>50}".format("ADMIN LOGIN"))
    print("{:>60}".format("********************************\n"))

    # inside login menu 
    print("1.Registration")
    print("2.Exit")
    print("Press any key for Login...\t",end='')
    counter = input()
    if counter == '1':
        registerUser()
    elif counter == '2':
        os.system("cls")
        print("Thank You")
        exit(1)
    else:
        os.system("cls")
        print("{:>60}".format("********************************"))
        print("{:>50}".format("ADMIN LOGIN"))
        print("{:>60}".format("********************************\n"))
        email = input("Please Enter Your Email:\t")
        password = input("Please Enter Your Password:\t")
        cursor = db.cursor()
        cursor.execute("""SELECT email,password,name FROM admin WHERE email = %s;""", (email,))
        result = cursor.fetchall()  
        flag = 0
        try:
            if email == result[0][0] and password == result[0][1]:
                    
                    print("Loading...")
                    time.sleep(1)
                    print('Login Successfully')
                    global username
                    username = result[0][2]
                    time.sleep(1)                             
                    mainMenu()  
            else:
                print("Loading...")
                time.sleep(1)
                os.system('cls')
                print("Invalid Email or Password")
                input("Press Any key for Continue...")
                loginAdmin()        
        except IndexError:
            print("Loading...")
            time.sleep(1)
            os.system('cls')
            print("Invalid Email or Password")
            input("Press Any key for Continue...")
            loginAdmin()
    
# Admin Login and Registration section End here
#######################################################################

#######################################################################
# Add Product section started here 
def addNewProduct():
    os.system('cls')
    print("{:>60}".format("*************************************"))
    print("{:>51}".format("ADD NEW PRODUCT"))
    print("{:>60}".format("*************************************\n"))
    cursor = db.cursor()

    print("0.Go Back")
    value = input("Press any key for continue:\t")
    if value == '0':
        mainMenu()
    else:
        os.system('cls')
        print("{:>60}".format("*************************************"))
        print("{:>51}".format("ADD NEW PRODUCT"))
        print("{:>60}".format("*************************************\n"))

        productId = input("Product ID:")
        cursor.execute("""SELECT productId FROM product WHERE productId = %s;""", (productId,))
        result = cursor.fetchone()
        flag = 0
        if result:
            flag = 1
        if flag == 0:
            productName = input("Product Name:\t")
            brandName = input("Brand Name:\t")
            price = input("Price:\t")
            display = input("Display Size:\t")
            memory = input("ROM:\t")
            ram = input("RAM:\t")
            camera = input("Camera:\t")
            battery = input("Battery:\t")

            
            sql  = "INSERT INTO product(productid, productname, barandname, price, display, memonry, ram, camera, battery)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value = (productId,productName,brandName,price,display,memory,ram,camera,battery)
            cursor.execute(sql,value)
            db.commit()
            os.system('cls')
            print("Added Successfully")
            print("1. Add more product")
            print("2. Go Back")
            print("Press any for exit")
            value = input("Please Enter:\t")
            if value == '1':
                os.system('cls')
                addNewProduct()
                os.system('cls')
            elif value == '2':
                mainMenu()
            else:
                os.system('cls')
                print(f"Thank You {username}")
                exit(1)
        else:
            print("This id already exist")
            input("Any key for continue...")
            os.system('cls')
            addNewProduct()

# Add Product section end here 
#######################################################################


# Find Product section Started here 
#######################################################################
def findProduct():
    os.system('cls')
    cursor = db.cursor()

    # find product header 
    def findProductHeader():
       print("{:>60}".format("*************************************"))
       print("{:>51}".format("FIND YOUR PRODUCT"))
       print("{:>60}".format("*************************************\n"))

    # print the all phone info 
    def printPhoneDetails(result):
        if result:
            print("ID:\t\t\t",result[0])
            print("Name:\t\t\t",result[1])
            print("Brand Name:\t\t",result[2])
            print("Price:\t\t\t",result[3]," BDT")
            print("Display:\t\t "+result[4]+" Inch")
            print("ROM:\t\t\t",result[5]," GB")
            print("RAM:\t\t\t",result[6]," GB")
            print("Camera:\t\t\t",result[7]," MP")
            print("Battery:\t\t",result[8]," mAh")
            input("\n\nPress any key for continue...")
            findProduct()
        else:
            os.system('cls')
            findProductHeader()
            print("Product Not found")
            input("\nPress any for continue...")
            findProduct()
    findProductHeader()
    print("1. Find by ID")
    print("2. Find by Product Name")
    print("3. Find by Brand Name")
    print("4. Find by Price Range")
    print("5. Go Back")
    value = input("Please Enter Your Value Between 1 and 4:\t")

    if value == '1':
        os.system('cls')
        findProductHeader()
        print("0.Go Back")
        value = input("Press any key for continue...\t")
        os.system('cls')
        if value == "0":
            findProduct()
        else:
            os.system('cls')
            findProductHeader()
            id = input("Please Enter Product ID:\t")
            cursor.execute("""SELECT * FROM product WHERE productid = %s;""", (id,))
            result = cursor.fetchone()
            printPhoneDetails(result)

    elif value == '2':
        os.system('cls')
        findProductHeader()
        print("0.Go Back")
        value = input("Press any key for continue...\t")
        os.system('cls')
        if value == "0":
            findProduct()
        else: 
            findProductHeader()
            productname = input("Please Enter Product Name:\t")
            cursor.execute("""SELECT * FROM product WHERE productname = %s;""", (productname,))
            result = cursor.fetchall()
            counter = 0
            if result:
                for x in result:
                    print(x)
                    counter = counter + 1
                print(f"\n\nTotal {productname} :\t",counter)
                input("\npress any key for continue...")
                findProduct()
            else:
                input("Invalid product Name! Press any key for continue...")
                findProduct()

    elif value == '3':
        os.system('cls')
        findProductHeader()
        print("0.Go Back")
        value = input("Press any key for continue...\t")
        os.system('cls')
        if value == "0":
            findProduct()
        else:
            findProductHeader()
            brandName = input("Please Enter Brand Name:\t")
            cursor.execute("""SELECT * FROM product WHERE barandname = %s;""", (brandName,))
            result = cursor.fetchall()
            counter = 0
            if result:
                for x in result:
                    print( x)
                    counter = counter + 1
                print("\n\nTotal Product:\t",counter)
                input("\npress any key for continue...")
                findProduct()
            else:
                input("Invalid Brand Name! Press any key for continue...")
                findProduct()
       
    elif value == '4':
        os.system('cls')
        findProductHeader()
        print("0.Go Back")
        value = input("Press any key for continue...:\t")
        os.system('cls')
        if value == "0":
            findProduct()
        else:
            findProductHeader()
            startingPrice = int(input("Please Enter Starting Price:\t"))
            endingPrice = int(input("Please Enter Ending Price:\t"))
            print("\n\n")
            cursor.execute("""SELECT * FROM product WHERE price >= %s && price <= %s""",(startingPrice,endingPrice))
            result = cursor.fetchall()
            counter = 0
            if result:
                for x in result:
                    print( x)
                    counter = counter + 1
                print("\n\nTotal Product in this Price Range:\t",counter)
                input("\npress any key for continue...")
                findProduct()
            else:
                input("Product not found! Press any key for continue...")
                findProduct()
       
    elif value == '5':
        os.system('cls')
        mainMenu()
    else:
        os.system('cls')
        print("Invalid Input")
        input("Press any for continue...")
        findProduct()
    db.commit()
        
# Find Product section end here 
#######################################################################




#######################################################################
# Delete Product section Start here 
def deleteProduct():
    os.system('cls')
    # delete header 
    def deleteHeader():
        print("{:>60}".format("*************************************"))
        print("{:>51}".format("DELETE PRODUCT"))
        print("{:>60}".format("*************************************\n"))


    cursor = db.cursor()
    deleteHeader()
    print("0.Go Back")
    value = input("Press any key for continue...\t")
    if value == '0':
        deleteProduct()
    else:
        os.system('cls')
        deleteHeader()
        id = input("Please Enter product ID:\t")
        cursor.execute("""SELECT * FROM product WHERE productid = %s;""", (id,))
        result = cursor.fetchone()
        if result:
            print("Are You Sure ?")
            print("1. Yes")
            print("2. No")
            value = input("Please Enter:\t")
            if value == '1':
                cursor.execute("""DELETE FROM product WHERE productid = %s;""", (id,))
                db.commit()
                os.system('cls')
                print("Delete Successfully")
                print("0.GO Back")
                value = input("Print any key for continue:\t")
                if value == "0":
                    mainMenu()
                else:
                    
                    deleteProduct()
            elif value == '2':
                print("Thanks for your confirmation")
                time.sleep(1)
                mainMenu()
        else:
            os.system('cls')
            deleteHeader()
            print("sorry!! Product not found")
            print("0.Go Back")
            value = input("Press any key for continue...")
            if value == '0':
                mainMenu()
            else:
                deleteProduct()
        
# Delete Product section End here 
#######################################################################


#######################################################################
# Show all Product section Start here 
def showAllProduct():
    os.system('cls')
    print("{:>60}".format("*************************************"))
    print("{:>51}".format("All Products List"))
    print("{:>60}".format("*************************************\n"))
    ObjCursor = db.cursor()
    ObjCursor.execute("SELECT * FROM product")
    result = ObjCursor.fetchall()
    counter = 0
    if result:
        for x in result:
            counter = counter + 1
            print(x)
        print("\nTotal Product:\t",counter)
        input("Press any key for continue...\t")
        mainMenu()
    else:
        print("No Product found")
        print("Total Product:\t",counter)
        input("Press any key for continue...")
        mainMenu()
   
    db.commit()

    
# Show all  Product section End here 
#######################################################################


#######################################################################
# Update  Product section Start here 
def updateProduct():
    os.system('cls')
    # update header function  
    def updateHeader():
        print("{:>60}".format("*************************************"))
        print("{:>51}".format("UPDATE PRODUCT VALUE"))
        print("{:>60}".format("*************************************\n"))
   
    updateHeader()
    cursor =  db.cursor()
    print("0.Go Back")
    value = input("Press any key for continue...:\t\t")
    if value == '0':
        mainMenu()
    else:
        updateHeader()
        os.system('cls')
        print("{:>60}".format("*************************************"))
        print("{:>51}".format("UPDATE PRODUCT VALUE"))
        print("{:>60}".format("*************************************\n"))
        id = input("Please Enter Product ID:\t")
        cursor.execute("""SELECT * FROM product WHERE productId = %s;""", (id,))
        result = cursor.fetchone()
        if result:
            print("ID:\t\t\t",result[0])
            print("Name:\t\t\t",result[1])
            print("Brand Name:\t\t",result[2])
            print("Price:\t\t\t",result[3]," BDT")
            print("Display:\t\t "+result[4]+" Inch")
            print("ROM:\t\t\t",result[5]," GB")
            print("RAM:\t\t\t",result[6]," GB")
            print("Camera:\t\t\t",result[7]," MP")
            print("Battery:\t\t",result[8]," mAh")

            # update menu 
            print("\nPlease select which one do you want to update")
            print("1. Name")
            print("2. Brand Name")
            print("3. Price")
            print("4. Display")
            print("5. ROM")
            print("6. RAM")
            print("7. Camera")
            print("8. Battery")
            print("9. Multiple Update")
            print("0. GO Back")
            
        
            value = input("Please Enter:\t")
            
            
            def singleUpdate(filedName, updatedValue, id):
                sql = f"UPDATE product SET `{filedName}` = %s WHERE productId = %s"
                values = (updatedValue, id)
                cursor.execute(sql, values)
                db.commit()
                print("Update Successful")
                print("0.Go Back")
                value = input("Press any key for continue...\t")
                if value == '0':
                    mainMenu()
                else:
                    updateProduct()
            

            if value == '1':
                os.system('cls')
                name = input("Please Enter new product name:\t")
                singleUpdate("productname",name, id)

            elif value == '2':
                os.system('cls')
                brandName = input("Please Enter new brand name:\t")
                singleUpdate("barandname",brandName, id)

            elif value == '3':
                os.system('cls')
                price = input("Please Enter new price:\t")
                singleUpdate("price",price, id)

            elif value == '4':
                os.system('cls')
                display = input("Please Enter new display size:\t")
                singleUpdate("display",display, id)

            elif value == '5':
                os.system('cls')
                rom = input("Please Enter new ROM size:\t")
                singleUpdate("memory",rom, id)

            elif value == '6':
                os.system('cls')
                ram = input("Please Enter new RAM size:\t")
                singleUpdate("ram",ram, id)

            elif value == '7':
                os.system('cls')
                camera = input("Please Enter new Camera:\t")
                singleUpdate("camera",camera, id)

            elif value == '8':
                os.system('cls')
                battery = input("Please Enter new battery size:\t")
                singleUpdate("battery",battery, id)

            elif value == '9':
                os.system('cls')
                name = input('Please enter new product name:\t')
                brand = input("Please Enter new brand name:\t")
                price = input("Please enter new price:\t")
                display = input("Please enter new display size:\t")
                rom = input("Please enter new ROM size:\t")
                ram = input("Please enter new RAM size:\t")
                camera = input("Please enter new camera size:\t")
                battery = input("Please enter new battery size:\t")
                sql = "UPDATE product SET productname = %s, barandname = %s, price = %s, display = %s, memonry = %s, ram = %s, camera = %s, battery = %s WHERE productId = %s"
                values = (name,brand,price,display,rom,ram,camera,battery,id)
                cursor.execute(sql,values)
                db.commit()
                print("Update Successful")
                print("0.Go Back")
                value = input("Press any key for continue...\t")
                if value == '0':
                    mainMenu()
                else:
                    updateProduct()

            elif value == '0':
                os.system('cls')
                mainMenu()
            else:
                print("Invalid Input !! ")
                input("Press any key for continue:\t")
                updateProduct()
        else:
            os.system('cls')
            updateHeader()
            print("Product Not found")
            input("Press any for continue...")
            updateProduct()
    
# UpdateProduct section End here 
#######################################################################

adminMenu()
# mainMenu()
