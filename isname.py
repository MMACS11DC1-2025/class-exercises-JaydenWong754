def is_light(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if ((r + g + b)/3) >= 128:
        return True
    return False
