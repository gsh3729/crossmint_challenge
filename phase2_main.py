import process
import helper

goal_data = helper.get_goal_data()
if goal_data is not None and goal_data['goal'] is not None:
    processed_data = process.process_data(goal_data['goal'])

    # to clear off the map, use the below line inplace of above line
    # processed_data = process.process_data(goal_data['goal'], delete=True)
else:
    print("Failed to fetch goal data.")

