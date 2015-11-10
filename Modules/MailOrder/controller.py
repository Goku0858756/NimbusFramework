__author__ = 'N05F3R4TU'
from nimbus import Nimbus

class MailOrder(Nimbus):
    """
    This Object is meant to listen to my Mail account with a REST API
    and when it detects a incoming email. It will Check if the mail
    for condition Through the Rules.
    """
    def __init__(self):
        super(MailOrder, self).__init__()
        self.name = "MailOrder Object"
        self.test_method()