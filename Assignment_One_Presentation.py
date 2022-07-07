
'''
    The first function is 'greeting' which presents the user with simple
    instructions. The next function, getInput, prompts the user to enter
    an integer.  In this function, I'm doing some error-handling to
    catch any keystrokes that are not integers.  The getPrimes function is
    used to calculate the Prime numbers, basically taking input from the
    getInput function.  In the doCalculation function, the inputs are the
    original number entered, and the list of prime numbers.

    To explain this
    function, inside the While loop, which loops until the number is 0, and
    we're subtracting by 2 because we're calculating for even numbers. Now,
    inside the while loop, our for statement will take the original number
    and subtract every prime number from it... if the product is in our
    list of prime numbers, then we can add that product to the first prime
    number in our list and we will keep the first number that equals our
    original even number.  These are then stored in a list, but reversed
    because the list is populated with the smallest numbers, which would
    then print the smallest numbers and then the largest... 
    our example displays the list by printing them from largest to smallest.
    The last function is to accept the list and print it.
