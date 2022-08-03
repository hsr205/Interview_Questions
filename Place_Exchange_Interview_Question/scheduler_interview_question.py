# Task:  Write a function which takes the input below and provide the expected output.
# Input: List of schedules (times when people are *not available*)
# Output: provide a list of times when everyone *is available* for a meeting

# Example input:

# [

# [ [4,5],[6,10],[12,14]], //  Person A busy

# [ [4,5],[5,9],[13,16]], // Person B busy

# [ [11,14]] // Person C busy

# ]


# Example Output:

# [[0,4],[10,11],[16,24]]


emp_hours = [
    [[4, 5], [6, 10], [12, 14]],
    [[4, 5], [5, 9], [13, 16]],
    [[11, 14]]
]


def create_hour_range():
    list_obj = []
    for i in range(25):
        list_obj.append(0)
    return list_obj


hours_in_the_day = create_hour_range()


def get_busy_hour_ranges():
    hour_ranges = []

    for i in emp_hours:
        for j in i:
            hour_ranges.append(range(j[0], j[1]))

    return hour_ranges


hour_ranges = get_busy_hour_ranges()


def indicate_busy_hours(ranges, hours_list):
    for i in ranges:
        for j in i:
            hours_list[j] = 1
    return hours_list


hours_in_the_day = indicate_busy_hours(hour_ranges, hours_in_the_day)

free_hours = [i for i, x in enumerate(hours_in_the_day) if x == 0]

# print(f'hours_in_the_day: {hours_in_the_day}')
# print(f'free_hours: {free_hours}')

busy_hour = []
for i in range(len(free_hours)):
    try:
        if free_hours[i] < free_hours[i + 1]:
            busy_hour.append(free_hours[i] + free_hours[i] + 1)
            print(f'{free_hours[i]}, {free_hours[i] + 1}')
    except:
        pass
