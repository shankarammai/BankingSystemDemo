from person import Person

class Customer(Person):

    def __init__(self, name, password, address = [None, None, None, None]):
        super().__init__(name, password, address)

    def open_account(self, account):
        self.account = account

    def get_account(self):
        return self.account
                            
    def print_details(self):
        super().print_details()
        bal = self.account.get_balance()
        acctype=self.account.get_account_type()
        print("Account balance: %.2f" %bal)
        print("Account Type :%s"%acctype)
        print(" ")

    def print_loan(self):
        loan_balance=self.account.get_loan_balance()
        pending_loan=self.account.get_pending_loan()
        if loan_balance!=0 or pending_loan!=0:
            self.print_details()
            self.account.print_loan_report()


    def view_loan_request(self):
        loan_request=self.account.get_loan_pending()
        if loan_request!=0:
            self.print_details()
            print ("Requested Amount :",loan_request)

