from sqlalchemy import Column, String, Float
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Apartment(Base):
    __tablename__ = 'apartments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    noiselevel = Column(Float, nullable=False)
    floor = Column(Float, nullable=False)
