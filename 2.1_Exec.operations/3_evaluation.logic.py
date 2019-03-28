# Логические операторы И, ИЛИ, НЕ

a = True
b = False

#AND
print('AND Logic:')
print('a AND a:', a and a)
print('a AND b:', a and b)
print('b AND b:', b and b)

#OR
print('\nOR Logic:')
print('a OR a:', a or a)
print('a OR b:', a or b)
print('b OR b:', b or b)

#NOT
print('\nNOT Logic:')
print('a =', a, '\tnot a=', not a) #False
print('b =', b, '\tnot a=', not b) #True