from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)
import json

def collatz(n):
	total = []
	while n!=1:
		total.append(n)
		if n%2==0: n = n/2
		else: n = (n*3)+1
	total.append(n)
	return total

@app.route("/<num>")
def display(num):
	sequence = collatz(int(num))
	id_dict = [{'id': x, 'label': str(x)} for x in sequence]
	#id_dict.reverse()
	edge_dict = []
	for i in range(len(sequence)-1):
		edge_dict.append({'from':sequence[i], 'to':sequence[i+1]})
	#edge_dict.reverse()
	return render_template('graph_template.html', n=num, id_dict = json.dumps(id_dict), edge_dict=json.dumps(edge_dict))

if __name__=="__main__":
	app.run()
