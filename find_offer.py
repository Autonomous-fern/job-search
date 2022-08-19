import requests  # module pour récupérer le code html d'une page
from bs4 import BeautifulSoup  # module pour lire l'html d'une page
import time  # nous permet de temporiser les requêtes à l'api dans une loop


def find_offer(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "lxml")
        jobDescription = soup.find('div', {'data-automation': 'searchResults'})
        return jobDescription.get_text()
    else:
        return None


url1 = "https://www.seek.com.au/devops-jobs/in-All-Sydney-NSW"

print(find_offer(url1))


# !! UPDATE >> the website have been updated and is not static anymore !!
