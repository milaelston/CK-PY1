salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def life_calc(slry, spnd, mnths, incrs):
    needmoney = 0
    for i in range(mnths):
        needmoney -= slry - spnd
        spnd *= 1 + incrs
    return needmoney


need_money = life_calc(salary, spend, months, increase)

print(round(need_money))
