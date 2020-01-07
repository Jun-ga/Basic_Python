def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = meal_cost * (tip_percent / 100)
    tax_cost = meal_cost * (tax_percent / 100)

    sum_cost = meal_cost + tip_cost + tax_cost
    result = round (sum_cost,0)

    print(int(result))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
