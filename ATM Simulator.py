# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:21:36 2024

@author: User
"""
import time, sys

print('Welcome to Cyber ATM, please insert your card!')
time.sleep(1)
print('processing...')
time.sleep(1)

def perform_another_transaction():
    while True:
        again = input('Do you want to perform another transaction (y/n): ').lower()
        if again == 'y':
            transaction()
        elif again =='n':
            sys.exit()
        else: print('please choose either y/n')
        
def transaction():
    def check_balance():
        balance = 10000
        print(f'your balance is: {balance}')
        perform_another_transaction()

    def withdraw():
        withdraw_acct=input('Please choose the withdrawal account:\n1. Checking Account 8643\n2. Savings Account 7560\n ')
        withdraw_acct_name = 'Checking Account 8643' if withdraw_acct == '1' else 'Savings Account 7560'
        withdraw = float(input('Enter the amount to withdraw: '))
        print ('Transaction is processing...')
        time.sleep(1)
        print (f'withdraw: ${withdraw} from {withdraw_acct_name}, please take your cash!')
        perform_another_transaction()
            
    def transfer():
        while True:
            withdraw_acct=input('Please choose the withdrawal account:\n1. Checking Account 8643\n2. Savings Account 7560\n ')
            deposit_acct = input('Please choose the deposit account:\n1. Checking Account 8643\n2. Savings Account 7560\n3. Enter Account Number\n')
            withdraw_acct_name = 'Checking Account 8643' if withdraw_acct == '1' else 'Savings Account 7560'
            if deposit_acct in ['1','2']:
                amount= float(input("Enter the amount to transfer: "))
                deposit_acct_name = 'Checking Account 8643' if deposit_acct == '1' else 'Savings Account 7560'
            elif deposit_acct=='3':
                deposit_acct_name = input("Enter the account number: ")
                amount= float(input("Enter the amount to transfer: "))
            else:
                print("Invalid option chosen for account. Please choose again.")
            print(f'Transferring ${amount} from {withdraw_acct_name} to {deposit_acct_name}...')
            time.sleep(1)
            print("Transaction is completed")
            perform_another_transaction()
    while True:
        choice = input("Choose an option:\n1. Check Balance\n2. Withdraw\n3. Transfer\n4. Exit\n")
        if choice =='1':
            check_balance()
        elif choice =='2':
            withdraw()
        elif choice =='3':
            transfer()
        elif choice=='4':
            print('Goodbye, thank you!')
            sys.exit()
        else: print("Invalid option. Please choose 1, 2, 3, or 4.")

    
    
def pin_authentication():
    pins =[1234, 5678, 2468, 3579]
    while True:
        pin=int(input('Please enter your pin!: '))
        if pin in pins:
            print('Welcom to your account!')
            transaction()
        else: print('Wrong pin number, please try again!')
pin_authentication()
        
    