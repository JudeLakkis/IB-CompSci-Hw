from random import randint
wheel = [str(i) for i in range(37)]
wheel.append('00')

odd = wheel[1:36:2]
even = wheel[2:36:2]
money = 1000
bets = bets = (odd, even)


for i in range(10):
    betted = round(money / 5, 2)
    land = wheel[randint(0, 37)]
    bet = bets[randint(0, len(bets) - 1)]
    if land in bet:
        money = round(money + 2 * betted, 2)
    else:
        money = round(money - betted, 2)
    print(land, betted, money)
