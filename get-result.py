path = "test3"

f1 = file("test.3.desc", "r")
f2 = file("result100/"+path, "r")

count = [0 for i in range(127)]
time = [0.0 for i in range(127)]
	
template = f1.readline()
timelong = f2.readline()

while template:
	id = (int(template)-1)/100+1
	time[id]=(time[id]*count[id]+float(timelong))/(count[id]+1)
	count[id]+=1
	template = f1.readline()
	timelong = f2.readline()
	
f1.close()
f2.close()

f3 = file("result100/result3",'w')

for i in range(0,127):
	f3.write(str(time[i]))
	f3.write('\t')
	f3.write(str(count[i]))
	f3.write('\n')
f3.close()
