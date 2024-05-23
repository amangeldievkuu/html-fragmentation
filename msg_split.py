from typing import Generator
import click
from bs4 import BeautifulSoup

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

MAX_LEN = 4096

def split_message(source: str, max_len=MAX_LEN) -> Generator[str, None, None]:
    """Splits the original message (`source`) into fragments of the specified length (`max_len`)."""
    soup = BeautifulSoup(source, 'html.parser')
    current_fragment = ""
    
    for tag in soup.recursiveChildGenerator():
        if len(current_fragment) + len(str(tag)) > max_len:
            yield current_fragment
            current_fragment = ""
        
        current_fragment += str(tag)
    
    if current_fragment:
        yield current_fragment

#click
@click.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.option('--max-len', type=int, default=MAX_LEN, help='Maximum length of each fragment.')
def split_html(filepath, max_len):
    """Split an HTML file into fragments."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    for i, fragment in enumerate(split_message(content, max_len)):
        print(f"-- {Fore.GREEN}fragment #{i + 1}{Style.RESET_ALL}:{Fore.BLUE} {len(fragment)} chars!{Style.RESET_ALL} --")
        print(f"{Fore.LIGHTMAGENTA_EX}{fragment}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    colorama_init()
    split_html()