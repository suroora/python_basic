s = {"red", 'blue', 2, 'car', 'cat', 313, 786, 'aizaan', 'pet'}
u = {'yellow', 'pen', 2, 313, 'pencil', 'car', 'pet'}
s.add("kerala")
s.remove('blue')
s_u = s | u
u_s =s & u
print(s)
print(s_u)
print(u_s)
