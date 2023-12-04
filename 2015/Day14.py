input = '''Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds.
'''

# Parsing the reindeer specs
reindeer_list = []
for entry in input.splitlines():
  entry = entry.replace(" can fly", "").replace(" km/s for", "").replace(" seconds, but then must rest for", "").replace(" seconds.", "").split()
  reindeer_list.append([entry[0], int(entry[1]), int(entry[2]), int(entry[3])])

# In case something change in the second part...
total_time = 2503

# Using a smart shortcut for the total distance calculation
max_distance = 0
for reindeer in reindeer_list:
  name, speed, time_running, time_resting = reindeer
  integer_steps = total_time // (time_running+time_resting)
  time_last_step = total_time % (time_running+time_resting)
  distance = speed * (integer_steps * time_running + min(time_running, time_last_step))
  # print(f"{name}: {distance}")
  max_distance = max(distance, max_distance)

print(f"Part One: {max_distance}")
    
# OK, Santa changed the score system and we can't use the smart calculation above, we have to analyze second-by-second this time

# Creating and populating these auxiliary variables
points = []
position = []
running = []
run_remaining = []
rest_remaining = []

for r in reindeer_list:
  points.append(0)            # Every reindeer starts with 0 points
  position.append(0)          # .. and at the starting position
  running.append(True)        # .. and running
  run_remaining.append(r[2])  # .. with all the remaing time
  rest_remaining.append(0)    # .. no resting

# Now we analyze every second of the race
for i in range(total_time):
  for i, r in enumerate(reindeer_list):
    # If the reindeer is running, update the position
    if( running[i] ):
      position[i] += r[1]
      # If it has reached the limit
      run_remaining[i] -= 1
      if( run_remaining[i] == 0 ):
        # Start resting
        running[i] = False
        rest_remaining[i] = r[3]
    # If it is resting, just wait for the resting time to complete
    else:
      rest_remaining[i] -= 1
      if( rest_remaining[i] == 0 ):
        running[i] = True
        run_remaining[i] = r[2]
  # Now we evaluate all the positions and give 1 point for everyone at the leading position
  max_position = max(position)
  for i, r in enumerate(reindeer_list):
    if( position[i] == max_position ):
      points[i] += 1
  
print(f"Part Two: {max(points)}")