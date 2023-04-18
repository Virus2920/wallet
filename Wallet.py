print("Welcome to your wallet")
print("Balance= $0")

investor_name = input("Enter your name: ")
amount_to_invest = float(input("Enter amount to invest: "))
comm = amount_to_invest * 0.5
print("you've been given a 50% commission of", "$",comm)

wallet_balance = (amount_to_invest * 0.5) + amount_to_invest
print("Wallet balance: ","$",wallet_balance)

amount_to_withdraw = float(input("Enter amount to withdraw: $ "))

if amount_to_withdraw >= wallet_balance:
    print("Insufficient Funds")
    option = input("would you like to withdraw a lower amount? ")
    if option == "yes":
        amount_to_withdraw = float(input("Enter amount to withdraw: "))
        if amount_to_withdraw < wallet_balance:
           vat_deduction = 0.07 * amount_to_withdraw
           wallet_balance -= (amount_to_withdraw + vat_deduction)
           print("Withdrawal successful, your account has been debited with", "$",amount_to_withdraw, "and 7% VAT has been deducted.")
           print("Final balance: ", "$", wallet_balance) 
        else:
            print("you have entered an amount higher than or equal to your wallet balance, try again after 24 hours time")
    else:
        print("Thanks for investing with us")
else:
    vat_deduction = 0.07 * amount_to_withdraw
    wallet_balance -= (amount_to_withdraw + vat_deduction)
    print("Withdrawal successful, your account has been debited with", "$",amount_to_withdraw, "and 7% VAT has been deducted.")
    print("Final balance: ", "$", wallet_balance)
    
