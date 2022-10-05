"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
age = input("Please enter your age: ")

max_rate = 220 - int(age)

lower_bounds = .65 * max_rate
upper_bounds = .85 * max_rate

print(f'When you exercise to strengthen your heart, you should \nkeep your heart rate between {lower_bounds:.0f} and {upper_bounds:.0f} beats per minute.')


