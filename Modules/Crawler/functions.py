from threading import Thread

class CrawlerFunctions:

    def __init__(self):
        self.name = "Crawler Functions Object"
        self.command = ""
        self.modus = ""
        self.crawler_thread = Thread


    def crawl(self, target=None):
        """[ CRAWL ] Like a Boss"""
        from Plugins.NimbusCrawler.spider import Spider

        # import os
        #
        # # os.system("tmux new-window -t Nimbus:123 -n Spider123")
        # # os.system("tmux send-keys -t Nimbus:123 'cd ~/virNimbus/; source bin/activate; cd Plugins/NimbusCrawler/; python spider.py -h;' C-m")

        url = target
        if target == None:

            url = self._queue_crawler.get(block=True)
            # check the queue and for every queue_target create a tmux new-window and crawl with daemon = False
            # MULTIPROCES . Proces

        # # start Spider() object with the given URL_target
        # s = Spider(url=url)
        # s.crawl()

        with Spider(url=url).crawl() as s:
            print("Started crawling from Arachnida")

    def treads(self):
        print("[ Is Alive ]: {}".format(self.crawler_thread.isAlive))
        print("[ Is Daemon]: {}".format(self.crawler_thread.isDaemon()))
        print("[ Get Name ]: {}".format(self.crawler_thread.getName()))
        print("[ ID get   ]: {}".format(self.crawler_thread.ident))

    def stop(self):
        print("Stop with crawling")
    def pause(self):
        print("Pause Crawler")
    def start(self):
        print("Start/Resume Crawling")
    # def use(self):
    #     crawl_usage()

    # def discover(self):
    #     """[ DISCOVER ] cms, framework, specific HTML5 stuff"""
    #
    #     """
    #         IF input_parameter == cms:
    #             then; Discover if TARGET is a type of CMS
    #         IF input_parameter == framework
    #             then; DISCOVER if TARGET is a using a type of FRAMEWORK
    #     """
    #     pass
