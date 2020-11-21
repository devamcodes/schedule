"""
Scope: Collect the data from the user and store it in one line
"""

name = input("Enter your name:")
start = input("Enter your start time:")
end = input("Enter your end time:")
status = "dev"

def add_schedule(name, start, end, status):

    with open ('schedule.txt', 'a') as file:
        file.write(f'{name}, {start}, {end}, {status}\n')





add_schedule(name, start, end, status)
