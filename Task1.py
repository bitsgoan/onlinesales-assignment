##HOW TO RUN THE CODE
#Overall there are 2 inputs - input_dict and number of tries - Change these two variables below and hit enter.
input_dict = { 1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
tries = 100000

#For test cases, I am taking a 15% error as acceptable range

#Get the data in the dict format, or convert the input in this dict format as below:
#I am assuming we get the input in dictionary format since the question specifies we get a map

import random

#Genrate a cumilative probability function
#Input ex: { 1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0} 
#Output ex: {1: (0, 0.1), 2: (0.1, 0.4), 3: (0.4, 0.55), 4: (0.55, 0.70), 5: (0.70, 1.0), 6: (1.0, 1.0)}
def generate_cumilative_dict(input_dict):
    cumilative_dict ={}
    total_occurences = sum(input_dict.values())
    
    if total_occurences !=1:
        for term in input_dict:
            input_dict[term] = (input_dict[term]/total_occurences)

    prob_start = 0 

    for term in input_dict:
        prob_end = prob_start + input_dict[term]
        cumilative_dict[term] = [prob_start, prob_end]
        prob_start = prob_end

    return cumilative_dict


#Function to get the event based on the cumilative dict. 
# It generates random number, and traverses through cumilative_dict to pick the event that occured. 
# This function will be used in the simulate function
#Input ex: {1: (0, 0.1), 2: (0.1, 0.4), 3: (0.4, 0.55), 4: (0.55, 0.70), 5: (0.70, 1.0), 6: (1.0, 1.0)}
#Output ex: 3 (term 3 occured)
def get_event(cumilative_dict):
    random_number = random.random()

    for term in cumilative_dict:
        start = cumilative_dict[term][0]
        end   = cumilative_dict[term][1]

        if start <= random_number < end:
            return term

#Initialise the results with all events being 0
#Get the randomised event based on cumilative dict and keep logging it in results, and return the results
#Input ex: {1: (0, 0.1), 2: (0.1, 0.4), 3: (0.4, 0.55), 4: (0.55, 0.70), 5: (0.70, 1.0), 6: (1.0, 1.0)}, 10000
#Output ex: {1: 992, 2: 2994, 3: 1481, 4: 1472, 5: 3061, 6: 0}
def simulate( cumilative_dict ,tries):    
    results = {term: 0 for term in cumilative_dict.keys()}
    for x in range(tries):
        term = get_event(cumilative_dict)
        results[term] += 1
    return results


#Taking care of the edge case of no events being possible, or 0 probability
try:
    
    cumilative_dict = generate_cumilative_dict(input_dict)

    if sum(input_dict.values()) == 0:
        print("Incorrect data. Total probaility/occurences cannot be 0")

    else:
        results = simulate(cumilative_dict, tries)

        #Print the required text
        print(f"On triggering the event {tries} times")
        for event, count in results.items():
            print(f"{event} appeared {count} times")
        print("which is roughly inline with the biasness given. This is just one of the possibilities.")

except TypeError:
    print("Incorrect Format. Check if the probability numbers or occurences are numbers or decimals")






# Test cases


def keys_within_percentage_range(d):
    """
    For every key-value pair, check if the key is within 15% of the value.
    If the sum of all keys is 0, raise a TypeError.
    """
    if sum(d.keys()) == 0:
        raise TypeError("Sum of all keys is zero.")
    
    for key, value in d.items():
        lower_bound = value - 0.15 * value
        upper_bound = value + 0.15 * value
        
        if not lower_bound <= key <= upper_bound:
            return False
    return True


def test_keys_within_percentage_range():
    # Test case 1: Input ex: { 1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0}
    # Expected: False, because 1 is not within 15% of 10
    assert not keys_within_percentage_range({1: 10, 2: 30, 3: 15, 4: 15, 5: 30, 6: 0})

    # Test case 2: All keys are exactly equal to their values
    # Expected: True
    assert keys_within_percentage_range({10: 10, 30: 30, 15: 15})

    # Test case 3: All keys are 15% more than their values
    # Expected: True
    assert keys_within_percentage_range({11.5: 10, 34.5: 30, 17.25: 15})

    # Test case 4: All keys are 15% less than their values
    # Expected: True
    assert keys_within_percentage_range({8.5: 10, 25.5: 30, 12.75: 15})

    # Test case 5: All keys are 16% more than their values
    # Expected: False
    assert not keys_within_percentage_range({11.6: 10, 34.8: 30, 17.4: 15})

    # Test case 6: Sum of all keys is zero
    # Expected: TypeError
    try:
        keys_within_percentage_range({0: 10, 0: 30, 0: 15})
        assert False  # This line should not be reached
    except TypeError:
        assert True

    print("All tests passed!")

test_keys_within_percentage_range()
