import requests
from internet_domain import InternetDomains

def domains_search(domain:str):
    response = requests.get(f"https://api.domainsdb.info/v1/domains/search?domain={domain}")
    return get_results(response) if (response) else "Oops...404"
        
def get_results(response):
    # convert to json format
    data_domains = response.json()["domains"]
    #instantiate class
    domains = InternetDomains(data_domains)
    return f"Dominios inactivos: {domains.inactive_domains()} \nDominios activos: {domains.active_domains()}\nAlgunos que existen: \n{domains.list_domains()}"