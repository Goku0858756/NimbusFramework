__author__ = 'N05F3R4TU'

class HipChat(object):
    """
    HipChat Bot made just for Nimbus ;)
    """

    def __init__(self, token=None, room=None, message=None):
        self.message = message
        self.message_format = "html"
        self.message_color = "blue"
        self.message_notify = True

        self.token = token
        self.room = room
        self.api_version = 'v2'

    def hipchat_api(self):
        return 'https://api.hipchat.com/{}/room/{}/notification'.format(self.api_version, self.room)

    def hipchat_headers(self):
        return {
            "content-type": "application/json",
            "authorization": "Bearer %s" % self.token
        }

    def hipchat_payload(self):
        return {
            'message': self.message, 'color': self.message_color, 'message_format': self.message_format, 'notify': self.message_notify
        }

    def post(self):
        import requests, json
        """
        To post to your #Channel
        :return:
        """
        post = requests.post(url=self.hipchat_api(), headers=self.hipchat_headers(), data=json.dumps(self.hipchat_payload()))
        return print(post.text)


if __name__ == '__main__':

    token = '-----'
    room = '----'

    HipChat(token=token, room=room, message="I got a kiss 4 you").post()
