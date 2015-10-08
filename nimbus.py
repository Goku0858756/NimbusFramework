__author__ = 'N05F3R4TU'

# TODO: Nimbus Own Envirement [ @startup ]
# TODO: PID file tracking
# mongod --pidfilepath ~/NimbusFramework/NimbusFramework/Database/dbmongo.pid

# TODO: Create Basic Crawler
# TODO: Create MasScanner
# TODO: Create Plugins
# TODO: Plugins: Gmail
# TODO: Create System
# TODO: System: [ check for ] Update
# TODO: System: Encryption and Decryption
# TODO: Thread Control System
# TODO: CommandLineInterface

# MOST IMPORTANT
# TODO: Threading
# TODO: Services
# TODO: Modules
# TODO: Plugins
# TODO: Body/Framework
# TODO: Documentation System Pythonic

"""
This Child of Crawler called Spiderling Will POP
an HREF from the Mother-Crawler-Object and will gather all HREFs from the given URL
 - Will Filter URLs by Internal_url && External_url with the Methods, which are Passed by
   the Mother-Object [ inherritence ]

 - The URLs will be stored into a Set() in the Mother-Crawler-Object

"""

"""
crawl basis pagina [ doe alles in een Set() ]
    Plaats van een Set() naar de Queue()
        Maak een Spiderling session aan, POP van de Queue(), MAAR ook APPEND naar een Lijst met de AL Gecrawlde URLs

        Als de NEW URL niet in de (((AL_CRAWLED_LIST)) zit, voeg toe aan de moeder_Set()

            Wanneer Queue None is ::

                Zet Set() over naar Queue() en Repeat
"""



"""
Check of URL overkomt met base_url
    Check of het een XPATH is
        Checl of het een SCHEME heeft
        Check of het een NETLOC heeft
            Check of het een PATH is

    Check of het een subdomain is
    Check of het een javascript link is find()

    Check of het een Social Media Link is

"""

"""
schemes: ['http', 'mailto', 'ftp']
"""