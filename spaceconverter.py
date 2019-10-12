def spaceconvert(stringe):
    i = 0
    strng = []
    for c in stringe:
        if (c == ' '):
            strng.append('%20')
        else:
            strng.append(stringe[i])
        i+=1
    return strng


if __name__ == '__main__':
    stringe = "spirit tomb"
    spaceconvert(stringe)
    # print(spaceconvert("spirit tomb"))