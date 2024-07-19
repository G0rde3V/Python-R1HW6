my_dict = {'Алексей': 1985, 'Андрей': 1991, 'Анастасия': 1998}
print(my_dict)
print(my_dict['Андрей'])
print(my_dict.get('Влад'))
my_dict.update({'Юля': 1989, 'Олег': 1993})
print(my_dict)
del my_dict['Анастасия']
print(my_dict)
my_set = {'Юрий', 3, 5, 4.7}
print(my_set)
my_set.update({'Илья', 9.1})
print(my_set)
print(my_set.discard(3))
print(my_set)