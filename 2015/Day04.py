# I won't implement md5 algorithm
import hashlib

secret_key = "yzbqklnj"

number = 0

# Part One
while True:
  # Appending next number to secret key
  number += 1
  secret_number = secret_key + str(number)
  # Calculating the md5 checksum
  hash = hashlib.md5(bytes(secret_number, 'utf-8')).hexdigest()
  # Comparing the first 5 hex digits to 00000
  if( hash[0:5] == '00000' ):
    print(f"Part One: {number}")
    break

# Part Two - we don't need to reset the current number
while True:
  number += 1
  secret_number = secret_key + str(number)
  hash = hashlib.md5(bytes(secret_number, 'utf-8')).hexdigest()
  # The only difference is that we compare the first 6 hex digits
  if( hash[0:6] == '000000' ):
    print(f"Part Two: {number}")
    break