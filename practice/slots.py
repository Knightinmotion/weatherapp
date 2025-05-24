# Python slot Machine
import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🔔":
            return bet * 9
        elif row[0] == "⭐":
            return bet * 12
    return 0


def main():
    balance = 100

    print("**************************")
    print("Welcome to DeepBlue slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("**************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be more than 0")
            continue

        balance -= bet

        row = spin_row()
        print("spinning...\n") # the "\n" is a command for a new line character
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout} ")
        else:
            print("Try again next time")

        balance += payout

        play_again = input("Do you want to spin again (Y/N): ").upper()
        if play_again != 'Y':  # "!=" stand for not equal
            break
        print("\n")

    print("************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("************************************")

if __name__ == '__main__':
    main()

