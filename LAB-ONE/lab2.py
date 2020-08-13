# part 1 is 9 tiles wide and 7 tiles long
# part2 is 5 tiles wides by 7 tiles long
# tiles come in package of 6

W1 = 9
L1 = 7
W2 = 5
L2 = 7
part_1 = (W1 * L1)

part_2 = (W2 * L2)

parts_total = (part_1 + part_2)

#amounts to a total of 98 tiles needed

print (parts_total)

#17 packages containing 6 tiles

packages = 17
tile_cont = 6
tiles_total = (packages * tile_cont)

tiles_left = (tiles_total - parts_total)

#4 tiles will be left

print (tiles_left)
