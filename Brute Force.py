# ATM
def atm(amt):
    str_amt = str(amt)

    output = []
    temp = []

    a = '1000'
    b = '500'
    c = '200'
    d = '100'
    e = '50'
    f = '20'
    g = '10'
    h = '5'

    thou = str_amt[:-3]
    hund = str_amt[-3:]
    ten = str_amt[-2:]
    intt = str_amt[-1]

    for num in str_amt:
        if num + str_amt[1] + str_amt[2] == thou or num + str_amt[1] == thou or num == thou:
            temp.append(a)
            output = output + (temp * int(thou))

        if num == hund[0]:

            if int(num) == 5:
                output.append(b)

            if int(num) > 5:
                if int(num) == 6:
                    output.append(b)
                    output.append(d)

                if int(num) == 7:
                    output.append(b)
                    output.append(c)

                if int(num) == 8:
                    output.append(b)
                    output.append(c)
                    output.append(d)

                if int(num) == 9:
                    output.append(b)
                    output.append(c)
                    output.append(c)

            if int(num) < 5:
                if int(num) == 4:
                    output.append(c)
                    output.append(c)

                if int(num) == 3:
                    output.append(c)
                    output.append(d)

                if int(num) == 2:
                    output.append(c)

                if int(num) == 1:
                    output.append(d)

        if num == ten[0]:

            if int(num) == 5:
                output.append(e)

            if int(num) > 5:
                if int(num) == 6:
                    output.append(e)
                    output.append(g)

                if int(num) == 7:
                    output.append(e)
                    output.append(f)

                if int(num) == 8:
                    output.append(e)
                    output.append(f)
                    output.append(g)

                if int(num) == 9:
                    output.append(e)
                    output.append(f)
                    output.append(f)

            if int(num) < 5:
                if int(num) == 4:
                    output.append(f)
                    output.append(f)

                if int(num) == 3:
                    output.append(f)
                    output.append(g)

                if int(num) == 2:
                    output.append(f)

                if int(num) == 1:
                    output.append(g)

        if num == intt:

            if int(num) >= 5:
                output.append(h)

            else:
                pass

    return output


def ATM_Sequence_corr():
    import time
    print('\nOFILI PATRICK ONYEBUCHI welcome to GoldMan Sachs')
   
    acct_type = int((input('Choose account type \n(1)Savings \n(2)Current \n: ')))
    if acct_type == 1 or acct_type == 2:
        receipt = int(input('Do you want a receipt for this transaction \n(1)Yes \n(2)No \n: '))
        if receipt == 1 or receipt == 2:
            trans_type = int(input(
                'Choose the transaction type \n(1)Withdraw \n(2)Buy airtime \n(3)Pay bills \n(4)Transfer fund \n: '))
            if trans_type == 1:
                trans_amt = int(input('Enter the amount: '))
                print(atm(int(trans_amt)))
                print('Please take your cash')

                redo = int(input('Do you want to perform another transaction? \n(1)YES \n(2)NO \n: '))
                if redo == 1:
                    print(ATM_Sequence())
                else:
                    print('Have a lovely day')
                    time.sleep(1)

            elif trans_type == 2 or trans_type == 3 or trans_type == 4:
                print('Sorry the algorithm isn\'t ready yet')
                time.sleep(1)
        
def ATM_Sequence():
    import time
    print('OFILI PATRICK ONYEBUCHI welcome to GoldMan Sachs')
    password = int(1234)
    pass_promt = int(input('Enter the four digit password: '))
    if password == pass_promt:
        acct_type = int((input('Choose account type \n(1)Savings \n(2)Current \n: ')))
        if acct_type == 1 or acct_type == 2:
            receipt = int(input('Do you want a receipt for this transaction \n(1)Yes \n(2)No \n: '))
            if receipt == 1 or receipt == 2:
                trans_type = int(input(
                    'Choose the transaction type \n(1)Withdraw \n(2)Buy airtime \n(3)Pay bills \n(4)Transfer fund \n: '))
                if trans_type == 1:
                    trans_amt = int(input('Enter the amount: '))
                    print(atm(int(trans_amt)))
                    print('Please take your cash')

                    redo = int(input('Do you want to perform another transaction? \n(1)YES \n(2)NO \n: '))
                    if redo == 1:
                        print(ATM_Sequence())
                    else:
                        print('Have a lovely day')
                        time.sleep(1)

                elif trans_type == 2 or trans_type == 3 or trans_type == 4:
                    print('Sorry the algorithm isn\'t ready yet')
                    time.sleep(1)
    else:
        try_again = int(input('\nWrong Password Please try again: '))
        while try_again != password:
            try_again = int(input('Wrong Password Please try again: '))

        if try_again == password:
            print(ATM_Sequence_corr())


ATM_Sequence()

