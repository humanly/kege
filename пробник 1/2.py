print("y w z x f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x and not(y)) or (x == z) or w
                if f == 0:
                    print(y, w, z, x, f)