from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['test']
    def vars_for_template(self):
        return {'img_range': range(Constants.endowment+1)}

class Results(Page):

    pass


page_sequence = [
    MyPage,
    Results
]

