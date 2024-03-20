count = 0
while count <= 40:
    if (count % 10 == 0 or count % 4 == 0) and count != 40:
        print("PIN")
    elif count == 40:
        print("FIM")
    else:
        print(count)
    count += 1