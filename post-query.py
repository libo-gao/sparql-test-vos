import requests
import time

headers = {"Content-type": "application/sparql",
            "Accept": "text/plain"}
path = "test.3.sparql"
sqlfile = open(path, 'r')
result = open("result100/test3", "w")
line = sqlfile.readline()
while line:
	index = line.find('WHERE')
	output_line = line[:index] + 'FROM <http://watdiv.10m> ' + line[index:]
	start = time.clock()
	r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60000)
	end = time.clock()
	result.write(str(end - start))
	result.write('\n')
	#print("%.03f" %(end-start))
	line = sqlfile.readline()
	
sqlfile.close()
result.close()
