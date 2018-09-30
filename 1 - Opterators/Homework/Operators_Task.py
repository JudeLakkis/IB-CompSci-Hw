# Task 1
task1_list = [(9 % 7),(8 * 4 - 4),bool(4/4),(abs(-1)) * 4 + 10,4 % 3,20 - int(14.5),
			  bool(10 - (int(2.2) * 5)),divmod(19,4),str((13 - 10) * 10 + (10 / 5)),
			  float(15%4 - int(True))]

for i in range(len(task1_list)):
	print('Part:', i+1)
	print(task1_list[i],'\n')

# Task 2
print('Task 2:\nint\n')

# Task 3
print('Task 3:\nBoolean\n')

# Task 4
print('Task 4:\nvar1 += 1\n')
# Benifits:
# Significantly faster to type than possibly very long var. names

# Task 5
task5_list = [2>1 and 3<4, len('hi') < 3, 6<8 or 12>10, not(7>10), 5>6 and 7<8, not(5>7 and 8<6),
			  10/2==5 and 'a' != 'b', 10/2!=5 and 'a' == 'b']

for i in range(len(task5_list)):
	print('Part:', i+1)
	print(task5_list[i],'\n')

# Task 6
	# Part a
a = 10
b = 100 - 1
print('Part a:\na =',a, 'b =',b)
	
	# Part b
var1 = 100
var2 = 50
print('Part b:\n',var1 + 10)

	# Part c
a = 'hi'
b = 'bye'
a += a + b
a *= 2
print('Part c:\n',a)

	# Part d
my_name = 'Mr.Bach'
your_name = 'Mr.Student'
print('Part c:\n',my_name + ' or ' + your_name + '?')

	# Part e
this_val = False
that_val = True
some_val = 0
this_val +=1
print(this_val)
that_val = False
this_val = False
print(some_val + 0)

# Task 7
def quadratic(a,b,c):
	answer_plus = -b+(b**2-4*a*c)**0.5
	answer_mins = -b-(b**2-4*a*c)**0.5
	answer1 = answer_plus/2*a
	answer2 = answer_mins/2*a
	print(answer1, answer2)

# Task 8
def logic_gate(a,b,c):
	part1 = a and b
	part2 = not(a and c)
	answer = (part1 or part2)
	print(answer)

a = 1
b = 1
c = 1
logic_gate(a,b,c)

a = 1
b = 2
c = 3
quadratic(a,b,c)
