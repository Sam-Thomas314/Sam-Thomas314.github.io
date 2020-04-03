from app import db

class User(db.model):
    customer_id = db.column(db.Integer, primary_key=True)
    Customer = db.column(db.String(64), index=True, unique=True)
    Total = db.column(db.Integer, index=True, unique=True)
    In = db.column(db.In)
    Out = db.column(db.Out)

    def __repr__(self):
        return '<User {}>'.format(self.username)


