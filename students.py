""" Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each I-Number name pair or each name as a value in the dictionary.
Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
If a user enters an I-Number that doesn't exist in the dictionary, your program must print the message, "No such student" (without the quotes). """

import csv

def main():
    # Index of the phone number column
    # in the dentists.csv file.
    I_NUMBER_INDEX = 0
    STUDENT_NAME_INDEX = 1

    # Read the contents of the dentists.csv into a
    # compound dictionary named dentists_dict. Use
    # the phone numbers as the keys in the dictionary.
    students_dict = read_dict("students.csv", I_NUMBER_INDEX)

    i_num = input("Please enter your student I-Number: ")
    student_name = students_dict[i_num][STUDENT_NAME_INDEX]
    print(f"Student Name: {student_name}")


    # Print the dentists compound dictionary.
    #print(students_dict)


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()