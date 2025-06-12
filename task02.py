'''
Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.
'''
import heapq

def merge_k_lists(lists):
  heap = []
  for i in range(len(lists)):
    if lists[i]:
      for li in range(len(lists[i])):
        heapq.heappush(heap, lists[i][li])

  sorted_list=[]
  while heap:
    sorted_list.append(heapq.heappop(heap))

  return sorted_list
    

if __name__ == "__main__":
  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
  merged_list = merge_k_lists(lists)
  print("Відсортований список:", merged_list)