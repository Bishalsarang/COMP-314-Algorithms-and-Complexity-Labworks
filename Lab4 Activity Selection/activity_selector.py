# Author: Bishal Sarang

def select_activity_r(s, e, j):
    """
		Recursive activity selector
		
        Args:
			s(list): start time of activities
            e(list): end time of activities
            j(int): index to be incuded in the selected_activites
		Returns:
			list: index of activities to be selected
		"""
    
    # Start pointer from the next index
    i = j + 1

    # While no compatible activity is found search
    while i < len(s) and s[i] < e[j]:
        i += 1
    
    # If we are at the end of the list, we include the current optimal activity
    if i == len(s):
        return [j]
    # Else we include the current optimal activity and recursively find solution for remaining part of array
    return [j] + select_activity_r(s, e, i)



def select_activity_i(s, e):
    """
		Iterative  activity selector
		
        Args:
			s(list): start time of activities
            e(list): end time of activities
		Returns:
			list: index of activities to be selected
	"""
    
    # Select the first activity i.e the activity which finishes the earliest
    selected_activities = [0]

    # CUrrent selected activity
    j = 0

    # Start searching for compatible activity from index 1 to len of array
    for i in range(1, len(s)):
        # If activity i and j are compatible
        # i.e end time of current selected activity do not overlap with start time of activity to be selected
        # We select the activity
        # Set selected activity j = i 
        if s[i] >= e[j]:
            selected_activities.append(i)
            j = i
    return selected_activities 


def main():

    # Start and end times of activities
    s, e =  [1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]
    
    # Sort all the activities based on finish time
    # i.e choose activity that finishes the earliest
    zipped = list(zip(s, e))
    sorted_activities = sorted(zipped, key=lambda x: x[1])
    s = [x[0] for x in sorted_activities]
    e = [x[1] for x in sorted_activities]

    # Select index so as to maximize activities
    # USing iterative version
    selected_activities_index = select_activity_i(s, e)
    print("The optimal schedule by iterative version is as follows: ")
    for i in range(len(selected_activities_index)):
        print(f"{s[i]} - {e[i]}")

    # USing recursive version
    selected_activities_index = select_activity_r(s, e, 0)
    print("The optimal schedule by recursive version is as follows: ")
    for i in range(len(selected_activities_index)):
        print(f"{s[i]} - {e[i]}")

if __name__ == "__main__":
    main()