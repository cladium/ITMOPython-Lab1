FILENAME = "sequence.txt"

def get_numbers(filename = FILENAME):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    # skip lines that cannot be converted to a float
                    continue
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")  
    return numbers

def get_ratio(numbers):
    less_than_minus_five = 0
    more_than_minus_five = 0
    for n in numbers:
        if n < -5:
            less_than_minus_five += 1
        elif n <= 0:
            more_than_minus_five += 1
    return less_than_minus_five, more_than_minus_five

def draw_diagram(name_a, name_b, count_a, count_b, symbol = '=', size = 40):
    size_a, size_b = 0, 0
    ratio = count_a / (count_a + count_b)
    if ratio < 0.5:
        size_b = size
        size_a = round(size * (count_a / count_b))
    else:
        size_a = size
        size_b = round(size * (count_b / count_a))
        
    print(f"{name_a}: {symbol * size_a} ({count_a})")
    print(f"{name_b}: {symbol * size_b} ({count_b})")

def main():
    numbers = get_numbers()
    ratio_data = get_ratio(numbers)
    draw_diagram('Less than -5', 'More than -5', ratio_data[0], ratio_data[1])

if __name__ == "__main__":
    main()