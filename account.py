import random
import datetime
class Account():

        def __init__(self, balance, account_no,account_type,pending_loan,loan_balance,loan_repaymentdate,fixeddeposit,interestdate):
                self.balance = float(balance)
                self.account_no = account_no
                self.account_type=account_type
                self.pending_loan=float(pending_loan)
                self.loan_balance=float(loan_balance)
                self.loan_repaymentdate=loan_repaymentdate
                self.fixeddeposit=float(fixeddeposit)
                self.interestdate=interestdate
        
        def fixed_deposit(self):
                if self.fixeddeposit>0:
                        self.interest_check()#checking date
                else:#if there is no fixed deposit then asking if he/she wants to have fixed deposit
                        try:
                                print("\n You do not have fixed deposit \n \n Do You want to have fixed deposit in your account \n \n Type Yes or No \n")
                                decision=input("\n Do You want to  deposit fixed amount :  ")
                                decision=decision.upper()
                                if decision=="YES" or decision=="Y" or decision=="y":
                                        self.fixeddeposit=float(input("\n Enter Fixed deposit Amount  :  "))
                                        if self.fixeddeposit<=0:
                                                print("Wrong Fixed deposit amount")
                                        else:
                                                self.interestdate=self.interest_getting_date()
                                                print("\n Now You have",self.fixeddeposit,"fixed deposit in your account")
                        except ValueError:
                                print("\n Wrong Input")
        def interest_check(self):
                self.interestdate=str(self.interestdate)
                #converting string to date 
                slist = self.interestdate.split("/")#spliting string to change into date
                self.interestdate = datetime.date(int(slist[2]),int(slist[1]),int(slist[0]))
                daysremaining=(self.interestdate-datetime.date.today()).days
                self.interestdate=str(self.interestdate)
                slist = self.interestdate.split("-")
                self.interestdate = (slist[2]),(slist[1]),(slist[0])#to convert format of date
                self.interestdate ='/'.join(self.interestdate) #to change format of date and avoid error
                self.interestdate=str(self.interestdate)
                if daysremaining<=0:
                                      interest=self.interestrate()
                                      self.balance+=(interest+self.fixeddeposit)
                                      self.interestdate="00/00/0000"#if interest and fixed deposit is paid setting date and fixed deposit into zero again
                                      self.fixeddeposit=0.0
                                      print("\n Your previous Interest and fixed deposit has been added to your balance \n")
                else:
                        print("You have",self.fixeddeposit,"fixed deposit in your account \n")
                        interest=self.interestrate()
                        print("You will have",interest,"interest and fixed deposit added to your account in",self.interestdate)
                        
                
                
        def interest_getting_date(self):
                approveddate = datetime.date.today() #getting current date
                self.interestdate=approveddate + datetime.timedelta(365) #interest after one year
                self.interestdate=str(self.interestdate)
                slist = self.interestdate.split("-")
                self.interestdate = (slist[2]),(slist[1]),(slist[0])#to convert format of date
                self.interestdate ='/'.join(self.interestdate) #to change format of date and avoid error
                return self.interestdate
        def interestrate(self): #setting interest rate for each types of accounts 
                if self.account_type=="Student":
                        interest=(self.fixeddeposit*5)/100
                        return interest
                if self.account_type=="Classic":
                        interest=(self.fixeddeposit*3)/100
                        return interest

                              
        def deposit(self, amount):
                self.balance+=amount #adding money to the account



        def overdraft(self,withdrawamount): #overdraft if balance is less than withdraw amount 
                if self.account_type=="Basic":
                        print ("\n You do not have Overdraft Services \n")#No overdraft for  basic account
                if self.account_type=="Classic" and (self.balance-withdrawamount>=-2000.00):
                        self.balance-=withdrawamount
                if self.account_type=="Classic" and (self.balance-withdrawamount<-2000.00):
                        print("\n Overdraft Limit is 2000 for Classic Account \n")#overdraft limit of 2000 for classic acount.
                if self.account_type=="Student" and (self.balance-withdrawamount>=-1000.00):
                        self.balance-=withdrawamount
                if self.account_type=="Student" and (self.balance-withdrawamount<-1000.00):
                        print("\n Overdraft Limit is 1000 For Student Account \n")#overdraft limit for student account is 1000.
        def loanduecheck(self):# to check whether customer should should pay extra charge for exceeding repayment date
                self.loan_repaymentdate=str(self.loan_repaymentdate)
                try:
                        slist = self.loan_repaymentdate.split("/")
                        self.loan_repaymentdate = datetime.date(int(slist[2]),int(slist[1]),int(slist[0]))
                        daysremaining=(self.loan_repaymentdate-datetime.date.today()).days
                except IndexError:
                        slist = self.loan_repaymentdate.split("-")
                        self.loan_repaymentdate = datetime.date(int(slist[0]),int(slist[1]),int(slist[2]))
                        daysremaining=(self.loan_repaymentdate-datetime.date.today()).days
                        
                print(" \n %s days to pay loan"%daysremaining)
                self.loan_repaymentdate=str(self.loan_repaymentdate)
                if daysremaining<0:
                        print("\n Loan Not paid at time \n")
                        print("You have to pay",daysremaining*2,"extra charge now")
                        self.loan_balance+=((abs(daysremaining))*2)
                        
                else:
                        self.loan_balance==self.loan_balance
        def loancheck(self): 
                if self.loan_balance==0:# if loan is paid then setting repayment date to 00/00/0000
                        self.loan_repaymentdate="00/00/0000"
                else: 
                        self.loan_repaymentdate==self.loan_repaymentdate

        def loandecision(self,loan_request_amount):
                if loan_request_amount>10000: #setting the loan request limit
                        
                        print(" ")
                        print("Maximum loan request amount is 10000")
                else:
                        decision=random.randrange(100)<30#30 percent of requests will be directly approved
                        percent60=random.randrange(100)<60# 60 percent of refused will be pending 
                        if decision==True:#30% will be granted automatically
                                print(" ")
                                print("Loan has been granted by system")
                                self.loan_balance+=loan_request_amount
                                self.loan_repaymentdate=self.loan_repay_date()
                                self.print_loan_report
                        elif decision==False and percent60==True:# if loan is refused then 60 % of refusals will be further reviewed by the administrator
                                print(" \n You need to wait for Administrator to approve your request")
                                self.pending_loan+=loan_request_amount
                                print(" \n Your pending loan balance is %s"%self.pending_loan)
                        else:
                                print("\n Loan was not granted by the Bank")
                                self.pending_loan==0
        def admin_loan_decision(self):
                print(" \n Type Yes or NO")
                choice=(input(" \n Do you want to approve loan request? "))
                choice=choice.upper()
                if choice=="YES":# if administrator approve loan pending loan will be granted as loan balance
                        self.loan_balance+=self.pending_loan
                        self.pending_loan=0
                        self.loan_repaymentdate==self.loan_repay_date()
                        print("\n Loan has been approved by the Administrator")
                else:
                        self.pending_loan=0 # if loan is not granted by administrator then pending loan will be 0
                        print(" \n Loan was not granted by Administrator")
                        
                
        def print_loan_report(self):#printing loan details
                if self.loan_balance!=0:
                        self.loanduecheck() #to check due date and if due date has passed to charge certain amount
                self.loancheck()#to check  loan amount and if loan is 0 then date will be 0
                print("\n Total Loan is %s"%self.loan_balance)
                print(" \n Loan Repayment due date %s"%self.loan_repaymentdate)
                if self.pending_loan!=0:
                        print(" \n Loan Pending :",self.pending_loan)#to print pending loan
        def loan_repay(self,repayamount):# loan repay method
                self.loan_balance-=repayamount
                if self.loan_balance==0:
                        print("\n All loan repaid")
                        self.loan_repaymentdate=="00/00/0000"#when loan balance is 0.0 date will be 00/00/0000
                else:
                        self.loan_repaymentdate=self.loan_repaymentdate
        def loan_repay_date(self):
                approveddate = datetime.date.today() #getting current date
                self.loan_repaymentdate=approveddate + datetime.timedelta(21) #setting repayment date to 21 days from today
                self.loan_repaymentdate=str(self.loan_repaymentdate)
                slist = self.loan_repaymentdate.split("-")
                self.loan_repaymentdate = (slist[2]),(slist[1]),(slist[0])#to convert format of date
                self.loan_repaymentdate ='/'.join(self.loan_repaymentdate) #to change format of date and avoid error
                return self.loan_repaymentdate
                
        def get_loan_pending(self):
                return self.pending_loan
        def get_loan_balance(self):
                return self.loan_balance

        def get_repaymentdate(self):
                return self.loan_repaymentdate
        
        def withdraw(self,withdrawamount):
                if self.balance>=withdrawamount and withdrawamount>0:#if balance is more than withdraw amount then subracting amount from balance
                        self.balance-=withdrawamount
                elif self.balance<withdrawamount and withdrawamount>0:#if balance is less than withdraw calling overdrafrt method
                        self.overdraft(withdrawamount)

        def transferout(self,transferamount,receiver):   #This method is to take out money transfered
                        if self.balance>=transferamount and transferamount>0:
                                self.balance-=transferamount
                        else:
                                print("\n Could Not Transfer Money \n \n Check Your Input or Balance \n")
                        print ("Balance is",self.balance)
        def checktransfer(self,transferamount):#To check tranfer   
                if self.balance>=transferamount and transferamount>0:
                        return ("pass")
                else:
                        return("fail")

                
                        
        def transfer(self,transferamount):
                self.balance=self.balance+transferamount  # Transfers money to receiver's account


        def print_balance(self):
                print(" \n Balance is %.2f" %self.balance)

        def get_balance(self):
                return self.balance

        def get_account_no(self):
                return self.account_no

        def get_account_type(self):
                return self.account_type
        def  get_pending_loan(self):
                return self.pending_loan
        def account_menu(self):
                #printing the options
                 print (" ")
                 print ("Your Transaction Options Are:")
                 print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 print ("1) Deposit money")
                 print ("2) Check balance")
                 print ("3) Interest")
                 print ("4) Withdraw money")
                 print ("5) Request Loan")
                 print ("6) Repay Loan")
                 print ("7) Loan Details")
                 print ("8) Back")
                 print (" ")
                 try:#to avoid error
                         option = int(input ("Choose your option: "))
                         return option
                 except ValueError:
                         print()
                         print("Incorrect Option.. Input correct option")
                

        def run_account_options(self):
                loop = 1
                while loop == 1:
                        choice = self.account_menu()
                        if choice == 1:
                                try:#to avoid error
                                        amount=float(input("::\nPlease enter amount to be deposited\n: "))
                                        if amount>0:# amount to deposit should not be negative number
                                                deposit = self.deposit(amount)
                                        else:#informing to use another option to withdraw
                                                print("Use another option to Withdraw money")
                                        self.print_balance()
                                except ValueError:
                                        print("Incorrect Amount")
                        elif choice == 2:
                                balance = self.print_balance()
                        elif choice==3:
                                if self.account_type=="Basic":
                                        print("You do not have this service")
                                else:
                                        self.fixed_deposit()
                                #interest=self.interestrate()
                                #print ("If You have",self.balance,"For one year Your interest will be",interest)
                        elif choice==4:
                                balance = self.print_balance()
                                try:
                                        withdrawamount=float(input("::\n Please enter amount to be Withdrawn \n: ")) #asking money to be withdrawn from the account
                                        withdraw=self.withdraw(withdrawamount)
                                        self.print_balance()
                                except ValueError:
                                        print("Incorrect Amount")
                        elif choice==5:
                                try:
                                        loan_request_amount=float(input("::\nPlease enter amount that you want to request \n: ")) #asking user rquest amount
                                        loanrequest=self.loandecision(loan_request_amount)
                                        print(" ")
                                        print("------------------------------------")
                                        self.print_loan_report()
                                except ValueError:
                                        print("Incorrect Amount")
                        if choice == 6:
                                if self.loan_balance==0: # if there is no loan then printing no loan taken
                                        print("You do not have Loan to pay")
                                else:
                                        try: # to handel error
                                                repayamount=float(input("::\nPlease enter amount to  repay\n: "))
                                                if self.loan_balance<repayamount or repayamount<0:
                                                        print("Repay Amount More than Loan taken Or Incorrect Input ")


                                                else:
                                                        repay = self.loan_repay(repayamount)
                                                self.print_loan_report()
                                        except ValueError:
                                                print("Incorrect Amount")                                        
                        elif choice==7:
                                self.print_loan_report()# print loan details
                        elif choice == 8:
                                loop = 0
                print ("Exit account operations")
