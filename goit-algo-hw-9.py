import time

# Жадібний алгоритм
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    coins.sort(reverse=True)
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count
    return result

# Динамічне програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    if min_coins[amount] == float('inf'):
        return None 

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Вимірювання часу
def measure_performance(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Сума: {amount}")
    print("Жадібний алгоритм:")
    print(f"  Час виконання: {greedy_time:.6f} секунд")
    print(f"  Результат: {greedy_result}")
    print("Алгоритм динамічного програмування:")
    print(f"  Час виконання: {dp_time:.6f} секунд")
    print(f"  Результат: {dp_result}")

if __name__ == "__main__":
    # Вимірювання продуктивності для різних сум
    for amount in [113, 1233, 5485, 10200, 20789, 55555, 17856]:
        measure_performance(amount)

