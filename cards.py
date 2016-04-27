from errbot import BotPlugin, botcmd

class Card(object):
    def __init__(self, title='', body=''):
        self.title=title
        self.body=body

class CardsMaker(BotPlugin):
    @botcmd(template='card')
    def cards(self, msg, args):
        c = Card('my title', 'my body')
        yield c.__dict__
        c = Card('my title', 'my body')
        c.thumbnail = 'https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/err.png'
        yield c.__dict__
        c = Card('my title', 'my body')
        c.link = 'http://www.google.com'
        yield c.__dict__
        c = Card('my title', 'my body')
        c.image = 'http://www.rudebaguette.com/assets/big-data.jpg'
        yield c.__dict__
