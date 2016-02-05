import requests
import time

headers = {"Content-type": "application/sparql",
            "Accept": "text/plain"}
path = "stress-workloads/watdiv-stress-100/test.1.sparql"
sqlfile = open(path, 'r')
result = open("result-100M/test1", "w")
print "start now..."
line = sqlfile.readline()
while line:
	index = line.find('WHERE')
	output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
	start = time.time()
	r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60000)
	#print r.text
	end = time.time()
	result.write(str(end - start))
	result.write('\n')
	#print("%.03f" %(end-start))
	line = sqlfile.readline()
print "end successfully."
sqlfile.close()
result.close()
