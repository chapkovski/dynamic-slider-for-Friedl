from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Andy'

doc = """
refugee
"""


class Constants(BaseConstants):
    name_in_url = 'refugee'
    players_per_group = None
    num_rounds = 1
    endowment = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    a = models.IntegerField()
    test = models.IntegerField(
        min=0, max=Constants.endowment,
        widget=widgets.Slider(attrs={'step': '1'}), default=0, blank=True
    )
