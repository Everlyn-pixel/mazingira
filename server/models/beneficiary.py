from extensions import db

class Beneficiary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    inventory = db.Column(db.String(120), nullable=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

    def __repr__(self):
        return f'<Beneficiary {self.name}>'
