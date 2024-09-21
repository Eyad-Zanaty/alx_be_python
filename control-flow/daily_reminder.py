task = input("What is your task? ")
task_priority = input("What is the task priority? (high / medium / low) ")
time_bound = input("Is it time bound ? (yes / no) ")
match time_bound :
    case "yes":
        print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
    case "no":
        print(f"Note: '{task}' is a {task_priority} priority task. Consider completing it when you have free time.")        