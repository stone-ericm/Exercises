from provided_code import L

# length = len(L)

# sorted_L = sorted(L)
# print (sorted_L[0])


while len(L) > 1:
    L.remove(min(L))
LIST_MAX = L[0]
