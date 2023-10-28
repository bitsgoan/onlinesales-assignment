#TASK3
##HOW TO RUN THE CODE: Overall there is 1 input below. Change this and run. YOu may uncomment the test cases as well
n = 5

#Assumption1 - Calculate the sum of all integers between 1 and (n-20).
#Included means both 1 and (n-20) included
#Note 2 - The output in case 3 will always be float. We may convert it to int

def compute(n):
    if n < 10:
        out = n ** 2
    #Change 1 - Include equal to 20 to make sure 20 is include in the second case
    elif n <= 20:
        out = 1
        #Change2 - 1+ n-10 to because python runs the loop excluding last value
        for i in range(1, 1+n-10):
            out *= i
    #Change3 - To make the formula n(n+1)/2
    else:
        lim = n - 20
        out = lim * lim
        out = out + lim
        out = out / 2 
    #print(out)
    return out
    #Return helps in testing the test cases

compute(n)
#Total 3 changes were required to be done


#For the debugging problem, mention all the edge cases you have tested for and the corresponding fixes.
#Tested for 
# case 1 => n = 10, 11, 12 => 12 should run for (1, 2), so made the change to alter "range(1,n-10) to range(1, 1+n-10))"
# case 2 => n = 19, 20, 21 => 20 should come in the second case, hence the change1

#TEST CASES
import math

def test_compute():

    # Test for n < 10: Should return n^2
    assert compute(5) == 25
    assert compute(2) == 4
    assert compute(9) == 81

    # Test for 10 <= n <= 20: Should return (n - 10)!
    assert compute(10) == math.factorial(0)  # 0!
    assert compute(12) == math.factorial(2)  # 0!
    assert compute(11) == math.factorial(1)  # 0!
    assert compute(15) == math.factorial(5)  # 5!
    assert compute(20) == math.factorial(10) # 10!

    # Test for n > 20: Should return lim * (lim + 1) / 2
    assert compute(21) == 1 * 2 / 2   # 1
    assert compute(25) == 5 * 6 / 2   # 15
    assert compute(30) == 10 * 11 / 2 # 55

    print("All tests passed!")

# Run the tests
test_compute()
