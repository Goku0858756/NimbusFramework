__author__ = 'N05F3R4TU'

# TODO: Plugins: Gmail
# TODO: Send automated emails
# TODO: Compose emails on command line
# TODO: Send email with attachment

class Gmail(object):

    def __init__(self, mail_title, mail_message, mail_to):
        import datetime
        import smtplib

        self.MAIL_FROM          = self.config()['from']
        self.MAIL_TO            = [mail_to]
        self.MAIL_DATE          = datetime.datetime.now()
        self.MAIL_TITLE         = mail_title
        self.MAIL_DESCR         = mail_message
        self.MAIL_ATTACHMENT    = ""
        self.MAIL_USERNAME      = self.config()['user']
        self.MAIL_PASSWORD      = self.config()['password']
        self.MAIL_SERVER        = smtplib.SMTP('smtp.gmail.com', int('587'))

    def config(self):
        """
        Configuration Function
        :return:
        """
        return {'user': "***", 'password': "***", "from": "***"}

    def message(self):
        """
        Compose Full Mail
        :return:
        """
        return "\From: %s\nTo: %s\nSubject: %s\n\n%s " % (self.MAIL_FROM, ", ".join(self.MAIL_TO), self.MAIL_TITLE, self.MAIL_DESCR)

    def send(self):
        """
        Send Mail Methode
        :return:
        """
        try:
            self.MAIL_SERVER.ehlo()
            self.MAIL_SERVER.starttls()
            self.MAIL_SERVER.login(user=self.MAIL_USERNAME, password=self.MAIL_PASSWORD)
            print("Email Send Succesfully")
            return self.MAIL_SERVER.sendmail(from_addr=self.MAIL_FROM, to_addrs=self.MAIL_TO, msg=self.message())
        except Exception as e:
            print(str(e))
        finally:
            self.MAIL_SERVER.close()


def main():

    compose = Gmail(mail_title='TesterTester', mail_message='Message Body', mail_to='***')
    compose.send()

if __name__ == '__main__':
    main()