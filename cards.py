from errbot import BotPlugin, botcmd

LOPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod " \
         "tempor incididunt ut labore et dolore magna aliqua."


class CardsMaker(BotPlugin):
    @botcmd
    def cards(self, msg, args):
        self.send_card(body='Body Only',
                       in_reply_to=msg)
        self.send_card(title='Title + Body',
                       body=LOPSUM,
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Thumbnail',
                       body=LOPSUM,
                       thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/err.png',
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Link',
                       body=LOPSUM,
                       link='http://www.google.com',
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Image',
                       body=LOPSUM,
                       image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                       in_reply_to=msg)
        self.send_card(title='Summary + Title + Body',
                       summary='Important Latin text, read carefully !',
                       body=LOPSUM,
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Fields',
                       body=LOPSUM,
                       fields=(('First Key','Value1'), ('Second Key','Value2')),
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Color positive',
                       body=LOPSUM,
                       color='red',
                       in_reply_to=msg)
        self.send_card(title='Title + Body + Color negative',
                       body=LOPSUM,
                       color='black',
                       in_reply_to=msg)
        self.send_card(title='EVEEERYTHINNNG !!!',
                       body='text body to put in the card',
                       thumbnail='https://raw.githubusercontent.com/errbotio/errbot/master/docs/_static/err.png',
                       image='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                       link='http://www.google.com',
                       fields=(('First Key', 'Value1'), ('Second Key', 'Value2')),
                       color='red',
                       in_reply_to=msg)
        return 'cards sent'
