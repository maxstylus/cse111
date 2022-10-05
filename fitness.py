# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime

"""
Please enter your gender (M or F): F
Enter your birthdate (YYYY-MM-DD): 2001-03-21
Enter your weight in U.S. pounds: 125
Enter your height in U.S. inches: 54
Age (years): 19
Weight (kg): 56.70
Height (cm): 137.2
Body mass index: 30.1
Basal metabolic rate (kcal/day): 1315
"""


def main():
    # Get the user's gender, birthdate, weight, and height.
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    weight = input("Enter your weight in U.S. pounds: ")
    height = input("Enter your height in U.S. inches: ")

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate)

    weight_in_kilograms = kg_from_lb(weight)
    heigh_in_centimeters = cm_from_in(height)

    bmi = body_mass_index(weight_in_kilograms, heigh_in_centimeters)
    basal = basal_metabolic_rate(gender, weight_in_kilograms, heigh_in_centimeters, age)

   # Print the results for the user to see.
    print(f"Age (years): {str(age)}")
    print(f"Weight (kg): {str(weight_in_kilograms)}")
    print(f"Height: (cm): {str(heigh_in_centimeters)}")
    print(f"Body mass index: {str(bmi)}")
    print(f"Basal metabolic rate (kcal/day): {str(basal)}")


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.

    1 lb = 0.45359237 kg
    """
    pounds = float(pounds)
    llbs_to_kg = .45359237

    return round(pounds * llbs_to_kg, 2)


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.

    1 in = 2.54 cm
    """
    inches = float(inches)
    cm_per_inch = 2.54

    centimeters = round(inches * cm_per_inch, 1)

    return centimeters


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * weight) / (height * height)
    return round(bmi, 1)


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    age = int(age)

    if gender == "F":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) 

    return bmr

# Call the main function so that
# this program will start executing.
main()