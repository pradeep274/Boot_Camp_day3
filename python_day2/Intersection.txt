#intersection of the above given lists

def intersect(a, b):

    return list(set(a) & set(b))


if __name__ == "__main__": 
    a = [1,3,6,78,35,55]
    b = [12,24,35,24,88,120,155]

    print intersect(a, b)
