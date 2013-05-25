import logging
from emitters.gtalk import Send


class XMPPHandler(logging.Handler):

    def __init_(self,
                username=False,
                password=False,
                recipients=[],
                host='talk.google.com',
                port=5223,
                name='python_log_bot'):

        config_dict = {'username': username,
                       'password': password,
                       'host': host,
                       'port': port,
                       'name': name
                       }
        logging.Handler.__init__(self)

    def emit(self, record):
        message = self.format(record)
        for recipient in self.recipients:
            Send(recipient, message, config_dict)
