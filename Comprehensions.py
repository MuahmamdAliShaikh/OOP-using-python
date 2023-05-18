a=['apple','banana','mango','cheery','strawberry','peech']
b=[x for x in a if 'a' not in x]
print(b)
c={x for x in range(len(a))}
print(c)
#Generator comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)#using tuple
print("Output values using generator comprehensions:", end = ' ')
for var in output_gen:
	print(var, end = ' ')

# Using Dictionary comprehensions
# for constructing output dictionary
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dict_using_comp = {key:value for (key, value) in zip(state, capital)}
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)

# Using Dictionary comprehensions
# for constructing output dictionary
list1 = [1,2,3,4,5,6,7]
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:",dict_using_comp)
