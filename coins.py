import timeit

def makeChange(change, change_list, coin_list=[]):
	change_list = sorted(change_list, reverse=True)
	if change == 0 or len(change_list) == 0:
		return coin_list
	coin_count = change // change_list[0]
	change = change - (coin_count*change_list[0])
	coin_list.append(coin_count)
	return makeChange(change, change_list[1:], coin_list)

def getOptimalChange(amount, change_list):
	losses = {}
	while change_list:
		coin_list = []
		change_list = sorted(change_list, reverse=True)
		coin_list = makeChange(amount, change_list, coin_list)
		losses[sum(coin_list)] = list(zip(coin_list, change_list))
		change_list.pop(0)
	return min(losses.keys()), losses[min(losses.keys())]


def main():
	amount = 54639
	change_list = sorted([1, 5, 10, 25, 100, 200, 500, 1000, 2000, 5000, 10000])
	change_name = ["cent", "nickel", "dime", "quarter", "one", "two", "five", "ten", "twenty", "fifty", "hundred"]
	currency_title = {change_list[i]:change_name[i] for i in range(len(change_list))}
	currency_count, currency_list = getOptimalChange(amount, change_list)
	change_str = ''
	total_items = 0
	for item in currency_list:
		total_items += item[0]
		if item[0] == 1:
			change_str += ", %d (%s)" % (item[0], currency_title[item[1]])
		elif item[0] > 1:
			change_str += ", %d (%ss)" % (item[0], currency_title[item[1]])
			change_str = change_str.replace('tys', 'ties')
		else:
			continue
	dollars = amount // 100
	cents = amount % 100
	print("\nInput Amount: $%d.%d"%(dollars, cents))
	change_str = change_str[2:]
	change_str = change_str.lstrip()
	print("\nChange: %d pieces\n"%total_items)
	print(change_str.lstrip())

print("\nexecution time:", timeit.timeit(main, number=1))
