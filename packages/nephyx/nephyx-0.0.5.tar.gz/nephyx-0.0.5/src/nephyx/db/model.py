from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
import re


class ModelBase(DeclarativeBase):

    __abstract__ = True

    @declared_attr.directive
    def __tablename__(self) -> str:
        names = re.split("(?=[A-Z])", self.__name__)
        return "_".join([x.lower() for x in names if x])
