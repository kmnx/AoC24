with open("2.txt", "r") as myfile:
    content = myfile.readlines()

safe_reports = 0
unsafe_reports = 0


# error dampening, remove values at current and possibly previous and or following index
def error_dampened(og_line, retest_index):
    newlines = []
    # new line without value at current index
    new_test_line_one = [n for n in og_line]
    del new_test_line_one[retest_index]
    newlines.append(new_test_line_one)
    # new line without value at following index
    if retest_index + 1 < len(og_line):
        new_test_line_two = [n for n in og_line]
        del new_test_line_two[retest_index + 1]
        newlines.append(new_test_line_two)
    # new line without value at previous index
    if retest_index - 1 > -1:
        new_test_line_three = [n for n in og_line]
        del new_test_line_three[retest_index - 1]
        newlines.append(new_test_line_three)

    if any(is_safe(line) for line in newlines):
        return True
    else:
        return False


# test if a given line fullfills the constraints
def is_safe(numberline):
    direction = ""
    for index, number in enumerate(numberline):
        # if we reached the end of the line without errors it must be safe
        if index == len(numberline) - 1:
            print(numberline, "is safe")
            return True

        # otherwise start checking
        current_number = int(number)
        next_number = int(numberline[index + 1])

        # set the expected direction at position 0
        if index == 0:
            if next_number > current_number:
                direction = "ascending"
            elif next_number < current_number:
                direction = "descending"
            else:
                return False

        # check constraints
        if (
            (abs(current_number - next_number) > 3)
            or (next_number > current_number and direction != "ascending")
            or (next_number < current_number and direction != "descending")
            or (next_number == current_number)
        ):
            return False
        else:
            continue


for line in content:
    direction = ""
    splitline = line.split()
    if is_safe(splitline):
        safe_reports += 1

    else:
        # line wasn't safe, check every position and generate error dampened lines
        for index, number in enumerate(splitline):
            current_number = int(number)
            print(splitline)
            print(index, number)
            next_number = int(splitline[index + 1])

            # set the direction
            if index == 0:
                if next_number > current_number:
                    direction = "ascending"
                elif next_number < current_number:
                    direction = "descending"
                else:
                    if error_dampened(splitline, index):
                        safe_reports += 1
                        break
                    else:
                        unsafe_reports += 1
                        break

            # try error_dampening if
            # distance > 3 or
            # distance == 0 or
            # expected direction of number progression changed
            if (
                abs(current_number - next_number) > 3
                or (next_number == current_number)
                or (next_number > current_number and direction != "ascending")
                or (next_number < current_number and direction != "descending")
            ):
                if error_dampened(splitline, index):
                    safe_reports += 1
                    break
                else:
                    unsafe_reports += 1
                    break


print(safe_reports)
