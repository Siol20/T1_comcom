from otree.api import *

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'beginn'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    einverstaendnis = models.BooleanField( blank = True )
    time_end = models.StringField()
    code = models.StringField(label="")


# PAGES
class introduction(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


class informed_consent(Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")


class einwilligung(Page):
    form_model = 'player'
    form_fields = ['einverstaendnis']

    @staticmethod
    def error_message(player, values):
        if values['einverstaendnis'] is not True:
            return 'Sie müssen die Teilnahmebedingungen akzeptieren, um an der Studie teilnehmen zu können.'
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")



class Code_Eingabe(Page):
    form_model = 'player'
    form_fields = ['code']

    @staticmethod
    def error_message(player, values):
        if len(values['code']) !=6:
            return 'Ihr Code muss sechsstellig sein'

    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        player.participant.label = player.code


class Einführung (Page):
    def before_next_page(player, timeout_happened):
        import datetime
        player.time_end = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

page_sequence = [introduction, informed_consent, einwilligung, Code_Eingabe, Einführung]
