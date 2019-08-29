class BankAccount :
    rate=7;
    def __init__(self):
        print("Constructor __init()__ called");
        
    def set(self):
        self.acno = int(input("Enter account no .: "));
        self.name=input("Enter customer name : ");
        self.balance=int(input("Enter Account balance : "));

    def Deposite(self):
        self.dep=int(input("Enter amount to deposite : "));
        self.balance=self.balance+self.dep;
    def Withdraw(self):
        self.wid=int(input("Enter amount to withdraw : "));
        if self.wid <= self.balance:
            print("Cannot withdraw..!!");
        else:
            self.balance=self.balance-self.wid;
    def calc_interest(self):
        self.interest=self.balance+(self.balance*self.rate)/100;
    def show(self):
        print("Account no : ",self.acno);
        #print("Name : ",self.name);
        print("customer name : ",self.name);
        print("Available balance : ",self.balance);
        print("Interest : ",self.interest);

acc1=BankAccount();
acc1.set();
acc1.Deposite();
acc1.Withdraw();
acc1.calc_interest();
acc1.show();
