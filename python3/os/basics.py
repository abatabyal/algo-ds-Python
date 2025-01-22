import os

print(os.name)
try:
    try:
        raise ValueError('1')
    except Exception as e:
        print(e)
        raise ValueError('1')
except Exception as e:
    print(e)
    raise ValueError('x')