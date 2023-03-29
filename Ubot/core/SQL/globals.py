from . import BASE, SESSION
from sqlalchemy import Column, String, UnicodeText, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound



class Globals(BASE):
    __tablename__ = "globals"
    user_id = Column(String(14), primary_key=True)
    variable = Column(String, primary_key=True, nullable=False)
    value = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, variable, value, user_id):
        self.user_id = (user_id)
        self.variable = str(variable)
        self.value = value
        


Globals.__table__.create(checkfirst=True)


def ambil_grup(user_id):
    try:
        return SESSION.query(Globals).filter(Globals.user_id == user_id, Globals.variable == "GRUPLOG").one().value
    except NoResultFound:
        return None

def addgvar(user_id, variable, value):
    if SESSION.query(Globals).filter(Globals.user_id == user_id, Globals.variable == str(variable)).one_or_none():
        delgvar(user_id, variable)
    adder = Globals(user_id=user_id, variable=str(variable), value=value)
    SESSION.add(adder)
    SESSION.commit()


def delgvar(user_id, variable):
    rem = (
        SESSION.query(Globals)
        .filter(Globals.user_id == user_id, Globals.variable == str(variable))
        .delete(synchronize_session="fetch")
    )
    if rem:
        SESSION.commit()


def gvarstatus(user_id, variable):
    try:
        return SESSION.query(Globals).filter(Globals.user_id == user_id, Globals.variable == str(variable)).first()
    except BaseException:
        return None
    finally:
        SESSION.close()