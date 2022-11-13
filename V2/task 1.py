from pprint import pprint
len_number = 15
list_ = [{'bin': bin(number),
          'dec': number,
          'hex': hex(number),
          'oct': oct(number)} for number in range(len_number+1)]

pprint(list_)