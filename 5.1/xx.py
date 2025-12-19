def isgreen(r, g, b):
    if r >= 0 and r <= 25 and g >= 230 and g <= 255 and b >= 0 and b <= 25:
        return True

    else:
        return False