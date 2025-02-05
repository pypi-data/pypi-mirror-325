import click
from .deploy import push_directory, run_directory
from .simplex import Simplex
import os
from dotenv import load_dotenv
import webbrowser
from colorama import init, Fore, Style
import time
import sys

init()  # Initialize colorama

load_dotenv()

def animated_print(message, color=Fore.CYAN):
    """Print with animated ellipsis"""
    for i in range(3):
        sys.stdout.write(f'\r{color}{message}{"." * (i+1)}{" " * (2-i)}{Style.RESET_ALL}')
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\n')

@click.group()
def cli():
    """Simplex CLI tool"""
    pass

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))  
def push(directory):
    try:
        push_directory(directory)
    except Exception as e:
        print(f"{Fore.RED}[SIMPLEX] Error running job: {e}{Style.RESET_ALL}")
        raise
    
    

@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def run(directory):
    try:
        run_directory(directory)
    except Exception as e:
        print(f"{Fore.RED}[SIMPLEX] Error running job: {e}{Style.RESET_ALL}")
        raise

@cli.command()
@click.argument('website')
def login(website):
    """Capture login session for a website"""
    try:
        # Initialize Simplex with API key from environment
        api_key = os.getenv("SIMPLEX_API_KEY")
        if not api_key:
            raise click.ClickException("SIMPLEX_API_KEY environment variable not set")
        
        simplex = Simplex(api_key)
        
        # Ensure website has proper URL format
        if not website.startswith(('http://', 'https://')):
            website = 'https://' + website
            
        animated_print(f"[SIMPLEX] Creating login session for {website}")
        result = simplex.create_login_session(website)
        
        if result.get('succeeded'):
            # Open the login URL in a new browser tab
            login_url = result.get('login_session_url')
            if login_url:
                animated_print("[SIMPLEX] Opening login page in your browser")
                webbrowser.open_new_tab(login_url)
            else:
                print(f"{Fore.YELLOW}[SIMPLEX] Warning: No login URL returned from the server{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[SIMPLEX] Failed to capture login session: {result.get('error', 'Unknown error')}{Style.RESET_ALL}")
    except Exception as e:
        raise click.ClickException(str(e))
    finally:
        print(f"{Fore.GREEN}[SIMPLEX] Login session closed.{Style.RESET_ALL}")

def main():
    cli() 