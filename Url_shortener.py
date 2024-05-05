import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    def shorten_url(self, original_url):
        short_url = self.generate_short_url()

        while short_url in self.url_mapping:
            short_url = self.generate_short_url()

        self.url_mapping[short_url] = original_url
        return short_url

    def retrieve_url(self, short_url):
        return self.url_mapping.get(short_url, None)

if __name__ == "__main__":
    shortener = URLShortener()
    
    original_url = input("enter url:")
    short_url = shortener.shorten_url(original_url)
    print("Shortened URL:", short_url)

    retrieved_url = shortener.retrieve_url(short_url)
    print("Retrieved URL:", retrieved_url)
