def find_poison_bottle():
    # Total number of bottles and people
    bottles = 1000
    people = 10

    # Creating a list of 10 people
    testers = [0] * people

    # Assigning each bottle to a combination of testers
    for bottle in range(1, bottles + 1):
        binary = format(bottle, '010b')  # Convert bottle number to binary
        for i in range(people):
            if binary[i] == '1':
                testers[i] = testers[i] | (1 << bottle)

    # Simulating which people are poisoned
    poisoned_people = [0] * people  # Replace with actual poisoned people data
    print("Poison's Data",)


# final example example
def find_poison_bottle(poisoned_people):
    """
    Determines which bottle contains poison based on poisoned people.

    Parameters:
        poisoned_people (list): List of poisoned testers (indices start from 0).
    
    Returns:
        int: Bottle number that contains poison.
    """
    bottle_number = 0
    for i, is_poisoned in enumerate(poisoned_people):
        if is_poisoned:
            bottle_number += 2 ** i
    return bottle_number


# Simulating the testing process
def simulate_test():
    bottles = 1000
    people = 10
    poison_bottle = 567  # Let's assume bottle 567 contains poison
    
    # Representing which testers drink from which bottles
    testers = [0] * people
    for bottle in range(1, bottles + 1):
        binary = format(bottle, '010b')  # Binary representation of the bottle
        for i in range(people):
            if binary[9 - i] == '1':  # Assign bottle to the corresponding tester
                testers[i] = testers[i] | (1 << (bottle - 1))
    
    # Simulating poisoned testers
    poisoned_people = [0] * people
    binary_poison_bottle = format(poison_bottle, '010b')
    for i in range(people):
        if binary_poison_bottle[9 - i] == '1':
            poisoned_people[i] = 1

    # Finding the poison bottle
    detected_poison_bottle = find_poison_bottle(poisoned_people)
    return poison_bottle, detected_poison_bottle


# Run the simulation
actual, detected = simulate_test()
print(f"Actual poison bottle: {actual}")
print(f"Detected poison bottle: {detected}")
