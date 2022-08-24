from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, TEXT, Text, Float
from sqlalchemy.orm import declarative_base, relationship
from swagger_server.models.player import Player as PlayerModel
from swagger_server.models.game import Game as GameModel
from swagger_server.models.fixture import Fixture as FixtureModel

Base = declarative_base()


class Team(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(50))
    team_logo = Column(String(50))
    form = Column(String(50))
    description = Column(String(50))


class PlayerFixture(Base):
    __tablename__ = "player_fixture"

    player_fixture_id = Column(String, primary_key=True)
    player_id = Column(Integer)
    fixture_id = Column(Integer)
    rating = Column(Float(25))
    position = Column(String(1))

class TeamStanding(Base):
    __tablename__ = "team_standing"

    team_league_season_id = Column(String, primary_key=True)
    team_id = Column(Integer)
    league_id = Column(Integer)
    season = Column(Integer)
    points = Column(Integer)
    goals_diff = Column(String(10))
    form = Column(String(10))
    description = Column(String(50))
    rank = Column(Integer)

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
    season_year = Column(Integer)
    date = Column(String(50))

    def as_model(self):
        return FixtureModel(self.fixture_id, self.referee, self.home_id, self.away_id, self.goals_ft_home,
                            self.goals_ft_away, self.league_id, self.season_year, self.round, self.date)

    def __repr__(self):
        return f"Fixture(id={self.fixture_id}, date={self.date}, away_id={self.away_id}, home_id={self.home_id})"
