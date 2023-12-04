input = "1113122113"

# This is the recursive function that interpret a given string and return the look-and-say of the string
def lookandsay(number):
  ret = ""
  current = None
  cur_count = 0
  for c in number:
    if( c != current ):
      if( current is not None ):
        ret += str(cur_count) + current
      current = c
      cur_count = 1
    else:
      cur_count += 1
  ret += str(cur_count) + current
  return ret

result = input

# Calling 40 times for the first part
for i in range(40):
  result = lookandsay(result)
print(f'Part One: {len(result)}')

# Calling 10 more times for the second part
for i in range(10):
  result = lookandsay(result)
print(f'Part Two: {len(result)}')
