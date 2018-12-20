# 输出99乘法表

# 使用for循环
for i in range(1,10) :
	for j in range(1,i+1) :
		print (f'{j}*{i}={i*j:<5}',end=' ')
	print ('')
print ('='*90)

for i in range(9,0,-1) :
	for j in range(1,i+1) :
		print (f'{j}*{i}={i*j:<5}',end=' ')
	print ('')
print ('='*90)

for i in range(1,10) :
	for j in range(9,0,-1) :
		if i < j :
			print('         ',end=' ')
		else :
		    print(f'{j}*{i}={i*j:<5}',end=' ')
	print('')
print('='*90)

for i in range(9,0,-1) :
	for j in range(9,0,-1) :
		if j > i  :
			print('         ',end=' ')
		else :
			print(f'{j}*{i}={i*j:<5}',end=' ')
	print('')

print('='*90)

# 使用while循环

i=1
while(i<10) :
	j = 1
	while(j<=i) :
		print (f'{j}*{i}={i*j:<5}',end=' ')
		j+=1
	print('')
	i+=1
print('='*90)

i=9
while(i>0) :
	j = 1
	while(j<=i) :
		print (f'{j}*{i}={i*j:<5}',end=' ')
		j+=1
	print('')
	i-=1
print('='*90)

i=1
while(i<10):
	j=9
	while(j>0) :
		if j>i :
			print('         ',end=' ')
			j-=1
		else :
			print (f'{j}*{i}={i*j:<5}',end=' ')
			j-=1
	print('')
	i+=1
print('='*90)

i=9
while(i>0):
	j=9
	while(j>0):
		if j>i :
			print('         ',end=' ')
			j-=1
		else :
			print (f'{j}*{i}={i*j:<5}',end=' ')
			j-=1
	print('')
	i-=1

print('='*90)