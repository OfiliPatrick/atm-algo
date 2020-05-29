def ATM(amount):
    # amount = 3675
    denoms = [1000,500,200,100,50,20,10,5]
    index =0
    out = []

    while amount >= 5:
        if amount >= denoms[index]:
            amount = amount - denoms[index]
            out.append(denoms[index])

        else:
            index += 1

    return out


print(ATM(100875325))




