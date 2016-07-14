bottles = 99

for i in range(99, 0 ,-1):
    if bottles > 2:
        print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer.")
        print("Take one down and pass it around,", (bottles - 1), "bottles of beer on the wall.\n")
        bottles = bottles - 1
    elif bottles == 2:
        print(bottles, "bottles of beer on the wall,", bottles, "bottles of beer.")
        print("Take one down and pass it around,", (bottles - 1), "bottle of beer on the wall.\n")
        bottles = bottles - 1
    else:
        print(bottles, "bottle of beer on the wall,", bottles, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")