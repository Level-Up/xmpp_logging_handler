import logging
from emitter import Send
"""
from xmpp_logging_handler import XMPPHandler

"""

class XMPPHandler(logging.Handler):

    def __init__(self,
                 username=False,
                 password=False,
                 recipients=[],
                 host='gmail.com',
                 server='talk.google.com',
                 port=5223,
                 name='python_log_bot'):
        self.config_dict = {'username': username,
                            'password': password,
                            'host': host,
                            'server': server,
                            'port': port,
                            'name': name
                            }
        self.recipients = recipients
        logging.Handler.__init__(self)

    def emit(self, record):
        message = self.format(record)
        for recipient in self.recipients:
            Send(recipient, message, self.config_dict)
