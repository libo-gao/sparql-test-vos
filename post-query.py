import requests
import time

headers = {"Content-type": "application/sparql",
            "Accept": "text/plain"}
path = "stress-workloads/watdiv-stress-1000/warmup.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/warm", "w")
print "warmup start now..."
line = sqlfile.readline()
while line:
	index = line.find('WHERE')
	output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
	start = time.time()
	r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
	#print r.text
	end = time.time()
	result.write(str(end - start))
	result.write('\n')
	#print("%.03f" %(end-start))
	line = sqlfile.readline()
print "warmup end successfully."
sqlfile.close()
result.close()

path = "stress-workloads/watdiv-stress-1000/test.1.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/test1", "w")
print "test start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "test end successfully."
sqlfile.close()
result.close()


path = "stress-workloads/watdiv-stress-1000/warmup.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/warm", "w")
print "warmup start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "warmup end successfully."
sqlfile.close()
result.close()

path = "stress-workloads/watdiv-stress-1000/test.2.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/test2", "w")
print "test start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "test end successfully."
sqlfile.close()
result.close()



path = "stress-workloads/watdiv-stress-1000/warmup.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/warm", "w")
print "warmup start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "warmup end successfully."
sqlfile.close()
result.close()

path = "stress-workloads/watdiv-stress-1000/test.3.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/test3", "w")
print "test start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "test end successfully."
sqlfile.close()
result.close()


path = "stress-workloads/watdiv-stress-1000/warmup.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/warm", "w")
print "warmup start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "warmup end successfully."
sqlfile.close()
result.close()

path = "stress-workloads/watdiv-stress-1000/test.4.sparql"
sqlfile = open(path, 'r')
result = open("result-1000M/test4", "w")
print "test start now..."
line = sqlfile.readline()
while line:
        index = line.find('WHERE')
        output_line = line[:index] + 'FROM <http://watdiv.10M> ' + line[index:]
        start = time.time()
        r = requests.post("http://localhost:8890/sparql", data = {"query":output_line}, timeout = 60)
        #print r.text
        end = time.time()
        result.write(str(end - start))
        result.write('\n')
        #print("%.03f" %(end-start))
        line = sqlfile.readline()
print "test end successfully."
sqlfile.close()
result.close()

