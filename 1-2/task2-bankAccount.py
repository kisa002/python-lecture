class BankAccount(object):
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.__balance = balance

    def GetName(self):
        return self.name;

    def SetBalance(self, amount):
        self.__balance = amount

    def GetBalance(self):
        return self.__balance

    def IncreaseBalance(self, amount):
        self.__balance += amount

    def DecreaseBalance(self, amount):
        self.__balance -= amount


class SavingAccount(BankAccount):
    def __init__(self, name, number, balance, rate):
        super().__init__(name, number, balance)
        self.rate = rate

    def SetRate(self, rate):
        self.rate = rate

    def GetRate(self):
        return self.rate

    def AddRate(self):
        self.IncreaseBalance(self.GetBalance() * self.rate)


class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.charge = 10000

    def SetCharge(self, charge):
        self.charge = charge

    def Withdraw(self, amount):
        amount += self.charge
        self.DecreaseBalance(amount)


def InitSavingAccounts():
    global savingAccounts

    savingAccounts = []
    savingAccounts.append(SavingAccount("이승민", len(savingAccounts), 10000, 0.05))
    savingAccounts.append(SavingAccount("차재훈", len(savingAccounts), 20000, 0.05))
    savingAccounts.append(SavingAccount("배재형", len(savingAccounts), 30000, 0.05))
    savingAccounts.append(SavingAccount("정대영", len(savingAccounts), 40000, 0.05))
    savingAccounts.append(SavingAccount("박철현", len(savingAccounts), 50000, 0.05))


def InitCheckingAccounts():
    global checkingAccounts

    checkingAccounts = []
    checkingAccounts.append(CheckingAccount("정혜진", len(checkingAccounts), 1000000))
    checkingAccounts.append(CheckingAccount("김원빈", len(checkingAccounts), 2000000))
    checkingAccounts.append(CheckingAccount("강동현", len(checkingAccounts), 3000000))
    checkingAccounts.append(CheckingAccount("강기환", len(checkingAccounts), 4000000))
    checkingAccounts.append(CheckingAccount("유광무", len(checkingAccounts), 5000000))


def GetSumBalance(accounts):
    balance = 0

    for account in accounts:
        balance += account.GetBalance()

    return balance

def GetVipAccount(accounts):
    vipAccount = {"name": "", "balance": 0}

    for account in accounts:
        if vipAccount["balance"] <= account.GetBalance():
            vipAccount["name"] = account.GetName()
            vipAccount["balance"] = account.GetBalance()

    return vipAccount


def GetVipAccounts(account1, account2):
    if account1["balance"] > account2["balance"]:
        vipName = vipSavingAccount["name"]
    elif account1["balance"] < account2["balance"]:
        vipName = vipCheckingAccount["name"]
    else:
        vipName = vipSavingAccount["name"] + ", " + vipCheckingAccount["name"]

    return vipName


def GetVipCheckingAccount():
    global vipCheckingAccount

    vipCheckingAccount = {"name": "", "balance": 0}


def Init():
    InitSavingAccounts()
    InitCheckingAccounts()


if __name__ == "__main__":
    Init()

    sumSavingBalance = GetSumBalance(savingAccounts)
    sumCheckingBalance = GetSumBalance(checkingAccounts)

    vipSavingAccount = GetVipAccount(savingAccounts)
    vipCheckingAccount = GetVipAccount(checkingAccounts)
    vipAllCount = GetVipAccounts(vipSavingAccount, vipCheckingAccount)

    print("[      예금 합계      ]")
    print("저축예금 합계: {0}원".format(sumSavingBalance))
    print("당좌예금 합계: {0}원\n".format(sumCheckingBalance))

    print("[      예금 VIP      ]")
    print("저축예금 VIP:", vipSavingAccount["name"])
    print("당좌예금 VIP:", vipCheckingAccount["name"])
    print("전체예금 VIP:", vipAllCount)
