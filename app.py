from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 入力された名前と景品を取得
        names = request.form.getlist('names')
        prizes = request.form.getlist('prizes')
        n_lines = len(names)
        depth = 15  # あみだの縦の長さ

        # 横線をランダムに生成
        amida_grid = []
        for d in range(depth):
            row = []
            for i in range(n_lines - 1):
                # 横線が連続しないように調整（30%の確率で線を引く）
                if i > 0 and row[i-1] == 1:
                    row.append(0)
                else:
                    row.append(1 if random.random() < 0.3 else 0)
            amida_grid.append(row)

        return render_template('result.html', names=names, prizes=prizes, 
                               amida_grid=amida_grid, n_lines=n_lines, depth=depth)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)