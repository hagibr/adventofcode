input = '''Alice would gain 2 happiness units by sitting next to Bob.
Alice would gain 26 happiness units by sitting next to Carol.
Alice would lose 82 happiness units by sitting next to David.
Alice would lose 75 happiness units by sitting next to Eric.
Alice would gain 42 happiness units by sitting next to Frank.
Alice would gain 38 happiness units by sitting next to George.
Alice would gain 39 happiness units by sitting next to Mallory.
Bob would gain 40 happiness units by sitting next to Alice.
Bob would lose 61 happiness units by sitting next to Carol.
Bob would lose 15 happiness units by sitting next to David.
Bob would gain 63 happiness units by sitting next to Eric.
Bob would gain 41 happiness units by sitting next to Frank.
Bob would gain 30 happiness units by sitting next to George.
Bob would gain 87 happiness units by sitting next to Mallory.
Carol would lose 35 happiness units by sitting next to Alice.
Carol would lose 99 happiness units by sitting next to Bob.
Carol would lose 51 happiness units by sitting next to David.
Carol would gain 95 happiness units by sitting next to Eric.
Carol would gain 90 happiness units by sitting next to Frank.
Carol would lose 16 happiness units by sitting next to George.
Carol would gain 94 happiness units by sitting next to Mallory.
David would gain 36 happiness units by sitting next to Alice.
David would lose 18 happiness units by sitting next to Bob.
David would lose 65 happiness units by sitting next to Carol.
David would lose 18 happiness units by sitting next to Eric.
David would lose 22 happiness units by sitting next to Frank.
David would gain 2 happiness units by sitting next to George.
David would gain 42 happiness units by sitting next to Mallory.
Eric would lose 65 happiness units by sitting next to Alice.
Eric would gain 24 happiness units by sitting next to Bob.
Eric would gain 100 happiness units by sitting next to Carol.
Eric would gain 51 happiness units by sitting next to David.
Eric would gain 21 happiness units by sitting next to Frank.
Eric would gain 55 happiness units by sitting next to George.
Eric would lose 44 happiness units by sitting next to Mallory.
Frank would lose 48 happiness units by sitting next to Alice.
Frank would gain 91 happiness units by sitting next to Bob.
Frank would gain 8 happiness units by sitting next to Carol.
Frank would lose 66 happiness units by sitting next to David.
Frank would gain 97 happiness units by sitting next to Eric.
Frank would lose 9 happiness units by sitting next to George.
Frank would lose 92 happiness units by sitting next to Mallory.
George would lose 44 happiness units by sitting next to Alice.
George would lose 25 happiness units by sitting next to Bob.
George would gain 17 happiness units by sitting next to Carol.
George would gain 92 happiness units by sitting next to David.
George would lose 92 happiness units by sitting next to Eric.
George would gain 18 happiness units by sitting next to Frank.
George would gain 97 happiness units by sitting next to Mallory.
Mallory would gain 92 happiness units by sitting next to Alice.
Mallory would lose 96 happiness units by sitting next to Bob.
Mallory would lose 51 happiness units by sitting next to Carol.
Mallory would lose 81 happiness units by sitting next to David.
Mallory would gain 31 happiness units by sitting next to Eric.
Mallory would lose 73 happiness units by sitting next to Frank.
Mallory would lose 89 happiness units by sitting next to George.
'''

happiness_map = {}
guest_list = []
for entry in input.splitlines():
  # Clearing and tokenizing the entry
  entry = entry.replace(" would", "").replace(" happiness units by sitting next to", "").replace(".", "").split()
  # Populating the happiness map
  if entry[1] == 'gain':
    happiness_map[(entry[0], entry[3])] = int(entry[2])
  elif entry[1] == 'lose':
    happiness_map[(entry[0], entry[3])] = -int(entry[2])
  # Populating the guest list
  if entry[0] not in guest_list:
    guest_list.append(entry[0])
  if entry[3] not in guest_list:
    guest_list.append(entry[3])
    
# print(happiness_map)
# print(guest_list)

# Trying every permutation (8! = 40320)
max_happiness = 0
for a in guest_list:
  r_a = guest_list[:]
  r_a.remove(a)
  for b in r_a:
    r_b = r_a[:]
    r_b.remove(b)
    for c in r_b:
      r_c = r_b[:]
      r_c.remove(c)
      for d in r_c:
        r_d = r_c[:]
        r_d.remove(d)
        for e in r_d:
          r_e = r_d[:]
          r_e.remove(e)
          for f in r_e:
            r_f = r_e[:]
            r_f.remove(f)
            for g in r_f:
              r_g = r_f[:]
              r_g.remove(g)
              h = r_g[0]
              happiness = happiness_map[(a,b)] + happiness_map[(b,a)]
              happiness += happiness_map[(b,c)] + happiness_map[(c,b)]
              happiness += happiness_map[(c,d)] + happiness_map[(d,c)]
              happiness += happiness_map[(d,e)] + happiness_map[(e,d)]
              happiness += happiness_map[(e,f)] + happiness_map[(f,e)]
              happiness += happiness_map[(f,g)] + happiness_map[(g,f)]
              happiness += happiness_map[(g,h)] + happiness_map[(h,g)]
              happiness += happiness_map[(h,a)] + happiness_map[(a,h)]
              if( happiness > max_happiness ):
                max_happiness = happiness 
              
print(f"Part One: {max_happiness}")

# Now we add ourselves to the list
for guest in guest_list:
  happiness_map[("me", guest)] = 0
  happiness_map[(guest, "me")] = 0
guest_list.append("me")
  
# Trying every permutation (9! = 362880)
max_happiness = 0
for a in guest_list:
  r_a = guest_list[:]
  r_a.remove(a)
  for b in r_a:
    r_b = r_a[:]
    r_b.remove(b)
    for c in r_b:
      r_c = r_b[:]
      r_c.remove(c)
      for d in r_c:
        r_d = r_c[:]
        r_d.remove(d)
        for e in r_d:
          r_e = r_d[:]
          r_e.remove(e)
          for f in r_e:
            r_f = r_e[:]
            r_f.remove(f)
            for g in r_f:
              r_g = r_f[:]
              r_g.remove(g)
              for h in r_g:
                r_h = r_g[:]
                r_h.remove(h)
                i = r_h[0]
                happiness = happiness_map[(a,b)] + happiness_map[(b,a)]
                happiness += happiness_map[(b,c)] + happiness_map[(c,b)]
                happiness += happiness_map[(c,d)] + happiness_map[(d,c)]
                happiness += happiness_map[(d,e)] + happiness_map[(e,d)]
                happiness += happiness_map[(e,f)] + happiness_map[(f,e)]
                happiness += happiness_map[(f,g)] + happiness_map[(g,f)]
                happiness += happiness_map[(g,h)] + happiness_map[(h,g)]
                happiness += happiness_map[(h,i)] + happiness_map[(i,h)]
                happiness += happiness_map[(i,a)] + happiness_map[(a,i)]
                
                if( happiness > max_happiness ):
                  max_happiness = happiness 

print(f"Part Two: {max_happiness}")
