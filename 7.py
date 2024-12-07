import time

with open("7.txt", "r") as myfile:
    data = myfile.readlines()

def brute(numbers, target, current_result=0, current_index=0, part_two=True):
    
    # base case, we're at the end of the list
    if current_index == len(numbers):
        return current_result == target
    # optimization, if result is already over target, stop recursion
    if current_result > target:
        return False
    # walk through the list of numbers
    current_number = numbers[current_index]
    # try addition
    if brute(numbers, target, current_result + current_number, current_index + 1, part_two):
        return True
    # try multiplication
    if brute(numbers, target, current_result * current_number, current_index + 1, part_two):
        return True
    # try concatenation, only required for part two
    if part_two and current_result != 0:
        concatenated_result = int(str(current_result) + str(current_number))
        if brute(numbers, target, concatenated_result, current_index + 1):
            return True

    return False

def main():
    time_start = time.time()
    total_part_one = 0
    total_part_two = 0
    for line in data:
        equation = line.strip().split(":")
        desired_result = int(equation[0])
        factors = [int(n) for n in equation[1].strip().split(" ")]
        is_result_possible_part_one = brute(factors, desired_result, part_two=False)
        if is_result_possible_part_one:
            total_part_one += desired_result
        else:
            is_result_possible_part_two = brute(factors, desired_result, part_two=True)
            if is_result_possible_part_two:
                total_part_two += desired_result


    print(total_part_one)
    print(total_part_one+total_part_two)
    print("Time taken: {:.6f}s".format(time.time() - time_start))

if __name__ == "__main__":
    main()