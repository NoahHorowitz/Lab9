while True:
    password = input('Input your password: ')
    encoded_pass = ''
    try:
        if len(password) == 8 and int(password) >= 0:
            for digit in password:
                if int(digit) >= 7:
                    encoded_pass += str(int(digit) + 3 - 10)
                else:
                    encoded_pass += str(int(digit) + 3)
            print(f'Your encoded password: {encoded_pass}')
        elif password == '-1':
            break
        else:
            print('Invalid password')
    except:
        print('Invalid password')