
# Bank Account Balance Program with Withdraw Feature
initial_balance = float(input("Enter initial balance: ₹"))
deposit = float(input("Enter deposit amount: ₹"))

balance_after_deposit = initial_balance + deposit
print("Initial Balance: ₹", initial_balance)
print("Deposit: ₹", deposit)
print("New Balance after deposit: ₹", balance_after_deposit)

withdraw = float(input("Enter withdraw amount: ₹"))
final_balance = balance_after_deposit - withdraw

print("Withdraw: ₹", withdraw)
print("Final Balance: ₹", final_balance)
