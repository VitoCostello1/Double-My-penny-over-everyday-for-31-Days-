penny = 0.01
total = 0
for i in range(31):
	total += penny
	penny *= 2
print("dollars {:.2f}".format(total))