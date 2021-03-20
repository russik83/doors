from app import db


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


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
