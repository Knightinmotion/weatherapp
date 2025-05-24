# Python Banking Program

def show_balance(balance):
    print(f"Your Balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("*************************")
        print("that's not a valid amount")
        print("*************************")
        return 0
    else:
        print(f"You have deposited ${amount:.2f} to your Grey account.")
        return amount


def withdrawal(balance):
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("*******************")
        print("Insufficient funds!")
        print("*******************")
        return 0
    elif amount < 0:
        print("**************")
        print("Invalid amount")
        print("**************")
        return 0
    else:
        print(f"You have withdrawn ${amount} from your grey account ")
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print()
        print("------Grey Banking Terminal------")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print()

        choice = input("Enter your choice (1 - 4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdrawal(balance)

        elif choice == '4':
            is_running = False

        else:
            print("********************")
            print("Enter a valid choice ")
            print("*********************")

    print()
    print("---------session ended---------")
    print("Thank you for banking with Grey... Have a wonderful day😅.")


if __name__ == '__main__':
    main()
