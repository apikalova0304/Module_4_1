calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(name):
    count_calls()
    return tuple([len(name), name.upper(), name.lower()])

def is_contains(arg, arg_2):
    count_calls()
    arg_2 = [word.lower() for word in arg_2]
    return arg.lower() in arg_2

print(string_info('Alina'))
print(string_info('Urban'))
print(string_info('krestiki-noliki'))
print(is_contains('AliNA', ['ALina', 'Eva', 'Max']))
print(is_contains('Egor', ['EvA', 'AliNa', 'MAX']))
print(is_contains('Mama', ['MAMA', 'PApa', 'URBAN']))
print(calls)