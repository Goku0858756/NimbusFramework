__author__ = 'N05F3R4TU'
import socket

class Bot(object):
    """
    This will be the main Bot Object
    """
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.bot_nick = "kristina kazarina"
        self.bot_id = 666
        self.server = "irc.freenode.net"
        self.channel = "#HRO"

        self.connect()

        while True:  # Be careful with these! it might send you to an infinite loop
            ircmsg = self.ircsock.recv(2048)  # receive data from the server
            ircmsg = ircmsg.strip('\n\r')  # removing any unnecessary linebreaks.
            print(ircmsg)  # Here we print what's coming from the server

            if ircmsg.find(":Hello " + self.bot_nick) != -1:  # If we can find "Hello Mybot" it will call the function hello()
                self.hello()

            if ircmsg.find("PING :") != -1:  # if the server pings us then we've got to respond!
                self.ping()

    def connect(self):
        """
        Here we connect to the server using the port 6667
        :return:
        """
        self.ircsock.connect((self.server, 6667))
        self.ircsock.send("USER " + self.bot_nick + " " + self.bot_nick + " " + self.bot_nick + " :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n")  # user authentication
        self.ircsock.send("NICK " + self.bot_nick + "\n")  # here we actually assign the nick to the bot
        self.join_channel(channel=self.channel)
        return

    def ping(self):
        """
        This is our first function! It will respond to server Pings.
        :return:
        """
        return self.ircsock.send("PONG :pingis\n")

    def send_msg(self, channel, msg):
        return self.ircsock.send("PRIVMSG " + channel + " :" + msg + "\n")

    def join_channel(self, channel):
        return self.ircsock.send("JOIN " + channel + "\n")

    def hello(self):
        return self.ircsock.send("PRIVMSG " + self.channel + " :Hello!\n")

if __name__ == '__main__':
    bot = Bot()
