# from functools import cmp_to_key

# Activity class to store start and finish time
class Activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

# Function to perform activity selection
def activity_selection(start, finish):
    n = len(start)  # Number of activities

    # Create an array of activities
    activities = [Activity(start[i], finish[i]) for i in range(n)]

    # Sort activities by finish time
    activities.sort(key=lambda x: x.finish)
    a = []
    b = []
    for i in activities:
        a.append(i.start)
        b.append(i.finish)
    print('Sorting order:')
    print("Start: ",a)
    print("Finish: ",b)
    print()
    # Select the first activity
    print("Selected activities:")
    print(f"({activities[0].start}, {activities[0].finish})")
    last_finish_time = activities[0].finish

    # Iterate over the remaining activities
    for i in range(1, n):
        # If this activity's start time is >= the last selected activity's finish time
        if activities[i].start >= last_finish_time:
            print(f"({activities[i].start}, {activities[i].finish})")
            last_finish_time = activities[i].finish  # Update the last finish time

if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    activity_selection(start, finish)
