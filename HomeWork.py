import logging

dictionary = {
    'Plo Kun': '104-battalion',
    'Obi Van Kenobi': '212-battalion'
}


logging.basicConfig(filename='my_logs_h1.log', filemode='w', level=logging.DEBUG,
                    format='%(name)s %(levelname)s %(process)d %(asctime)s %(message)s')


def addition(jedi_name: str, unit: str) -> dict:
    try:
        dictionary[jedi_name] = unit
        return dictionary
    except TypeError:
        logging.warning('Something happened with addition')


def subtraction(jedi_name: str) -> dict:
    try:
        dictionary.pop(jedi_name)
        return dictionary
    except KeyError:
        logging.warning('Something happened with subtraction')


def multiplication(a: int, jedi: str) -> dict:
    try:
        return dictionary[jedi] * a
    except TypeError:
        logging.warning('Something happened with multiplication')


print(addition('Anakin Skywalker', '501-legion'))
print(addition(["someone", "something"], 'unknown_unit'))

print(subtraction('Plo Kun'))
print(subtraction(4))

print(multiplication(5, 'Anakin Skywalker'))
print(multiplication('someone', 'Anakin Skywalker'))
