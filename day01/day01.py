def day_one(file_path, modify_function=None):
    total = 0
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            modified_line = modify_function(line) if modify_function else line
            line_list = list(modified_line)
            digit_list = [int(x) for x in line_list if x.isdecimal()]
            line_value = ((10 * digit_list[0]) + digit_list[-1])
            #debug: print(line, modified_line, digit_list, line_value)
            total += line_value

    return(total)

def replace_number_strings_with_digits(line):
    #cant just replace with digit as a char might be in two number strings - e.g. eightwothree
    return line.replace('one','o1e').replace('two','t2o').replace('three','t3e').replace('four','f4r').replace('five','f5e').replace('six','s6x').replace('seven','s7n').replace('eight','e8t').replace('nine','n9e')

print(day_one('day01//day01.txt'))
print(day_one('day01//day01.txt', replace_number_strings_with_digits))