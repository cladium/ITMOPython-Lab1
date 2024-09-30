def print_pattern(x = 1, y = 1):
    pattern = [
        "  /\\    /\\  ",
        " /  \\  /  \\ ",
        "/    \\/    \\",
        "\\    /\\    /",
        " \\  /  \\  / ",
        "  \\/    \\/  "
    ]
    
    for i in range(y):
        for line in pattern:
            print(line*x)
            
print_pattern(4, 5)