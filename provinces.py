def main():
    # Read the contents of a text file
    # named provinces.txt into a list.
    provinces_list = read_list("provinces.txt")

    # Print the entire list.
    print()
    print(provinces_list)

    # Remove the first element
    provinces_list.pop(0)

    # Remove the last element from the list
    provinces_list.pop(-1)

    # Replace all occurrences of "AB" in the list with "Alberta"
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'

    # Count the number of elements that are "Alberta" and print that number.
    alberta_count = 0
    for province in provinces_list: 
        if province == "Alberta":
            alberta_count += 1

    print()
    print(f"Alberta occurs {alberta_count} times in the provinces list.")

    print()
    print(provinces_list)

def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    provinces_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            provinces_list.append(clean_line)

    # Return the list that contains the lines of text.
    return provinces_list


# Call main to start this program.
if __name__ == "__main__":
    main()