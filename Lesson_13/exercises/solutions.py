# Exercise 1
# Write a function which reads a file and writes out a new file with the lines in reversed
# order (i.e. the first line in the old file becomes the last one in the new file.)

def reverse_file(old_file_name, new_file_name):
    contents = []
    with open(old_file_name, "r") as fh:
        while True:
            line = fh.readline()
            if len(line) == 0:
                break

            contents.append(line)

    contents.reverse()

    with open(new_file_name, "w") as fh:
        for line in contents:
            fh.write(line)


# Exercise 2
# Write a function that reads a file and prints only those lines that contain the substring
# 'snake'.

def extract_snake_lines(snake_file_name):
    with open(snake_file_name, 'r') as file:
        for line in file:
            if "snake" in line.lower():
                print(line)


# Exercise 3
# Write a function that reads a text file and produces an output file which is a copy of
# the file, except the first five columns of each line contain a four digit line number,
# followed by a space. Start numbering the first line in the output file at 1. Ensure that
# every line number is formatted to the same width in the output file.

def add_line_numbers(old_file_name, new_file_name):
    with (open(old_file_name, 'r') as input_f, open(new_file_name, 'w') as output_f):
        for line_number, line in enumerate(input_f, start=1):
            line_number_str = str(line_number).zfill(4)
            output_line = f"{line_number_str} {line}"
            output_f.write(output_line)
