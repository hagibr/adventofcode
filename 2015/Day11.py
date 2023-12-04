input = "cqjxjnds"

# Calculate the next password
def next_pass(curr_pass):
  next = curr_pass[:]
  # From rightmost character to leftmost character
  for d in range(len(next)-1,-1,-1):
    # Incrementing this digit
    if next[d] != 'z':
      next[d] = chr(ord(next[d])+1)
      return next
    else:
      next[d] = 'a'
  return next

# Check the validity of a passowrd
def valid(password):
  # i, o, l are prohibited
  for c in password:
    if c in "iol":
      return False
  # Must have 3 sequentially crescent digits
  for i in range(6):
    if ord(password[i]) == (ord(password[i+1])-1) and ord(password[i+1]) == (ord(password[i+2])-1):
      # Must have 2 non-overlapping pairs of letters
      for i in range(4):
        if( password[i] == password[i+1] ):
          for j in range(i+2,7):
            if( password[j] == password[j+1]):
              return True
  return False

# Calculating the next valid password
new_pass = next_pass(list(input))
while( not valid(new_pass) ):
  new_pass = next_pass(new_pass)

print(f"Part One: {''.join(new_pass)}")

# Again, calculating the next valid password
new_pass = next_pass(new_pass)
while( not valid(new_pass) ):
  new_pass = next_pass(new_pass)

print(f"Part Two: {''.join(new_pass)}")