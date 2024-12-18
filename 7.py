def do_something(target, accumulate_value, values, position):
    position += 1
    if position == len(values):
        return accumulate_value == target
    return (
        do_something(target, accumulate_value + values[position], values, position)
        or do_something(target, accumulate_value * values[position], values, position)
        or do_something(
            target, int(f"{accumulate_value}{values[position]}"), values, position
        )
    )


count = 0
with open("input7") as file:
    for line in file:
        [result, rest] = line.strip().split(":")
        result = int(result)
        values = [int(i) for i in rest.split()]

        possible = do_something(result, values[0], values, 0)

        if possible:
            count += result

print(count)
