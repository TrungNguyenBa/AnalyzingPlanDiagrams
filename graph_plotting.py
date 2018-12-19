import subprocess
import sys
import argparse
#import patch
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import json
import numpy as np

Z = np.zeros((101,101))

PIPE=subprocess.PIPE

class parameter:
	def __init__(self,q,s,l):
		self.q = int(q)
		self.s = int(s)
		self.l = int(l)
		self.cost = 0

	def print(self):
		return "(Q{},S-{},L-{})".format(self.q,self.s,self.l)

	def equal(self,p):
		if self.s == p.s and self.q == p.q and self.l == p.l:
			return True
		return False

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
		with open("{}/results.out".format(args.plan_output_dir)) as f:
			lines = f.read().split("\n")
			for l in lines:
				l = l[:-1]
				ps = l.split(";")
				r = []
				for p in ps:
					chunk = p.split(",")
					#print(chunk[0])
					q = chunk[0][2:].strip()
					s = chunk[1][2:].strip()
					l = chunk[2][2:-1].strip()
					
					#print(q,s,l)
					r.append(parameter(q,s,l))
				print(len(r))
				records.append(r)
				#print(records)
			print("Current number of plan is {}".format(len(records)))
	except:
		print("No saved file yet")


def load_cost():
	maxcost = -1	
	for r in records:
		for p in r:
			f = open("{}/query{}s{}_l{}.json".format(args.cost_output_dir,p.q,p.s,p.l))
			json_data = f.read().	split()[3:-2]
			json_data = ''.join(json_data)
			json_data = json_data.replace('+','')
			data = json.loads(json_data)
			p.cost = data[0]["Plan"]["TotalCost"]
			maxcost = max(maxcost,p.cost)
			f.close()
	for r in records:
		for p in r:
			p.cost = round(p.cost/maxcost,1)


records = []

parser = argparse.ArgumentParser()
parser.add_argument('list_of_query_output', help='list of all query output file to compare')
parser.add_argument('--plan-output-dir', required=True)
parser.add_argument('--cost-output-dir',required = True)
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

#print(records)
plan_diagram = np.zeros((101,101))

cost_diagram = []

def creating_plan_diagram():
	i = 0
	for r in records:
		for p in r :
			plan_diagram[p.s,p.l] = i
		i+=1
	plt.pcolor(plan_diagram)
	plt.colorbar()
	plt.show()

def creating_cost_diagram():
	for r in records:
		for p in r :
			cost_diagram.append((p.s,p.l,p.cost))
	fig = plt.figure()
	X,Y,Z = zip(*cost_diagram)
	print(len(X),len(Y),len(Z))
	ax = fig.gca(projection='3d')
	X = np.reshape(X, (101,101))
	Y = np.reshape(Y, (101,101))
	Z = np.reshape(Z, (101,101))
	surf = ax.plot_surface(X,Y,Z)	
	plt.show()

load_cost()
creating_cost_diagram()
creating_plan_diagram()

