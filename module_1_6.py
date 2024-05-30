def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=23)
print_params(a=23, b='string')
print_params(a=23, b='string', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 2.5, 'number']
values_dict = {'a': 5, 'b': False, 'c': 'sun'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 2343]

print_params(*values_list_2, 23)
