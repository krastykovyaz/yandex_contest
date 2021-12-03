with open('input.txt') as txtf:
	data = txtf.readlines()
a, b = data[0].split('+')
answer = int(a) + int(b)
with open('output.txt', 'a') as txtf:
	txtf.write(str(answer))