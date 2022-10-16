from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ende'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    costs = models.CurrencyField(
        initial=0
    )
    effort = models.IntegerField(
        choices=[
            [1, 'fast keine'],
            [2, 'sehr wenig'],
            [3, 'etwas'],
            [4, 'ziemlich viel'],
            [5, 'sehr viel'],
        ],
        widget=widgets.RadioSelect
    )
    attention = models.IntegerField(
        choices=[
            [1, 'fast keine'],
            [2, 'sehr wenig meiner'],
            [3, 'etwas meiner'],
            [4, 'die meiste meiner'],
            [5, 'meine volle'],
        ],
        widget=widgets.RadioSelect
    )
    use_data = models.BooleanField(
        choices=[
            [True, 'Ja'],
            [False, 'Nein'],
        ]
    )
    comments = models.LongStringField(
        label='',
        blank=True
    )
    time_end = models.StringField()
    study_completed = models.BooleanField(
        initial=False
    )
    srsn_check_pass = models.BooleanField(
        initial=False
    )
    Auszahlung = models.StringField(
        choices=[
            [True, 'SVO'],
            [False, 'Conditional_Cooperation']
        ]
    )


# PAGES
class SeriousnessCheck(Page):
    form_model = 'player'
    form_fields = ['effort','attention','use_data']

    def before_next_page(player, timeout_happened):
        player.study_completed = True
        import random
        player.Auszahlung = random.choice(["SVO", "Conditional_Cooperation"])
        with open('_static/Participated.txt', 'a') as file:
            if(player.participant.personal_code != "123456"):
                file.write('\n')
                file.write(player.participant.personal_code)
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        if player.use_data:
            player.srsn_check_pass = True

        with open('_static/CountParticipation.txt', 'r') as file:
            txt = int(file.read())
            print(txt)
            txt += 1
            print(txt)
        if(player.participant.code != "123456") and player.use_data:
                with open('_static/CountParticipation.txt', 'w') as file:
                    file.write(str(txt))

class Debriefing(Page):
    form_model = 'player'
    form_fields = ['comments']
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

class Finish(Page):
    pass


page_sequence = [SeriousnessCheck, Debriefing, Finish]
