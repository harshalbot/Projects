user_input = raw_input('Want to find the next immediate prime number? Reply in Y or N: ')

user_input = user_input.lower()

i = 3
a = 2

def is_prime(i):
	while i > a :
		if i%a==0 & a!=i:
		 	break
		 	
    
  		else: 
  			print(i)
  			i += 1


if user_input == 'y':
	is_prime(i)
else:
	print('Thank you')






