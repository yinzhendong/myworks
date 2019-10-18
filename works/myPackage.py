def _private_1(name):
    return 'Hello, {}'.format(name)

def _private_2(name):
    return 'Hi, {}'.format(name)

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


print(greeting('Yin'))

print(greeting('Trent'))