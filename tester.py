from functools import wraps


def deco(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Doing the thing')
        print('args: ',*args)
        print('kwargs: ', **kwargs)
        return f(*args, **kwargs)
    return wrapper

@deco
def potato(a, b='carrots'):
    print('potato + ', b)


if __name__ == '__main__':
    potato(1, 'beans')