# %%
# Debug this version of the function, there are some semantic and some syntax errors.
# Work through them to get it working as the example function does.

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
        else:  # Do something useful with the file]

            key = f.lower()  # Normalize the filename
            if key in files_dict:
                files_dict[key].append(fullname)
            else:   # insert the key and a list of one pathname
                files_dict[key] = [fullname]

            file_count + 1
            if file_count // 100 == 0:
                print(".", end="")
                if file_count % 5000 == 0:
                    print()


crawl_files(Path.cwd().parent.parent)

print()  # End the last line of dots ...
print "Crawling completed!"
print("Indexed {0} files, {1} entries in the dictionary.".
                    format(file_count, len(files_dict)))

# %%
