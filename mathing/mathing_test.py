from mathing import exercise1
from mathing import exercise2
from mathing import exercise3
from mathing import exercise4
from mathing import exercise5

# testing multiplication 
def test_multiplication():
    assert exercise1.multiplication(2,5) == 10

def test_multiplication():
    assert exercise1.multiplication(22,3) == 10

def test_multiplication():
    assert exercise1.multiplication(22,3) == 66

# testing factorial function
def test_factorial():
    assert exercise2.factorial(4) == 24

# Testing devision function
def test_devision():
    assert exercise3.devision(5,2) == 2.5

# Testing Fibonacci Sequence
#def test_fibonacci():
#   assert exercise4.fibonacci(1) == True
#   assert exercise4.fibonacci(6) == False

#def test_fibonacci():
#   assert exercise4.fibonacci(1) == 0

def test_fib():
    assert exercise5.fib(2) == 1

def test_fib():
    assert exercise5.fib(6) == 8
 


