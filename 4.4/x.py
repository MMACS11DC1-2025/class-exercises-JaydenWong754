def namebot():
    print("give me a name")
    name = input()
    count = 0
    letters = []
    letters2 = []
    for x in name:
        if x in ["aeiou"]:
            letters += [x]
            letters2 += [x]

    for y in letters:
        letters[0] = letters[-1]
        letters2[-1] = letters[0]

    for z in name:
        if z in ["aeiou"]:
            z = letters[0]
            break

    for a in range(len(name)):
        if name[-a] in ["aeiou"]:
            a == letters2[-1]
            break

    print(name)

namebot()