#Steven Chen
def encode_password(password):
    encoded_password = ''
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    print("Your password has been encoded and stored!\n")
    return encoded_password

#Mia Hakkarainen
def decode_password(password):
    decoded_password = ''
    for i in password:
        j = str((int(i) - 3) % 10)
        decoded_password += j
    return decoded_password


if __name__ == '__main__':


    while True:

        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        menu_opt = int(input("Please enter an option: "))

        if menu_opt == 1:
            encode = input("Please enter your password to encode: ")
            encoded_password = encode_password(encode)

        elif menu_opt == 2:
            encoded_password = input("Please enter the encoded password to decode: ")
            decoded_password = decode_password(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')

        elif menu_opt == 3:
            break

        else:
            print("Invalid option. Try again.")
