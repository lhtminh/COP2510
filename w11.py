#Intro to classes

class CreditAccount:
    #initializer
    def __init__(self, holder, limit, apr, balance):
        self.__holder = holder 
        self.__limit = limit
        self.__apr = apr
        self.__balance = balance

        

    #accessors (getters)
    def getHolder(self):
        return self.__holder
    
    def getLimit(self):
        return self.__limit
    
    def getAPR(self):
        return self.__apr
    
    def getBalance(self):
        return self.__balance
    
    #mutators (setters)
    def setHolder(self, hname):
        self.__holder = hname
    
    def setLimit(self, limit):
        self.__holder = limit

    def setAPR(self, apr):
        self.__holder = apr
    
    def setHolder(self, balance):
        self.__holder = balance

    

    #additional methods 
    def purchase(self, amount):
        self.__balance = self.__balance + amount
    
    def payment(self, amount):
        self.__balance = self.__balance - amount

    def apply_interest(self):
        rate = self.__apr /12.0
        interest = self.__balance * rate
        self.__balance = self.__balance + interest
        return interest

    #string (summary) methods
    def __str__(self):
        return  (f"Credit Account Info:\n\Holder: {self.__holder}"
                 f"\n\tLimit: ${self.__limit:.2f}"
                 f"\n\tAPR: {self.__apr*100}"
                 f"\n\tBalance: ${self.__balance:,.2f}")
    
    #List of objects
accounts = []

    #recap: input validation and type checking
valid = False
while not valid:
    numaccts = int(input("How many accounts to create?"))
    try:
        if numaccts > 0:
                valid = True
        else:
            print("Enter a positive number.")
    except:
        print("Enter a whole number")
#create numaccts number of accounts
for n in range(numaccts):
    print(f'\n--Enter details for account #{n+1}---')
    holder = input("Account Holder name: ")
    limit = float(input("Credit Limit: "))
    apr = float(input('APR(as a decimal): $'))
    balance = float(input('Balance(as a decimal): $'))

    #create object and add to list
    acct = CreditAccount(holder, limit, apr, balance)
    
    #and add to list
    accounts.append(acct)

#Show all accounts on list
print("\n----Accounts created----")

#recap of matplotlib
import matplotlib.pyplot as plt

#Sample data
exams = [1, 2, 3, 4, 5]
scores = [78, 85, 88, 88, 92, 94]

#create line graph
plt.plot(exams, scores)

#display the graph
plt.show()

names = [acct1.getHolder(), acct2.getHolder(), acct3.getHolder() ]
limits =[acct1.getLimit(), acct2.getLimit(), acct3.getLimit()  ]
plt.bar(names, limits)
plt.show()
