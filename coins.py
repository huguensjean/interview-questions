import timeit

def makeChange(change, change_list, coin_list=None):
    if coin_list is None:
        coin_list = []
    if change == 0 or not change_list:
        return coin_list
    largest_coin = change_list[0]
    coin_count = change // largest_coin
    change = change - (coin_count * largest_coin)
    coin_list.append(coin_count)
    return makeChange(change, change_list[1:], coin_list)

def getOptimalChange(amount, change_list):
    # We'll try subsets of the coin list by removing one coin each iteration
    # and track the minimal total coin count.
    losses = {}
    temp_list = change_list[:]  # Work on a copy, to not modify original
    while temp_list:
        # Sort descending to ensure makeChange uses largest coin first
        current_list = sorted(temp_list, reverse=True)
        coin_list = makeChange(amount, current_list)
        losses[sum(coin_list)] = list(zip(coin_list, current_list))
        temp_list.pop(0)  # Remove one coin (smallest) for next iteration
    min_coins = min(losses.keys())
    return min_coins, losses[min_coins]

def main():
    amount = 54639
    # Sort coins ascending once here
    change_list = [1, 5, 10, 25, 100, 200, 500, 1000, 2000, 5000, 10000]
    change_list.sort()

    change_name = ["cent", "nickel", "dime", "quarter", "one", "two", "five", 
                   "ten", "twenty", "fifty", "hundred"]
    currency_title = {change_list[i]: change_name[i] for i in range(len(change_list))}

    currency_count, currency_list = getOptimalChange(amount, change_list)

    # Build the output string
    change_str = ''
    total_items = 0
    for count, coin_val in currency_list:
        if count > 0:
            total_items += count
            coin_name = currency_title[coin_val]
            if count == 1:
                change_str += f", {count} ({coin_name})"
            else:
                # Handle pluralization simply by adding 's' except special case for 'twenty'
                if coin_name.endswith('y'):
                    # Replace 'y' with 'ies' (e.g., "twenty" -> "twenties")
                    coin_name = coin_name[:-1] + "ies"
                else:
                    coin_name += "s"
                change_str += f", {count} ({coin_name})"

    dollars = amount // 100
    cents = amount % 100
    print(f"\nInput Amount: ${dollars}.{cents:02d}")
    change_str = change_str[2:].strip()
    print(f"\nChange: {total_items} pieces\n")
    print(change_str)

print("\nExecution time:", timeit.timeit(main, number=1))
