from flask import Flask, render_template


app = Flask(__name__)


@app.route("/") 
def index():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ" 
    return render_template('index.html', page_title=title, heading=heading)


@app.route('/delivery')
def delivery():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('delivery.html', page_title=title, heading=heading)


@app.route('/glass')
def glass():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('glass.html', page_title=title, heading=heading)


@app.route('/single_light')
def single_light():
    title = "Мир дверей"
    heading = "ПРОСТЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('single_light.html', page_title=title, heading=heading)


@app.route('/single_letters')
def single_letters():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ LETTERS"
    return render_template('single_letters.html', page_title=title, heading=heading)


@app.route('/single_fantasy')
def single_fantasy():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FANTASY"
    return render_template('single_fantasy.html', page_title=title, heading=heading)


@app.route('/single_satin')
def single_satin():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ SATIN"
    return render_template('single_satin.html', page_title=title, heading=heading)


@app.route('/single_florid')
def single_florid():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FLORID"
    return render_template('single_florid.html', page_title=title, heading=heading)


@app.route('/single_tripleks')
def single_tripleks():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ТРИПЛЕКС"
    return render_template('single_tripleks.html', page_title=title, heading=heading)


@app.route('/single_illusion')
def single_illusion():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ILLUSION"
    return render_template('single_illusion.html', page_title=title, heading=heading)


@app.route('/single_classic')
def single_classic():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ В КЛАССИЧЕСКОМ СТИЛЕ"
    return render_template('single_classic.html', page_title=title, heading=heading)


@app.route('/single_flowers')
def single_flowers():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FLOWERS"
    return render_template('single_flowers.html', page_title=title, heading=heading)


@app.route('/single_foto')
def single_foto():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ С ФОТОПЕЧАТЬЮ"
    return render_template('single_foto.html', page_title=title, heading=heading)


@app.route('/single_mirra')
def single_mirra():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ MIRRA"
    return render_template('single_mirra.html', page_title=title, heading=heading)


@app.route('/single_loft')
def single_loft():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ЛОФТ"
    return render_template('single_loft.html', page_title=title, heading=heading)


@app.route('/single_decor')
def single_decor():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ART DÉCOR"
    return render_template('single_decor.html', page_title=title, heading=heading)


if __name__=="__main__": 
    app.run(debug=True)
    