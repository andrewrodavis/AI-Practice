input = """O1P1P1Q1Q1B1
O1....C1..B1
..X0X0C1....
......D1....
......D1....
............
"""
cols = int(input.find("\n") / 2)
rows = int(len(input) / (cols*2+1))
exit_row = 2
print("Rush Hour Dimensions: %d x %d" % (rows, cols))


def getIndex(row, col):
	return row * (cols*2+1) + col*2


def getRowCol(index):
	return int(index / (cols*2+1)), index % (cols*2+1)


def getCarInformation(c):
	first_location = input.find(c)
	second_location = input.rfind(c)
	if second_location == first_location+2:
		return "(horizontal %s) (front %s %d)" % (c, c, second_location)
	else:
		return "(vertical %s) (front %s %d)" % (c, c, first_location)


cars = ["O1", "P1", "Q1", "B1", "C1", "X0", "D1"]
car_information = [getCarInformation(c) for c in cars]
print("Car Information: %s" % car_information)

for car in cars:
	print("(%s OBJECT)" % car)

for row in range(0, rows):
	for col in range(0, cols):
		print("(%d OBJECT)" % getIndex(row, col))

print("(preconds")
for row in range(0, rows):
	for col in range(0, cols):
		if col > 0:
			print("\t(right-of %d %d) " % (getIndex(row, col-1), getIndex(row, col)))
		if row > 0:
			print("\t(above %d %d) " % (getIndex(row, col), getIndex(row-1, col)))
		if input[getIndex(row, col)] == '.':
			print("\t(clear %d)" % getIndex(row, col))
for info in car_information:
	print("\t%s" % info)
print(")")

print("(effects")
print("\t(front X0 %d)" % getIndex(exit_row, cols-1))
print(")")