# %%
import json
import os
from pathlib import Path

# Part 2
files_dict = {}

# Part 3
file_count = 0


def crawl_files(path):
    """ Recursively visit all files in path """

    global file_count

    # Fetch all the entries in the current folder.
    dirlist = os.listdir(path)
    for f in dirlist:
        # Turn each name into full pathname
        fullname = os.path.join(path, f)

        # If it is a directory, recurse.
        if os.path.isdir(fullname):
            crawl_files(fullname)
        else:  # Do something useful with the file
            #print("{0:30} {1}".format(f, fullname))

            # Part 2
            # Write code to normalize the filename, and either append the path to a global
            # dictionary for that file name, or create a new entry.
            key = f.lower()  # Normalize the filename
            if key in files_dict:
                files_dict[key].append(fullname)
            else:   # insert the key and a list of one pathname
                files_dict[key] = [fullname]

            # Part 3
            # Write code here to display a progress bar, for every 100 files print a "."
            # with no line breaks after it. For every 5000 files, create a new line with
            # an empty print..
            file_count += 1
            if file_count % 100 == 0:
                print(".", end="")
                if file_count % 5000 == 0:
                    print()



crawl_files(Path.cwd().parent.parent)
# Part 3
print()  # End the last line of dots ...
print("Indexed {0} files, {1} entries in the dictionary.".
                    format(file_count, len(files_dict)))

# %%

len(files_dict)

# %%

files_dict["example1.py"]

# %%

files_dict["main.py"]

# %%

with open("./mydict.txt", "w") as f:
    json.dump(files_dict, f)

# %%

with open("./mydict.txt", "r") as f:
    json_dict = json.load(f)
print("Loaded {0} filenames for querying.".format(len(json_dict)))


def query(filename):
    f = filename.lower()
    if f not in json_dict:
        print("No hits for {0}".format(filename))
    else:
        print("{0} is at ".format(filename))
        for p in json_dict[f]:
            print("...", p)


# %%

query("base_game.py")

# %%

query("README1.md")

# %%

