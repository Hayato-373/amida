from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        names = request.form.getlist('names')
        n_lines = len(names)
        depth = 15

        amida_grid = []
        for _ in range(depth):
            row = []
            for i in range(n_lines - 1):
                if i > 0 and row[i-1] == 1:
                    row.append(0)
                else:
                    row.append(1 if random.random() < 0.3 else 0)
            amida_grid.append(row)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)