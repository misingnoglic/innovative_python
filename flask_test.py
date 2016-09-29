from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)
import json

def collatz(n):
	total = []
	already_seen = set()
	while n!=1 and n not in already_seen:
		print n
		total.append(n)
		already_seen.add(n)
		if n%2==0: n = n/2
		else: n = (n*3)+11
	total.append(n)
	return total

def color(num):
	if num%2==0: return "#E74C3C"
	else: return "#F1C40F"

@app.route("/<num>")
def display(num):
	sequence = collatz(int(num))
	
	
	#id_dict.reverse()
	edge_dict = []
	for i in range(len(sequence)-1):
		edge_dict.append({'from':sequence[i], 'to':sequence[i+1], 'color':{'inherit':'both'}})
	#edge_dict.reverse()
	if sequence[-1] in sequence[:-1]: sequence.pop()
	id_dict = [{'id': x, 'label': str(x), 'color':color(x)} for x in sequence]
	return render_template('graph_template.html', n=num, id_dict = json.dumps(id_dict), edge_dict=json.dumps(edge_dict))

if __name__=="__main__":
	app.run()
