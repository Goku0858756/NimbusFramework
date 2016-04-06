__author__ = 'N05F3R4TU'


class NimbusDebug(object):

    def __init__(self):
        self.name = "Nimbus Debug Controller Object"

    @classmethod
    def save_log(cls, msg):
        import os

        full_path = os.path.dirname(os.path.realpath(__file__))
        with open("{}/test_log_file.txt".format(full_path), mode="a") as log:
            log.writelines("{}\n\n".format(msg))
            print("Log File Dumped")

        del os

# if __name__ == '__main__':
#     NimbusDebug.save_log("hahahhaa")
    # datetime()    __class__.__name__
    # Error number
    # Error message


    """
    Meerdere spiders tegelijk over zelfde request session
    get(block=True)

    LogFile beter aanpassen aan /dir/ip_to_int_conversion.log >> @session_date enumerate dan daaronder alles append

    crawl job als thread

    en Tmux window/Pane openen vanuit commandline

    voor beginnen van session, check eerst of ip_to_int session/data_dump bestaat
    zo ja kopier alle links naar Array van bestaande URLs en in de queue om te kijken of er nieuwe links zijn

    Beter exceptions opvangen door de Framework heen

    en doe een Nose_test
    """