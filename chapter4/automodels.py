from typing import Optional
import datetime

from sqlalchemy import Date, Float, ForeignKey, Integer, String
#from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

#class Base(DeclarativeBase):
#    pass


class League(Base):
    __tablename__ = 'league'

    league_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    league_name: Mapped[str] = mapped_column(String, nullable=False)
    scoring_type: Mapped[str] = mapped_column(String, nullable=False)
    last_changed_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    team: Mapped[list['Team']] = relationship('Team', back_populates='league')


class Player(Base):
    __tablename__ = 'player'

    player_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    position: Mapped[str] = mapped_column(String, nullable=False)
    last_changed_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    gsis_id: Mapped[Optional[str]] = mapped_column(String)

    performance: Mapped[list['Performance']] = relationship('Performance', back_populates='player')
    team_player: Mapped[list['TeamPlayer']] = relationship('TeamPlayer', back_populates='player')


class Performance(Base):
    __tablename__ = 'performance'

    performance_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    week_number: Mapped[str] = mapped_column(String, nullable=False)
    fantasy_points: Mapped[float] = mapped_column(Float, nullable=False)
    player_id: Mapped[int] = mapped_column(ForeignKey('player.player_id'), nullable=False)
    last_changed_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    player: Mapped['Player'] = relationship('Player', back_populates='performance')


class Team(Base):
    __tablename__ = 'team'

    team_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    team_name: Mapped[str] = mapped_column(String, nullable=False)
    league_id: Mapped[int] = mapped_column(ForeignKey('league.league_id'), nullable=False)
    last_changed_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    league: Mapped['League'] = relationship('League', back_populates='team')
    team_player: Mapped[list['TeamPlayer']] = relationship('TeamPlayer', back_populates='team')


class TeamPlayer(Base):
    __tablename__ = 'team_player'

    team_id: Mapped[int] = mapped_column(ForeignKey('team.team_id'), primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey('player.player_id'), primary_key=True)
    last_changed_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    player: Mapped['Player'] = relationship('Player', back_populates='team_player')
    team: Mapped['Team'] = relationship('Team', back_populates='team_player')