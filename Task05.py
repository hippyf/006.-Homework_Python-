def same_by (characteristic, object):
	result = True
	characteristicList = [characteristic(x) for x in object]
	for i in range(len(characteristicList) - 1):
		if characteristicList[i] != characteristicList[i + 1]:
			result = False
	return result
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')