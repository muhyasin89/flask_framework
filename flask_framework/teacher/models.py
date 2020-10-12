from flask_framework.database import (
    Column,
    PkModel,
    db,
    reference_col,
    relationship,
)

class Earning(PkModel):
    __tablename__ = "earning"
    subject = Column(db.String(80), unique=True, nullable=False)
    number_by = Column(db.String(30), nullable=True)
    total = Column(db.Integer(), nullable=True)
