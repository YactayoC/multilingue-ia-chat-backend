from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from src.database.db_pg import db


class Clients(db.Model):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    uuid = Column(String, nullable=False, unique=True)
    fullname = Column(String(80))
    cellphone = Column(String(80))
    email = Column(String(80), unique=True, nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"))
    created_at = Column(DateTime, default=datetime.now())

    conversations_client = relationship(
        "Conversations",
        back_populates="client",
    )

    language = relationship(
        "Languages",
        back_populates="clients",
    )

    requests = relationship(
        "Requests",
        back_populates="client",
    )

    def __init__(
        self,
        email,
        fullname=None,
        cellphone=None,
        language_id=None,
        created_at=None,
    ):
        self.uuid = str(uuid.uuid4())
        self.email = email
        self.fullname = fullname
        self.cellphone = cellphone
        self.language_id = language_id
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.uuid,
            "idv2": self.id,
            "fullname": self.fullname,
            "cellphone": self.cellphone,
            "email": self.email,
            "language": self.language.to_dict(),
            "created_at": self.created_at,
        }
