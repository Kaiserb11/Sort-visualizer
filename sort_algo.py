def bubble(val, p):
    i = p
    if val[i] > val[i+1]:
        temp = val[i]
        val[i] = val[i+1]
        val[i+1] = temp
    return val


def selection(val,i):
    min_idx = i
    for j in range(i+1, len(val)):
        if val[min_idx] > val[j]:
            min_idx = j
    val[i], val[min_idx] = val[min_idx], val[i]
    return val




