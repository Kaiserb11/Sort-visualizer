def bubble(val, p):
    i = p
    if val[i] > val[i+1]:
        temp = val[i]
        val[i] = val[i+1]
        val[i+1] = temp
    print(val)
    return val






