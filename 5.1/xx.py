def color(r, g, b):
    if r >= 230 and r <= 255 and g >= 0 and g <= 25 and b >= 0 and b <= 25:
        print("red")

    if r >= 0 and r <= 25 and g >= 230 and g <= 255 and b >= 0 and b <= 25:
        print("green")

    if r >= 0 and r <= 25 and g >= 0 and g <= 25 and b >= 230 and b <= 255:
        print("blue")


    print(color(5, 235, 2))