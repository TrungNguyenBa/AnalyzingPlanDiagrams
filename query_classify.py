import subprocess
import sys
import argparse
#import patch
import os
PIPE=subprocess.PIPE

class parameter:
	def __init__(self,q,s,l):
		self.q = q
		self.s = s
		self.l = l

	def print(self):
		return "(Q{},S-{},L-{})".format(self.q,self.s,self.l)

def get_parameter(i):
	i = i.replace(".json","")
	temp = i.split("_l")
	l = temp[1].strip()
	temp = temp[0].split("s")
	s = temp[1].strip()
	temp = temp[0].split("query")
	q = temp[1].strip()
	return parameter(q,s,l)


def load_file():
	try :
		with open("{}/results.out".format(args.output_dir)) as f:
			for l in f:
				l = l[:-1]
				ps = l.split(";")
				r = []
				for p in ps:
					chunk = p.split(",")
					#print(chunk)
					q = chunk[0][1].strip()
					s = chunk[1][1].strip()
					l = chunk[2][1].strip()
					#print(q,s,l)
					r.append(parameter(q,s,l))
				records.append(r)
	except:
		print("No saved file yet")


def save_to_file():
	with open("{}/results.out".format(args.output_dir),"w+") as f:
		for r in records:
			l = ""
			for p in r:
				l+= p.print() + ";"
			f.write(l)

def check_equal_to_plan(p1,p2):
	file1name = "query{}s{}_l{}.json".format(p1.q,p1.s,p1.l)
	file2name = "query{}s{}_l{}.json".format(p2.q,p2.s,p2.l)
	#print("checking {} and {}".format(file1name,file2name))
	r = subprocess.run("diff {}/{} {}/{}".format(args.input_dir,file1name,args.input_dir,file2name),shell=True,stdout=PIPE,stderr=PIPE)
	if (r.stderr.decode() != ""):
		print(r.stderr.decode())
		raise Exception("diff command error")
	elif (r.stdout.decode() != ""):
		#print(r.stdout.decode())
		return False
	else:
		return True

records = []

parser = argparse.ArgumentParser()
parser.add_argument('list_of_query_output', help='list of all query output file to compare')
parser.add_argument('--input-dir',required = True)
parser.add_argument('--output-dir', required=True)
parser.add_argument('--start-from', default="0")

args = parser.parse_args()
print(args)

with open(args.list_of_query_output) as f:
	versions = f.readlines()

start = 0
if (args.start_from != '0'):
  start = int(args.start_from) -1
  versions=versions[start:]

load_file()

for i in versions:
	p = get_parameter(i)
	if records == []:
		records.append([p])
	else:
		newPlan = True
		for r in records:
			if check_equal_to_plan(r[0],p):
				r.append(p)
				newPlan = False
				break
		if (newPlan):
			records.append([p])
print("Numes of plans: {}".format(len(records)))
save_to_file()