def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
        print()
        print('!')
        print()
        
    return wrapper

@logger
def sample():
    print('--Inside sample function')

@logger
def pineapple_treatment():
    print('--Eat pineapple pizza!!')


sample()

pineapple_treatment()

