"""
Title: URL shorter from command line



"""


class URLshorter:
    def __init__(self):
        self.url = {}

    """ Return shorted URL """
    def shorten(self, url: str) -> str:
        if url in self.url:
            return self.url[url]
        else:
            short_url = f'http://short.url/{len(self.url)}'
            self.url[url] = short_url
            return short_url

    """ Return expanded URL """

    def expand(self, short_url: str) -> str:
        for original_url, shortened_url in self.url.items():
            if shortened_url == short_url:
                return original_url
        return f'URL not found for {short_url}'


if __name__ == "__main__":
    url = URLshorter()
    print(url.shorten('https://www.google.com'))
    print(url.shorten('https://www.facebook.com'))
    print(url.shorten('https://www.twitter.com'))
    print(url.expand('http://short.url/0'))
    print(url.expand('http://short.url/1'))
    print(url.expand('http://short.url/2'))
    print(url.expand('http://short.url/3'))

    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
    # print(url.url['https://www.twitter.com'])
    # print(url.url)
    # print(url.url['https://www.google.com'])
    # print(url.url['https://www.facebook.com'])
