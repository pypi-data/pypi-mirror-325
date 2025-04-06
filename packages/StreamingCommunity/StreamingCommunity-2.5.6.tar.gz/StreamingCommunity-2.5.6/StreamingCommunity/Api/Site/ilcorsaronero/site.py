# 02.07.24


# Internal utilities
from StreamingCommunity.Util._jsonConfig import config_manager
from StreamingCommunity.Util.table import TVShowManager


# Logic class
from StreamingCommunity.Api.Template import get_select_title
from StreamingCommunity.Api.Template.Util import search_domain
from StreamingCommunity.Api.Template.Class.SearchType import MediaManager
from .util.ilCorsarScraper import IlCorsaroNeroScraper


# Variable
from .costant import SITE_NAME, DOMAIN_NOW
media_search_manager = MediaManager()
table_show_manager = TVShowManager()
max_timeout = config_manager.get_int("REQUESTS", "timeout")
disable_searchDomain = config_manager.get_bool("DEFAULT", "disable_searchDomain")


async def title_search(word_to_search: str) -> int:
    """
    Search for titles based on a search query.

    Parameters:
        - title_search (str): The title to search for.

    Returns:
        - int: The number of titles found.
    """
    media_search_manager.clear()
    table_show_manager.clear()

    # Find new domain if prev dont work
    domain_to_use = DOMAIN_NOW
    
    if not disable_searchDomain:
        domain_to_use, base_url = search_domain(SITE_NAME, f"https://{SITE_NAME}.{DOMAIN_NOW}")

    # Create scraper and collect result
    print("\n")
    scraper = IlCorsaroNeroScraper(f"https://{SITE_NAME}.{domain_to_use}/", 1)
    results = await scraper.search(word_to_search)

    for i, torrent in enumerate(results):
        try:
            
            media_search_manager.add_media({
                'name': torrent['name'],
                'type': torrent['type'],
                'seed': torrent['seed'],
                'leech': torrent['leech'],
                'size': torrent['size'],
                'date': torrent['date'],
                'url': torrent['url']
            })

        except Exception as e:
            print(f"Error parsing a film entry: {e}")

    # Return the number of titles found
    return media_search_manager.get_length()


def run_get_select_title():
    """
    Display a selection of titles and prompt the user to choose one.
    """
    return get_select_title(table_show_manager, media_search_manager)