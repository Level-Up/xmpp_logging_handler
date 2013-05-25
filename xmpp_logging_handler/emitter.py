import xmpp


class Send():

    def __init__(self, to, message, config_dict):
        client = xmpp.Client(host)
        client.connect(server=(config_dict['host'], config_dict['port']))
        client.auth(config_dict['username'],
                    config_dict['password'],
                    config_dict['name'])
        client.sendInitPresence()
        message = xmpp.Message(to, message)
        message.setAttr('type', 'chat')
        client.send(message)
