from customer import Customer
from admin import Admin
from account import Account


customers_list = []
admins_list = []

	
class BankSystem(object):
    def __init__(self):
        self.customers_list = [] #creating empty customers list
        self.admins_list = []  #creating #empty admins list
        self.load_bank_data()  # loading database


    def load_bank_data(self):
        #loding customers data
        databasecustomers=open("customersdata.csv","r")  # opening database file as reading mode
        line=databasecustomers.readline()           # reading line
        account_no=1234
        while line!="":# reading line unless it is empty    
            customerdata=line.split(",")#spliting each words if comma is in the line
            customer=Customer((customerdata[0]),(customerdata[1]),(customerdata[2:6]))#creating customer
            account=Account((customerdata[6]),(account_no),(customerdata[7]),(customerdata[8]),(customerdata[9]),(customerdata[10]),(customerdata[11]),(customerdata[12]))#creating account
            customer.open_account(account)
            self.customers_list.append(customer)
            line=databasecustomers.readline()
            account_no+=1   
        databasecustomers.close()
        #Loading Admins data
        databaseadmin=open("admindatabase.csv","r")
        line=databaseadmin.readline()
        count=1
        while line!="":
            admindata=line.split(",")
            admin=Admin((admindata[0]),(admindata[1]),(admindata[2]),(admindata[3:7]))
            self.admins_list.append(admin)
            line=databaseadmin.readline()
        databaseadmin.close()


    def customer_login(self, name, password):
        #STEP A.1 Customer login function
        found_customer = self.search_customers_by_name(name)  #searching customer name 
        if found_customer == None:                            #if name name is not found
            return("\n The customer has not been found!\n")
        else:
            if (found_customer.check_password(password) == True):  # if name is found then check if password is right.  
                self.run_customer_options(found_customer)          # if name and password is right show options..   
            else:
                return(" \n Password or Username is wrong")        # if name is right and password is wrong
                
        
    def search_customers_by_name(self, customer_name):
        #STEP A.2 Search for a customer object
        found_customer = None
        for a in self.customers_list:                  # checking list of names in our database 
            name = a.get_name()                        # if given name is right then saving it
            if name == customer_name:
                found_customer = a
                break                                  # if found brealing loop
        if found_customer == None:                      # if name is not found then found customer is none.
            print("\nThe customer %s does not exist! Try again...\n" %customer_name)  # printing no such name is there in system    
        return found_customer                          #returning if the name is there in system


    def main_menu(self):
        #printing the options 
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Customer login")
        print ("3) Quit Python Bank System")
        print (" ")
        try:#to handle error if input is incorrect
            option = int(input ("Choose your option: "))
            return option
        except ValueError:
            print()
            print("Your chosen option is Incorrect. Please input 1 / 2 / 3")

    def run_main_option(self): #Login
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                name = input ("\nPlease input admin name: ")
                password = input ("\nPlease input admin password: ")
                msg = self.admin_login(name, password)
                print(msg)
            elif choice == 2:
                name = input ("\nPlease input customer name: ")
                password = input ("\nPlease input customer password: ")
                msg = self.customer_login(name, password)
                print(msg)
            elif choice == 3:
                loop = 0
        print ("Thank-You for stopping by the bank!")


    def transferMoney(self, sender_account, receiver_name, transferamount):
        sender= self.search_customers_by_name(sender_account)
        if sender!=None:
            receiver=self.search_customers_by_name(receiver_name)# searching receiver
            if receiver!=None:#if receiver found then
                account=sender.get_account()
                account.transferout(transferamount,receiver_name)#take out money from sender
                check=account.checktransfer(transferamount)
                if check=="pass":
                    account=receiver.get_account()
                    account.transfer(transferamount)          #transfer money to receiver
   

    def customer_menu(self, customer_name):
        #print the options you have
         print (" ")
         print ("Welcome %s : Your transaction options are:" %customer_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Other account operations")
         print ("3) profile settings")
         print ("4) Sign out")
         print (" ")
         try:#to handele incorrect input
             option = int(input ("Choose your option: "))
             return option
         except ValueError:
             print()
             print("Option you choose is Incorrect.... ")
    

    
    def run_customer_options(self, customer):
                    
        account = customer.get_account()            
        loop = 1
        while loop == 1:
            choice = self.customer_menu(customer.get_name())
            if choice == 1:
                sender_account=customer.get_name()
                print (sender_account)
                try:#to handle input error
                    receiver_name=input(" \n Enter Reciever name   :")#getting receiver's name
                    transferamount=float(input(" \n Enter amount to be transferred : \n"))#getting amount to be transferred
                    self.transferMoney(sender_account, receiver_name, transferamount)#calling another method to transfer money
                except ValueError:
                    print("Input is Incorrect....")
            elif choice == 2:
                account.run_account_options()
            elif choice == 3:
                customer.run_profile_options()
            elif choice == 4:
                loop = 0
        print ("Exit account operations")

                
    def admin_login(self, name, password):
        # STEP A.3
        found_admin = self.search_admin_by_name(name)  #searching admin name 
        if found_admin == None:                            #if name name is not found
            return("\n The Admin has not been found!\n")
        else:
            if (found_admin.check_password(password) == True):  # if name is found then check if password is right.  
                self.run_admin_options(found_admin)          # if name and password is right show options..   
            else:
                return("you have input a wrong password")        # if name is right and password is wrong
                




    def search_admin_by_name(self, admin_name):
        # STEP A.4
        found_admin = None
        for a in self.admins_list:                  # checking list of names in our database 
            name = a.get_name()                        # if given name is right then saving it
            if name == admin_name:
                found_admin = a
                break                                  # if found exit loop
        if found_admin == None:                      # if name is not found then found admin is none.
            print("\nThe customer %s does not exist! Try again...\n" %admin_name)  # printing no such name is there in system    
        return found_admin                          #returning if the name is there in system        



    def admin_menu(self, admin_name):
        #printing the options 
         print (" ")
         print ("Welcome Admin %s : Available options are:" %admin_name)
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations")
         print ("3) Customer profile settings")
         print ("4) Admin profile settings")
         print ("5) Delete customer")
         print ("6) Print all customers detail")
         print ("7) View Loan Requests")
         print ("8) Print Loan Report")
         print ("9) Sign out")
         print (" ")
         try:# to handle errors
             option = int(input ("Choose your option: "))
             return option
         except ValueError:
             print ("Option You Choose is Incorrect...") 


    def run_admin_options(self, admin):
                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin.get_name())
            if choice == 1:
                sender_account=input (" \n Enter sender  name  :")#getting sender's name
                receiver_name=input(" \n Enter Reciever name   :")#getting receiver's name
                try:
                    transferamount=float(input(" \n Enter amount to be transferred : \n"))#getting amount to transfer
                    self.transferMoney(sender_account, receiver_name,transferamount)
                except ValueError:
                    print ("Please enter correct amount.")
            elif choice == 2:
                #STEP A.5
                customer_name=input("\n Please input customer name: \n")            
                customer = self.search_customers_by_name(customer_name)
                if customer != None:
                  account = customer.get_account()
                  if account != None:
                      account.run_account_options()  
                
            elif choice == 3:
                #STEP A.6
                customer_name = input("\nPlease input customer name :\n")
                customer = self.search_customers_by_name(customer_name)

                if customer!=None:
                    customer.run_profile_options()
                
            elif choice == 4:
                #STEP A.7
                admin.run_profile_options()
            elif choice == 5:
                #STEP A.8
                if admin.has_full_admin_right() == "TRUE":
                    customer_name = input("\nPlease input customer name you want to delete :\n")

                    customer_account = self.search_customers_by_name(customer_name)
                    if customer_account != None:
                        self.customers_list.remove(customer_account)
                        print("\n Customer %s has been removed from the system \n"%customer_name)
                else:
                        print("\nOnly administrators with full admin rights can remove a customer from the bank system!\n")
                
            elif choice == 6:
                #STEP A.9
                self.print_all_accounts_details()
            elif choice==7:
                self.print_loan_request()
            elif choice==8:
                self.print_all_loan_report()
    
            elif choice == 9:
                loop = 0
        print ("Exit account operations")


    def print_all_accounts_details(self):
            # list related operation - move to main.py
            i = 0
            for c in self.customers_list:
                i+=1
                c.print_details()

    def print_loan_request(self):
            i = 0
            for c in self.customers_list:
                i+=1
                c.view_loan_request()
            print("Type Yes or NO ")
            choice=input("\n Do you want to approve/reject loan requests?  ")  #asking if admin wants to approve or reject loan
            choice=choice.upper()
            if choice=="YES":
                self.loan_approve_reject()
    def loan_approve_reject(self):
            customer_name=input("\n Please input customer name: \n")# asking customer's name to approve or reject loan request
            customer = self.search_customers_by_name(customer_name)#searching customer
            if customer != None:
                account = customer.get_account()
                if account != None:
                    account.admin_loan_decision()
            

                    
    def print_all_loan_report(self):
            i = 0
            for c in self.customers_list:
                i+=1
                c.print_loan()
                

                               
app = BankSystem()
app.run_main_option()


