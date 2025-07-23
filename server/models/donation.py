from extensions import db
from sqlalchemy.sql import func

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    is_anonymous = db.Column(db.Boolean, default=False)
    donation_type = db.Column(db.String(80), nullable=False) # one-time, recurring
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Donation {self.id}>'
