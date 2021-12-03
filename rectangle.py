# E. Задача 5.
#
# Ограничение времени	3 секунды
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Дано N отрезков (3 <= N <= 100 000). Необходимо выбрать среди них такие (от 3 до N), чтобы сумма их длин получилась максимальной, но при этом из трех любых среди них можно было составить треугольник. В ответе выведите получившуюся сумму длин выбранных отрезков или 0, если таковых не существует.
# Пример входного файла input.txt
# 3 2 5 4 1
# Пример выходного файла output.txt
# 12
# nums = sorted(input().split(' '))

nums = sorted([3, 2, 5, 4, 1])


max_sum = 0

uniq = set()

for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if i == j or i == k or j == k:
                continue
            print(i, j, k)
            n_i = nums[i]
            n_j = nums[j]
            n_k = nums[k]
            if n_i < n_j + n_k and \
                n_j < n_k + n_i and \
                n_k < n_j + n_i:
                uniq.add(tuple(sorted([n_i, n_j, n_k])))
                abc = tuple(sorted([n_i, n_j, n_k]))
list(uniq)
print(uniq)