import requests

class Proxy:

    def __init__(self, instance):

        self.instance = instance

    def proxy(self):

        object_instance = self.instance

        if object_instance.number % 2 == 0:

            response = requests.get("https://restcountries.eu/rest/v2/region/asia")
            print(response.content)
            return True

        else:
            response = requests.get("https://restcountries.eu/rest/v2/region/europe")
            print(response.content)
            return True


        return False