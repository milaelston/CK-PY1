money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def life_calculator(capital, slry, spnd, incrs):
    month = 0
    while capital > spnd:
        capital += slry - spnd
        spnd *= 1 + incrs
        month += 1
    return month


month = life_calculator(money_capital, salary, spend, increase)

print(month)
