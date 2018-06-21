import requests

url = 'https://graph.facebook.com/243712686379081/'
access_token = 'EAACEdEose0cBAKjDscis0JlXCeF8lREVbXwWorPj9m8YDtZAZBJXzPZBoLroDZCDGRa77wpfpfPdDpLt2cxEYt9R5gVkrZCW64wDTA4biezQOStFxETdSBIyPCKZB1h33XjoPWamEj76A0quLizPcDjaux33GmbZABzfZBFydb9Eer7ymGDgV7ApO8ti1PmNk10ZD'


def get_feed(url, access_token):
    feed = requests.get(url, access_token)
    print(feed)


get_feed(url, access_token)
