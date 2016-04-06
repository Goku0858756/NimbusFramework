__author__ = 'N05F3R4TU'

class Discover(object):
    """
    Main Discover Object
    """
    def __init__(self):
        self.name = "Main Discover Object"

    def is_wordpress(self):
        pass

    def is_joomla(self):
        pass

    def is_drupal(self):
        pass

    def is_typo3(self):
        pass

    def is_opencart(self):
        pass

    def is_magento(self):
        pass

    def is_oscommerce(self):
        pass

    def is_iis(self):
        pass

    def is_bootstrap(self):
        pass

    def is_node_js(self):
        pass

    def is_angular_js(self):
        pass

class DiscoverWordpress(object):

    def __init__(self):
        self.name = "Wordpress Paths Object"
        self.file_themes = "wp_themes.json"
        self.file_plugins = "wp_plugins.json"
        self.file_plugins_225 = "wp_plugins_225.json"
        self.file_paths = "wp_paths.json"

    def wp_themes(self):
        """
        Themes Generate from: http://themes.svn.wordpress.org
        :return:
        """
        with open(self.file_themes, mode="rt", buffering=2000) as wp:
            themes = [theme.strip() for theme in wp.readlines()]
        return themes

    def wp_paths(self):
        """
        Wordpress Paths
        :return:
        """
        with open(self.file_paths, mode="rt", buffering=2000) as wp:
            paths = [path.strip() for path in wp.readlines()]
        return paths

    def wp_plugins(self):
        """
        Wordpress Plugins
        :return:
        """
        with open(self.file_plugins, mode="rt", buffering=2000) as wp:
            plugins = [plugin.strip() for plugin in wp.readlines()]
        return plugins

    def wp_plugins_225(self):
        """
        Wordpress Plugins Top 225 Used
        :return:
        """
        with open(self.file_plugins_225, mode="rt", buffering=2000) as wp:
            plugins = [plugin.strip() for plugin in wp.readlines()]
        return plugins

class DiscoverJoomla(object):

    def __init__(self):
        self.name = "Joomla Paths Object"
        self.file_plugins = "joomla_plugins.json"
        self.file_themes = "joomla_themes.json"

    def joomla_themes(self):
        """
        Joomla Themes
        :return: a list with all Joomla themes
        """
        with open(self.file_themes, mode="rt", buffering=2000) as joomla:
            themes = [theme.strip() for theme in joomla.readlines()]
        return themes

    def joomla_paths(self):
        return "[ MISSING ] - Joomla All Files and Paths"

    def joomla_plugins(self):
        """
        Joomla Plugins
        :return: a list with all Joomla Plugins
        """
        with open(self.file_plugins, mode="rt", buffering=2000) as joomla:
            plugins = [plugin.strip() for plugin in joomla.readlines()]
        return plugins

class DiscoverDrupal(object):

    def __init__(self):
        self.name = "Drupal Paths Object"
        self.file_plugins = "drupal_plugins.json"
        self.file_themes = "drupal_themes.json"

    def drupal_themes(self):
        """
        Drupal Themes
        :return: a list with all Drupal themes
        """
        with open(self.file_themes, mode="rt", buffering=2000) as drupal:
            themes = [theme.strip() for theme in drupal.readlines()]
        return themes

    def drupal_paths(self):
        return "[ MISSING ] - Drupal All Files and Paths"

    def drupal_plugins(self):
        """
        Drupal Plugins
        :return: a list with all Drupal Plugins
        """
        with open(self.file_plugins, mode="rt", buffering=2000) as drupal:
            plugins = [plugin.strip() for plugin in drupal.readlines()]
        return plugins


class DiscoverTypo3(object):
    """
    Discover Typo3 CMS Framework
    URL: http://www.typo3exploit.com/
    URL: https://www.intelligentexploit.com/view-details.html?id=2400
    """

    def __init__(self):
        self.name = "Typo3 CMS Discovery"

class DiscoverOpenCart(object):
    """
    Discover OpenCart CMS Framework
    """

    def __init__(self):
        self.name = "Opencart CMS Framework Object"


if __name__ == '__main__':

    wp = DiscoverWordpress()
    wp.wp_themes()
    # http://www.giantflyingsaucer.com/blog/?cat=6