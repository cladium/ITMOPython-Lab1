import math

FILENAME = "sequence.txt"
COLOR_A = "\033[91m"  # red for group A
COLOR_B = "\033[94m"  # blue for group B
RESET = "\033[0m"

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

def draw_pie_chart(name_a, name_b, count_a, count_b, radius = 12):
    angle_a = (count_a / (count_a + count_b)) * 360
    
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            distance = math.sqrt(i**2 + j**2)
            if distance < radius:
                # calculate the angle for the point
                angle = (math.degrees(math.atan2(i, j)) + 360) % 360
                if angle < angle_a:
                    print(f"{COLOR_A}x", end="")
                else:
                    print(f"{COLOR_B}x", end="")
            else:
                print(" ", end="")
        print(RESET)

    print(f"{COLOR_A}{name_a}: {count_a} {RESET}")
    print(f"{COLOR_B}{name_b}: {count_b} {RESET}")


def main():
    numbers = get_numbers()
    ratio_data = get_ratio(numbers)
    draw_diagram('Less than -5', 'More than -5', ratio_data[0], ratio_data[1])
    draw_pie_chart('Less than -5', 'More than -5', ratio_data[0], ratio_data[1])
    
if __name__ == "__main__":
    main()