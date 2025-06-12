'''
Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.
'''
import heapq

def merge_k_lists(lists):
  #print(lists)
  merged_list = []
  for i in range(len(lists)):
    if lists[i]:
      #print(lists[i])
      # while lists[i]:
      #   merged_list.append(lists[i].pop(0))
      #print("merged_list",merged_list)
      for li in range(len(lists[i])):
        merged_list.append(lists[i][li])

  heapq.heapify(merged_list)
  #print("merged_list",merged_list)
  sorted_list=[]
  while merged_list:
    sorted_list.append(heapq.heappop(merged_list))

  return sorted_list
    

if __name__ == "__main__":
  lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
  merged_list = merge_k_lists(lists)
  print("Відсортований список:", merged_list)