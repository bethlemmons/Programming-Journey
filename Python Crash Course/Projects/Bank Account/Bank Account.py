class Account:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

        print("Account owner: {}".format(owner))
        print("Account balance: ${}".format(balance))

    def deposit(self, dep_amount):
        self.balance += dep_amount
        print("Deposit of: ${} accepted.".format(dep_amount))
        print("Your new balance is: ${}".format(self.balance))

    def withdraw(self, wd_amount):
        if wd_amount > self.balance:
            print("Not enough funds available.")
            print("You have ${} available at this time.".format(self.balance))
        else:
            self.balance -= wd_amount
            print("You withdrew: ${}".format(wd_amount))
            print("Your current balance is: ${}".format(self.balance))


c = Account("Bob", 650)
c.deposit(300)
c.withdraw(400)
c.withdraw(1000)