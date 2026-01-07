print("Números processados: ")
for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if x < 3:
        pass

    if x == 3:
        continue

    if x == 10:
        break

    print(x)