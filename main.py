from djangotenberg.client import APIClient

client = APIClient()

resp = client.url_to_pdf("https://google.com")