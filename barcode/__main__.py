import click
import requests
import requests
import xml.etree.ElementTree as ET

def isbn_search(isbn_number):
    base_url = "https://www.goodreads.com/search/index.xml"
    params = {  "q": isbn_number,
              "key": "" }
    res = requests.get(base_url, params = params)
    return res.content

@click.group()
def cli():
    click.echo("Barcode CLI V0.0.1")

@cli.command()
def isbn():
    isbn = click.prompt('Please enter ISBN', type=int)
    parse_search_result(isbn_search(isbn))

def parse_search_result(res):
    root = ET.fromstring(res)
    print(root[1][6][0][8][1].text)
