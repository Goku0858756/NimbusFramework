__author__ = 'N05F3R4TU'

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


if __name__ == '__main__':

    wp = DiscoverWordpress()
    wp.wp_themes()
    # http://www.giantflyingsaucer.com/blog/?cat=6