input = '''Tristram to AlphaCentauri = 34
Tristram to Snowdin = 100
Tristram to Tambi = 63
Tristram to Faerun = 108
Tristram to Norrath = 111
Tristram to Straylight = 89
Tristram to Arbre = 132
AlphaCentauri to Snowdin = 4
AlphaCentauri to Tambi = 79
AlphaCentauri to Faerun = 44
AlphaCentauri to Norrath = 147
AlphaCentauri to Straylight = 133
AlphaCentauri to Arbre = 74
Snowdin to Tambi = 105
Snowdin to Faerun = 95
Snowdin to Norrath = 48
Snowdin to Straylight = 88
Snowdin to Arbre = 7
Tambi to Faerun = 68
Tambi to Norrath = 134
Tambi to Straylight = 107
Tambi to Arbre = 40
Faerun to Norrath = 11
Faerun to Straylight = 66
Faerun to Arbre = 144
Norrath to Straylight = 115
Norrath to Arbre = 135
Straylight to Arbre = 127
'''

cities_list = ["Tristram", "AlphaCentauri", "Snowdin", "Tambi", "Faerun", "Norrath", "Straylight", "Arbre"]

dist_map = {}

for entry in input.splitlines():
  cityA, cityB, dist = entry.replace(" to", "").replace(" =", "").split()
  dist_map[(cityA,cityB)] = int(dist)
  dist_map[(cityB,cityA)] = int(dist)
  
shortest = 200*7 # There is no distance between cities longer than 200
longest = 0
# We are going to try ALL the routes (8! = 40320 possibilities)
for a in cities_list:
  r_a = cities_list[:]
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
              # Calculating the route. It's so simpler this way.
              route = dist_map[(a,b)] + dist_map[(b,c)] + dist_map[(c,d)] + dist_map[(d,e)] + dist_map[(e,f)] + dist_map[(f,g)] + dist_map[(g,h)]
              # Comparing this route with the shortest and the longest until now
              if( route < shortest ):
                shortest = route
                print(f"{a} {b} {c} {d} {e} {f} {g} {h}: {route} (shorter)")
              if( route > longest ):
                longest = route
                print(f"{a} {b} {c} {d} {e} {f} {g} {h}: {route} (longer)")
                

print(f"Part One: {shortest}")

print(f"Part Two: {longest}")