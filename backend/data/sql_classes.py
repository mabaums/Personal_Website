from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, TEXT, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)
    birthdate = Column(TIMESTAMP)
    season_year = Column(Integer)
    photo = Column(Text)

    def __repr__(self):
        return f"Player(id={self.player_id}, name={self.name}, firstname={self.firstname}, lastname={self.lastname}, photo={self.photo})"


class Fixture(Base):
    __tablename__ = "fixture"

    fixture_id = Column(Integer, primary_key=True)
    referee = Column(String(50))
    league_id = Column(Integer)
    round = Column(String(50))
    goals_ft_home = Column(Integer)
    goals_ft_away = Column(Integer)
    goals_ht_home = Column(Integer)
    goals_ht_away = Column(Integer)
    away_id = Column(Integer)
    home_id = Column(Integer)

    def __repr__(self):
        return f"Fixture(id={self.fixture_id})"


