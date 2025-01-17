import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    subscription_date = Column(DateTime, nullable=False)
    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    weather = Column(String(250))
    population = Column(Integer, nullable=False)
    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name=Column(String(250), nullable=False)
    gender=Column(String(250), nullable=False)
    species=Column(String(250), nullable=False)
    favorites = relationship('Favorite', back_populates='character')
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id=Column(Integer, ForeignKey("planet.id"), nullable=True)
    character_id=Column(Integer, ForeignKey("character.id"), nullable=True)

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
