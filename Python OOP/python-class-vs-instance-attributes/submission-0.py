class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, bal: int) -> None:
        self.name = name
        self.bal = bal
        BankAccount.total_accounts += 1
        BankAccount.total_balance += bal



# TODO: Create two accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
# print(f"Alice's balance: ${acc1.bal}")
# print(f"Bob's balance: ${acc2.bal}")

# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${acc1.bal}")
print(f"Bob's balance: ${acc2.bal}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")