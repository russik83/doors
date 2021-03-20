from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String, unique=True, nullable=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    door_list = db.relationship("Door", backref="door_id")

    def __repr__(self):
        return '<Category {} {}>'.format(self.name, self.description)


class Door(db.Model):
    __tablename__ = 'doors_table'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'))
    img_src = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    drawing = db.Column(db.String, nullable=False)
    colour = db.Column(db.String, nullable=False)
    material = db.Column(db.String, nullable=False)
    dimensions = db.Column(db.String, nullable=False)
    findings = db.Column(db.String, nullable=False)
    box = db.Column(db.String, nullable=False)
    availability = db.Column(db.String, nullable=False)
    term = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Door {} {}>'.format(self.name, self.description)


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


@app.route('/glass')
def glass():
    title = "Мир дверей"
    heading = "МЕЖКОМНАТНЫЕ СТЕКЛЯННЫЕ ДВЕРИ"
    return render_template('glass.html', page_title=title, heading=heading)


if __name__=="__main__": 
    app.run(debug=True)
    