def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(1111)
print_params(None, False, 'piton')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [112, True, "Hello"]
values_dict = {"a":112, "b":True, "c":"Hello" }
print(values_dict)
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["LOL", 1222]
print_params(*values_list_2, 42)