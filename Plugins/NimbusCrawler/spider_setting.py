__author__ = 'N05F3R4TU'
__all__ = ["SpiderSetting"]

class SpiderSetting(object):
    """
    Spider Configurations per Session
    """

    def __init__(self):
        import yaml, os

        self.name = "Crawler Settings Template Object"
        self.this_path = os.path.dirname(os.path.realpath(__file__))
        self.settings = ""

        # default settings
        # default = open("default_setting.yml", mode="r")

        with open("{}/spider_settings.yml".format(self.this_path), mode="r") as setting:
            self.settings = yaml.load(setting)

        # defence
        self.proxy = []
        self.vpn = []

        # Visibility
        self.verbose = self.settings["setting"]["verbose"]

        # spoof
        self.userAgent = {}
        self.cookies = {}
        self.session = {}

        # look human
        self.timeout = self.settings["setting"]["timeout"]
        self.redirect_follow = self.settings["setting"]["follow_redirect"]

        # misc
        self.depth = self.settings["setting"]["crawl_depth"]
        self.baseOnly = self.settings["setting"]["base_domain"]
        self.threads = self.settings["setting"]["threads"]

        # mode
        self.mode_scan = self.settings["setting"]["modes"]["scan"]
        self.mode_attack = self.settings["setting"]["modes"]["attack"]

        # schemes allowed
        # self.allow_scheme = config["allow_scheme"]
        self.allow_scheme = self.settings["setting"]["allow_scheme"]

        # auth
        self.auth_username = self.settings["auth"]["username"]
        self.auth_password = self.settings["auth"]["password"]
        self.auth_basic = self.settings["auth"]["use_basic"]
        self.auth_oauth = self.settings["auth"]["use_oauth"]


    def __str__(self):
        return str(self.__dict__)

    def user_agent(self):
        """Set UserAgent"""
        pass
