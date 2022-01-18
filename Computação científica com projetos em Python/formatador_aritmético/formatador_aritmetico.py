def arithmetic_arranger(problems, val=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems

    numbers = []
    operations = list(map(lambda x: x.split()[1], problems))    # list of all operations in str format
    top = ''
    bottom = ''
    dashes = ''
    results = list(map(lambda x: eval(x), problems))
    solutions = ''

    if set(operations) != {'+', '-'} and len(set(operations)) != 2:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems

    for p in problems:
        i = p.split()
        numbers.extend([i[0], i[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(results[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i-1]), len(numbers[i])) + 1
        bottom += operations[i // 2]
        bottom += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom += ' ' * 4
    if val:
        arranged_problems = '\n'.join((top, bottom, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top, bottom, dashes))
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))