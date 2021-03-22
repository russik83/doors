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
    heading = "СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('glass.html', page_title=title, heading=heading)


@app.route('/interior/single_light')
def single_light():
    title = "Мир дверей"
    heading = "ПРОСТЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('interior/single_light.html', page_title=title, heading=heading)


@app.route('/interior/single_letters')
def single_letters():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ LETTERS"
    return render_template('interior/single_letters.html', page_title=title, heading=heading)


@app.route('/interior/single_fantasy')
def single_fantasy():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FANTASY"
    return render_template('interior/single_fantasy.html', page_title=title, heading=heading)


@app.route('/interior/single_satin')
def single_satin():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ SATIN"
    return render_template('interior/single_satin.html', page_title=title, heading=heading)


@app.route('/interior/single_florid')
def single_florid():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FLORID"
    return render_template('interior/single_florid.html', page_title=title, heading=heading)


@app.route('/interior/single_tripleks')
def single_tripleks():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ТРИПЛЕКС"
    return render_template('interior/single_tripleks.html', page_title=title, heading=heading)


@app.route('/interior/single_illusion')
def single_illusion():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ILLUSION"
    return render_template('interior/single_illusion.html', page_title=title, heading=heading)


@app.route('/interior/single_classic')
def single_classic():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ В КЛАССИЧЕСКОМ СТИЛЕ"
    return render_template('interior/single_classic.html', page_title=title, heading=heading)


@app.route('/interior/single_flowers')
def single_flowers():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ FLOWERS"
    return render_template('interior/single_flowers.html', page_title=title, heading=heading)


@app.route('/interior/single_foto')
def single_foto():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ С ФОТОПЕЧАТЬЮ"
    return render_template('interior/single_foto.html', page_title=title, heading=heading)


@app.route('/interior/single_mirra')
def single_mirra():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ MIRRA"
    return render_template('interior/single_mirra.html', page_title=title, heading=heading)


@app.route('/interior/single_loft')
def single_loft():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ЛОФТ"
    return render_template('interior/single_loft.html', page_title=title, heading=heading)


@app.route('/interior/single_decor')
def single_decor():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ART DÉCOR"
    return render_template('interior/single_decor.html', page_title=title, heading=heading)


@app.route('/peregorodki')
def peregorodki():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ"
    return render_template('peregorodki.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_aluminum')
def single_aluminum():
    title = "Мир дверей"
    heading = "АЛЮМИНИЕВЫЕ ПЕРЕГОРОДКИ"
    return render_template('peregorodki/single_aluminum.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_razdvizhnyye')
def single_razdvizhnyye():
    title = "Мир дверей"
    heading = "РАЗДВИЖНЫЕ СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ И ДВЕРИ"
    return render_template('peregorodki/single_razdvizhnyye.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_apartments')
def single_apartments():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ ДЛЯ КВАРТИРЫ"
    return render_template('peregorodki/single_apartments.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_mirror')
def single_mirror():
    title = "Мир дверей"
    heading = "ЗЕРКАЛЬНЫЕ ПЕРЕГОРОДКИ"
    return render_template('peregorodki/single_mirror.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_smart')
def single_smart():
    title = "Мир дверей"
    heading = "СМАРТ ПЕРЕГОРОДКИ ИЗ СТЕКЛА"
    return render_template('peregorodki/single_smart.html', page_title=title, heading=heading)


@app.route('/peregorodki/single_office')
def single_office():
    title = "Мир дверей"
    heading = "ОФИСНЫЕ СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ"
    return render_template('peregorodki/single_office.html', page_title=title, heading=heading)


@app.route('/sauna')
def sauna():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ДЛЯ САУНЫ И БАНИ"
    return render_template('sauna.html', page_title=title, heading=heading)


@app.route('/sauna/single_ajio')
def single_ajio():
    title = "Мир дверей"
    heading = "ОФИСНЫЕ СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ"
    return render_template('sauna/single_ajio.html', page_title=title, heading=heading)


@app.route('/sauna/single_sauna_light')
def single_sauna_light():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ LIGHT ДЛЯ БАНИ"
    return render_template('sauna/single_sauna_light.html', page_title=title, heading=heading)


@app.route('/sauna/single_steam')
def single_steam():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ В ПАРНУЮ"
    return render_template('sauna/single_steam.html', page_title=title, heading=heading)


@app.route('/sauna/single_glassjet')
def single_glassjet():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ GLASSJET ДЛЯ САУНЫ"
    return render_template('sauna/single_glassjet.html', page_title=title, heading=heading)


@app.route('/sauna/single_hamam')
def single_hamam():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ХАМАМ"
    return render_template('sauna/single_hamam.html', page_title=title, heading=heading)


@app.route('/sauna/single_glassjet_colored')
def single_glassjet_colored():
    title = "Мир дверей"
    heading = "ЦВЕТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ GLASSJET"
    return render_template('sauna/single_glassjet_colored.html', page_title=title, heading=heading)


@app.route('/showers')
def showers():
    title = "Мир дверей"
    heading = "ДУШЕВЫЕ ОГРАЖДЕНИЯ ИЗ СТЕКЛА"
    return render_template('showers.html', page_title=title, heading=heading)


@app.route('/showers/single_corners')
def single_corners():
    title = "Мир дверей"
    heading = "ДУШЕВЫЕ УГОЛКИ ИЗ СТЕКЛА"
    return render_template('showers/single_corners.html', page_title=title, heading=heading)


@app.route('/showers/single_nishu')
def single_nishu():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДУШЕВЫЕ ДВЕРИ В НИШУ"
    return render_template('showers/single_nishu.html', page_title=title, heading=heading)


@app.route('/showers/single_soul')
def single_soul():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ДВЕРИ ДЛЯ ДУША"
    return render_template('showers/single_soul.html', page_title=title, heading=heading)


@app.route('/showers/single_shower_partitions')
def single_shower_partitions():
    title = "Мир дверей"
    heading = "СТЕКЛЯННЫЕ ПЕРЕГОРОДКИ ДЛЯ ДУША"
    return render_template('showers/single_shower_partitions.html', page_title=title, heading=heading)


@app.route('/showers/single_glass_partitions')
def single_glass_partitions():
    title = "Мир дверей"
    heading = "РАЗДВИЖНЫЕ ДУШЕВЫЕ ПЕРЕГОРОДКИ ИЗ СТЕКЛА"
    return render_template('showers/single_glass_partitions.html', page_title=title, heading=heading)


@app.route('/showers/single_bathroom_blinds')
def single_bathroom_blinds():
    title = "Мир дверей"
    heading = "РАЗДВИЖНЫЕ ДУШЕВЫЕ ПЕРЕГОРОДКИ ИЗ СТЕКЛА"
    return render_template('showers/single_bathroom_blinds.html', page_title=title, heading=heading)



if __name__=="__main__": 
    app.run(debug=True)
    