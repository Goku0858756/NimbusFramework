__author__ = 'N05F3R4TU'

def robots(url):
    """
    Check if there is a Robots.txt @URL
    :param url:
    :return:
    """
    import requests

    r = requests.get("{}/robots.txt".format(url))
    print(r.text)
    print(r.status_code)

    return r.status_code, r.text

# if __name__ == '__main__':
#     robots(url="http://delangejammer.nl/")