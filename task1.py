from pprint import pprint

dictlist = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]

pprint(dictlist)
