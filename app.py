from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") 
def index():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ" 
    return render_template('index.html', page_title=title, heading=heading)


@app.route('/doors_table/<int:doors_table_id>')
def single_doors_table(doors_table_id):
    return render_template('single_doors_table.html')


@app.route('/delivery')
def delivery():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('delivery.html', page_title=title, heading=heading)


if __name__=="__main__": 
    app.run(debug=True)