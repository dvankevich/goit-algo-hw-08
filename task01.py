'''
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
'''

import heapq

cables = [4, 10, 3, 5, 1]
heapq.heapify(cables)
cost = 0
print("cables: ",cables,"cost: ", cost)

while len(cables) > 1:
  cable01 = heapq.heappop(cables)
  cable02 = heapq.heappop(cables)
  print("cables after pop two cable", cables)
  cable0102 = cable01 + cable02
  cost += cable0102
  heapq.heappush(cables,cable0102)
  print("cables: ",cables,"cost: ", cost)


