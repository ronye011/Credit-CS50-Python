from cs50 import get_int


def main():
    # Ask for a credit card number
    number_card = get_int("Number: ")

    # Measures the size of the number and checks if it is less than 13 digits long
    invalid = len(str(number_card))
    if invalid < 13:
        print("INVALID")
        return 0

    # Separate each digit and add it to a list
    number_temp = []
    for i in range(16):
        number_temp.append(int(number_card) % 10)
        number_card = int(number_card) / 10

    # Multiplies 8 of the 16 numbers alternately by 2
    controle = 1
    number_medium = []
    for i in range(8):
        medium = number_temp[controle] * 2
        number_medium.append(medium)
        controle = controle + 2

    # Separate numbers with two digits
    tamanho = -1
    number_account = []
    medium = 0
    for i in range(8):
        if number_medium[i] > 9:
            medium = number_medium[i]
            result = medium % 10
            number_account.append(int(result))
            medium = medium / 10
            result = medium % 10
            number_account.append(int(result))
            tamanho = tamanho + 2
        else:
            number_account.append(number_medium[i])
            tamanho = tamanho + 1

    # Perform the sum of the numbers
    final = 0
    controle = 0
    for i in range(8):
        medium = int(number_temp[controle])
        final = final + medium
        controle = controle + 2
    print(final)

    for i in range(tamanho + 1):
        final = final + number_account[i]

    final = final % 10

    # Decision tree to find out if the card is valid and what type it is
    if final == 0:
        if 4 in {number_temp[15], number_temp[12]}:
            print("VISA")
            return 0
        if number_temp[15] == 5 and (number_temp[14] in {1, 2, 3, 4, 5}):
            print("MASTERCARD")
            return 0
        if number_temp[14] == 3 and (number_temp[13] in {4, 7}):
            print("AMEX")
            return 0
        else:
            print("INVALID")
            return 0
    else:
        print("INVALID")
        return 0


main()
