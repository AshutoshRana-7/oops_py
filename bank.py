class swiss_bank():
    Ifsc = 'swiss1234'
    Branch_code = 1
    Location = 'Marathahalli'
    
    def __init__ (self,name,Acc_no,mob_no,Bal):
        self.name = name
        self.Acc_no = Acc_no
        self.mob_No = mob_no
        self.Bal = Bal
        
    def Details(self):
        print(f'name = {self.name}')
        print(f'Account Number = {self.Acc_no}')
        print(f'Contact = {self.mob_No}')
        print(f'Bal = {self.Bal}')

    def Check_Bal(self):
        print(f'Avaliable Balance is {self.Bal}')

    def Deposite(self):
        money = int(input('Enter the amount to Deposite: '))
        if 100 <= money <= 40000:
            if money % 100 ==0:
                self.Bal+=money
                print('Money added successfully...')
            else:
                print('check the denomition')
        else:
            print('Invalid Amount')
    
    def Withdrawn(self):
        money = int(input('enter the amount to withdrown: '))
        if 100 <= money <= 20000:
            if money % 100 ==0:
                self.Bal -=money
                print('Amount debited successfuly')
            else:
                print('check the denomition')
        else:
            print('Invalid Amount')

cust1 = swiss_bank('ashu',40001241903,9337676371,10000000000)
cust2 = swiss_bank('me',944887733001,9883663532,4998899080)
cust3 = swiss_bank('asut',565326456,787876524,500000000)

cust1.Check_Bal()
print('-----------')
cust1.Withdrawn()
print('-----------')
cust1.Check_Bal()
