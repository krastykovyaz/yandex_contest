#Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из файла и выводить ответ в файл
fname = input()
fh = open(fname)
count = 0
s_num = 0
line = fh.read()
nums = line.split()
f = open("output.txt", "w")
f.write(str(int(nums[0]) + int(nums[1])))
fh.close()
f.close()