odd_list = []
pair_list = []

def pair_odd(*args):
    for arg in args:
        if arg % 2 == 0:
            pair_list.append(arg)
        else:
            odd_list.append(arg)
    return pair_list, odd_list

print(pair_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(f'Pair Numbers: {pair_list}')
print(f'Odd Numbers: {odd_list}')