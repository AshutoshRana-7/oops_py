class swiss_bank:
    Ifsc = 'swiss1234'
    Branch_code = 1
    Location = 'Marathahalli'
    
    def __init__(self, name, Acc_no, mob_no, Bal, pin):
        self.name = name
        self.Acc_no = Acc_no
        self.mob_No = mob_no
        self.Bal = Bal
        self.pin = pin
        
    def Details(self):  # object method
        print(f'Name = {self.name}')
        print(f'Account Number = {self.Acc_no}')
        print(f'Contact = {self.mob_No}')
        #print(f'Balance = {self.Bal}')

    def Check_Bal(self):  # object method
        count = 3
        while count != 0:
            print(f'Number of attempts left: {count}')
            if self.Take_password() == self.pin:
                print(f'Available Balance is {self.Bal}')
                print('Transaction done')
                break
            else:
                print('Invalid PIN')
                count -= 1
        else:
            print('Try after 24 hours')
        
    def Deposite(self):  # object method
        count = 3
        while count != 0:
            print(f'Number of attempts left: {count}')
            if self.Take_password() == self.pin:
                money = int(input('Enter the amount to Deposit: '))
                if 100 <= money <= 40000:
                    if money % 100 == 0:
                        self.Bal += money
                        print('Money added successfully...')
                        print('Transaction done')
                        break
                    else:
                        print('Check the denomination')
                else:
                    print('Invalid Amount')
            else:
                print('Invalid PIN')
                count -= 1
        else:
            print('Try after 24 hours')
    
    def Withdrawn(self):  # object method
        count = 3
        while count != 0:
            print(f'Number of attempts left: {count}')
            if self.Take_password() == self.pin:
                money = int(input('Enter the amount to Withdraw: '))
                if 100 <= money <= 20000:
                    if money % 100 == 0:
                        if money <= self.Bal:
                            self.Bal -= money
                            print('Amount debited successfully')
                            print('Transaction done')
                            break
                        else:
                            print('Insufficient Balance')
                    else:
                        print('Check the denomination')
                else:
                    print('Invalid Amount')
            else:
                print('Invalid PIN')
                count -= 1
        else:
            print('Try after 24 hours')
    
    @classmethod
    def change_Loc(cls, new_location='USA'):
        cls.Location = new_location
    
    @staticmethod
    def Take_password():
        password = int(input('Enter 4-digit PIN: '))
        return password


# Customers
cust1 = swiss_bank('ashu', 40001241903, 9337676371, 10000000000, 2003)
cust2 = swiss_bank('me', 944887733001, 9883663532, 4998899080, 2222)
cust3 = swiss_bank('asut', 565326456, 787876524, 500000000, 1111)


cust1.Deposite()
# cust1.Check_Bal()
# cust1.Withdrawn()
