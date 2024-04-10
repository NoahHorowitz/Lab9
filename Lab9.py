if __name__ == "__main__":

    while True:
        # Menu
        print('Password Encoder/Decoder')
        print('------------------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = input('Choose an option: ')
        print('')


        # Option 1: encoder
        if option == '1':
            password = input('Input your password: ')
            encoded_password = str()
            try:
                if len(password) == 8 and int(password) >= 0:
                    for digit in password:
                        if int(digit) >= 7:
                            encoded_password += str(int(digit) + 3 - 10)
                        else:
                            encoded_password += str(int(digit) + 3)
                    password = str()
                    print(f'Your encoded password: {encoded_password}')
                else:
                    print('Invalid password: Please use 8 non-negative numbers')
            except:
                print('Invalid password: An Error occurred')
            print('')


        # Option 2: decoder

        # Option 3: exit the program
        elif option == '3':
            print('Thank you for using this program')
            break