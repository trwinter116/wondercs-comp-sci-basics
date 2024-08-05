# %%
import pathlib
import urllib.request

with open("test.txt", "w") as myfile:
    myfile.write("My first file written from Python\n")
    myfile.write("#---------------------------------#\n")
    myfile.write("Hello, world!\n")

# %%
with open("test.txt", "r") as mynewhandle:
    while True:  # Keep reading forever
        theline = mynewhandle.readline()  # Try to read next line
        if len(theline) == 0:  # If there are no more lines
            break  # leave the loop

        # Now process the line we've just read
        print(theline, end="")

# %%
content = pathlib.Path("test.txt").read_text()
words = content.split()
print("There are {0} words in the file.".format(len(words)))


# %%
def filter(oldfile, newfile):
    with open(oldfile, "r") as infile:
        outfile = open(newfile, "w")
        while True:
            text = infile.readline()
            if len(text) == 0:
                break
            if text[0] == "#":
                continue

            # Put any more processing logic here
            outfile.write(text)

    outfile.close()


# %%
filter("test.txt", "test2.txt")


# %%


url = "https://www.ietf.org/rfc/rfc793.txt"
destination_filename = "rfc793.txt"

urllib.request.urlretrieve(url, destination_filename)


# %%
def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta


the_text = retrieve_page("https://www.ietf.org/rfc/rfc793.txt")
print(the_text)


# %%
