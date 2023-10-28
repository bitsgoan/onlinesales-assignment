Use a python IDE

## Task 1
HOW TO RUN THE CODE: Overall there are 2 inputs - input_dict and number of tries.

Change these two variables below and run the task on a python IDE
  input_dict = { 1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
  tries = 100000

Running code: snapshot: ![image](https://github.com/bitsgoan/onlinesales-assignment/assets/25197103/8f7ff523-8308-4186-a24b-8ee5445f06fa)


## Task 2
HOW TO RUN THE CODE: Overall there is one input - expressions.

Brief of what the code does:
#Step 1 - variable 'expressions' is passed
#Step 2 - We calculate the max requests we can take and alter the requests to take the first 'max requests' expressions 
#Step 3 - We break this expressions into chunks of 50
#Step 4 - We initiate as many processes as these chunks
#Step 5 - We take each process which will have max 50 expressions, and create max 50 threads to make sure these expressions are called parallelly

Expression should be a list of strings.

Running Code Snapshot: ![image](https://github.com/bitsgoan/onlinesales-assignment/assets/25197103/00c1bbeb-fabc-4b53-8793-0068041fc4cd)


## Task 3
HOW TO RUN THE CODE: Overall there is 1 input (n = 5). Change this and run. 

Running Code snapshot: ![image](https://github.com/bitsgoan/onlinesales-assignment/assets/25197103/d970cdb9-5013-4026-b4db-10c7dfbf3561)

Assumption1 - Calculate the sum of all integers between 1 and (n-20). ==> Included means both 1 and (n-20) included
#Note 2 - The output in case 3 will always be float. We may convert it to int
