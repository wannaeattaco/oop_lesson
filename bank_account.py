class AccountDB:
    def __init__(self):
        self.account_database = []

    def insert(self, account):
        index = self.search_private(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print("Account", account.account_number, "already exists")

    def search_private(self, account_num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == account_num:
                return i
        return -1

    def search_public(self, account_num):
        for account in self.account_database:
            if account.account_number == account_num:
                return account
        return None

    def __str__(self):
        s = ''
        for account in self.account_database:
            s += str(account) + ", "
        return s


class Account:
    def __init__(self, num, type, account_name, balance):
        self.account_number = num
        self.type = type
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        print("Depositing", amount, "to", self.account_number)
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            print("Withdrawing", amount, "from", self.account_number)
            self.balance -= amount
        else:
            print("withdrawal amount", amount, "exceeds the balance of", self.balance,
                  "for", self.account_number, "account.")

    def __str__(self):
        return '{' + str(self.account_number) + ',' + str(self.type) + ',' + \
               str(self.account_name) + ',' + str(self.balance) + '}'



