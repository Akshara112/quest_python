'''User gives the data like this:
kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
You have to separate the states and store in the list states[] and also the seperated capitals must be stored in capitals[]'''

states_capitals= [string for string in input().split(' ')]
print(states_capitals)

# Initialize empty lists for states and capitals
states = []
capitals = []

# Split each entry into state and capital
for entry in states_capitals:
    state, capital = entry.split('-')
    states.append(state)
    capitals.append(capital)

# Print the results
print("States:", states)     
print("Capitals:", capitals) 