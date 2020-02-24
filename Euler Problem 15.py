##Starting in the top left corner of a 2×2 grid,
##and only being able to move to the right and down,
##there are exactly 6 routes to the bottom right corner.
##
##How many such routes are there through a 20×20 grid?

paths = [1]*21 + [0]*420
for path in range(21, 441):
    if path % 21 != 0:
        paths[path] += paths[path-1]
        paths[path] += paths[path-21]
    else:
        paths[path] += paths[path-21]
print(paths[-1])
