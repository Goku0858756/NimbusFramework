__author__ = 'N05F3R4TU'

class Banners(object):

    def options(self):
        import inspect
        from veryprettytable import VeryPrettyTable

        commands = VeryPrettyTable(["Command", "Description"])
        commands.align = "l"
        commands.padding_width = 2

        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__"]:
                # print("%s\t\t\t%s" % (attr, getattr(self, attr).__doc__))
                commands.add_row([attr, getattr(self, attr)()])
        return commands

    def randomize(self):
        import inspect
        import random

        banner = []
        for attr in [attr for attr in dir(self) if inspect.ismethod(getattr(self, attr))]:
            if attr not in ["options", "__init__", "randomize"]:
                banner.append(attr)
        getattr(self, random.choice(banner))()
        # return random.choice(banner)


    def daemon_threat(self):
        print("""
                            daemon_threat
                      \,,,/      was here
                      (o o)
            ----o000o--(_)--o000o----""")

    def kilroy(self):
        print("""
                            kilroy was
                      \,,,/      here
                      (o o)
            ----o000o--(_)--o000o----""")

    def rain_with_rage(self):
        print("""
            _______________▄▄▄▄▄▄__▄▄▄▄▄
            __________▄▄▀▀_______▀▀▀____▀▀█▄
            _____▄▄▄█▀________________▄▄▄▄▄██▄
            __█▀▀▄▄▄▄▄▄▄██████████████████▄
            _███████████████████████████████▄
            █████████████████████████████████
            ▀████████████████████████████████
            _▀██████████████████████████████▀
            ___▀██████████████████████████▀▀
            __________▀███████████████████▀
            ________▄▄____▀▀▀▀▀▀_____▄_▀▀
            _____▄███_________▄____▄██____
            ___█████_______▄██___████____▄
            ____▀██▀_____▄████___▀▀▀__▄██
            __________▄█__████________████
            _______▄███___▀▀_________████
            ________▀▀_________________▀▀
            ________▄________________▄
            ____▄███_________▄____▄██
            __█████_______▄██___████____▄
            ___▀██▀_____▄████___▀▀▀__▄██
            _________▄█__████________████
            ______▄███___▀▀_________████
            _______▀▀_________________▀▀

            -- Rain with Rage,
                    exploit with Love --""")

    def arachnida(self):
        print('''
                   ;               ,
                 ,;                 '.
                ;:                   :;
               ::                     ::
               ::                     ::
               ':                     :
                :.                    :
             ;' ::                   ::  '
            .'  ';                   ;'  '.
           ::    :;                 ;:    ::
           ;      :;.             ,;:     ::
           :;      :;:           ,;"      ::
           ::.      ':;  ..,.;  ;:'     ,.;:
            "'"...   '::,::::: ;:   .;.;""'
                '"""....;:::::;,;.;"""
            .:::.....'"':::::::'",...;::::;.
           ;:' '""'"";.,;:::::;.'""""""  ':;
          ::'         ;::;:::;::..         :;
         ::         ,;:::::::::::;:..       ::
         ;'     ,;;:;::::::::::::::;";..    ':.
        ::     ;:"  ::::::"""'::::::  ":     ::
         :.    ::   ::::::;  :::::::   :     ;
          ;    ::   :::::::  :::::::   :    ;
           '   ::   ::::::....:::::'  ,:   '
            '  ::    :::::::::::::"   ::
               ::     ':::::::::"'    ::
               ':       """""""'      ::
                ::                   ;:
                ':;                 ;:"
                  ';              ,;'
        ''')

if __name__ == '__main__':
    b = Banners()
    b.arachnida()