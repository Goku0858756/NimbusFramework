__author__ = 'N05F3R4TU'
# import json
# from pprint import pprint
#
# path = "strings.json"
#
# with open(path) as useragent:
#     data = json.load(useragent)
#
# pprint(data)

class UserAgents(object):
    """
    This Object Will Update the Latest User-Agents for the Spiders
    """
    def __init__(self):
        self.agent = self.user_agent()

    def user_agent(self):
        """
        This method returns a random chosen User-Agent from a list-file
        :return:
        """
        import random
        # TODO: Automatic Check This Directory and Grab File user_agents.txt
        with open('/Users/N05F3R4TU/PycharmProjects/Arachnophobia/extract/HTML/user_agents.txt', mode="r+") as UA:
            agents_tuple = UA.readlines()
            return {'User-Agent': random.choice(agents_tuple)}

    def user_agent_update(self):
        """
        This Method Will Update the List of available User-Agents when Called For
        :return:
        """
        pass


if __name__ == '__main__':
    a = UserAgents()
    print(a.user_agent())
