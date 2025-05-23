# Currying is the process of transforming a function that takes multiple arguments into a sequence of functions, each taking one argument.
	
	# a closure is a function that "closes over" its surrounding state—it retains access to the variables in its scope even after the outer function has returned.
	
def example() :
    outer = 23
    print("outer function")
    def inner_function(a, b) :
        print("Inner function", a, b)
	    print("outer scoped variable", ++outer)
	    return outer * a * b
    return inner_function
inner = example()
print(inner(2, 3))