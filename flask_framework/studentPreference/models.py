import enum

from flask_framework.database import (
    Column,
    PkModel,
    db,
    reference_col,
    relationship,
)

class PreferenceStatusEnum(enum.Enum):
    bookmark = 'bookmark'
    uninterested = 'uninterested'


class studentPreference(PkModel):
    subject = relationship("Subject", backref="preference")
    status = db.Column(
        db.Enum(PreferenceStatusEnum),
        default=PreferenceStatusEnum.employed,
        nullable=False
    )
