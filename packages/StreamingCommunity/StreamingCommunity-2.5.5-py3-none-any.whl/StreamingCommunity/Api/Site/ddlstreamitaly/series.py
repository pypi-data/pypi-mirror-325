# 13.06.24

import os
import sys
from urllib.parse import urlparse


# Internal utilities
from StreamingCommunity.Util.console import console
from StreamingCommunity.Util.message import start_message
from StreamingCommunity.Util.os import os_manager
from StreamingCommunity.Util.table import TVShowManager
from StreamingCommunity.Lib.Downloader import MP4_downloader


# Logic class
from StreamingCommunity.Api.Template.Class.SearchType import MediaItem
from StreamingCommunity.Api.Template.Util import manage_selection, map_episode_title, validate_episode_selection


# Player
from .util.ScrapeSerie import GetSerieInfo
from StreamingCommunity.Api.Player.ddl import VideoSource


# Variable
from .costant import SERIES_FOLDER



def download_video(index_episode_selected: int, scape_info_serie: GetSerieInfo, video_source: VideoSource) -> tuple[str,bool]:
    """
    Download a single episode video.

    Parameters:
        - tv_name (str): Name of the TV series.
        - index_episode_selected (int): Index of the selected episode.

    Return:
        - str: output path
        - bool: kill handler status
    """
    start_message()

    # Get info about episode
    obj_episode = scape_info_serie.list_episodes[index_episode_selected - 1]
    console.print(f"[yellow]Download: [red]{obj_episode.get('name')}\n")
    console.print(f"[cyan]You can safely stop the download with [bold]Ctrl+c[bold] [cyan] \n")

    # Define filename and path for the downloaded video
    title_name = os_manager.get_sanitize_file(
        f"{map_episode_title(scape_info_serie.tv_name, None, index_episode_selected, obj_episode.get('name'))}.mp4"
    )
    mp4_path = os.path.join(SERIES_FOLDER, scape_info_serie.tv_name)

    # Create output folder
    os_manager.create_path(mp4_path)

    # Setup video source
    video_source.setup(obj_episode.get('url'))

    # Get m3u8 master playlist
    master_playlist = video_source.get_playlist()
    
    # Parse start page url
    parsed_url = urlparse(obj_episode.get('url'))

    # Start download
    r_proc = MP4_downloader(
        url=master_playlist, 
        path=os.path.join(mp4_path, title_name),
        referer=f"{parsed_url.scheme}://{parsed_url.netloc}/",
    )
    
    if r_proc != None:
        console.print("[green]Result: ")
        console.print(r_proc)

    return os.path.join(mp4_path, title_name)


def download_thread(dict_serie: MediaItem):
    """
    Download all episode of a thread
    """

    # Start message and set up video source
    start_message()

    # Init class
    scape_info_serie = GetSerieInfo(dict_serie)
    video_source = VideoSource()

    # Collect information about thread
    list_dict_episode = scape_info_serie.get_episode_number()
    episodes_count = len(list_dict_episode)

    # Display episodes list and manage user selection
    last_command = display_episodes_list(scape_info_serie.list_episodes)
    list_episode_select = manage_selection(last_command, episodes_count)

    try:
        list_episode_select = validate_episode_selection(list_episode_select, episodes_count)
    except ValueError as e:
        console.print(f"[red]{str(e)}")
        return

    # Download selected episodes
    kill_handler = bool(False)
    for i_episode in list_episode_select:
        if kill_handler:
            break
        kill_handler = download_video(i_episode, scape_info_serie, video_source)[1]


def display_episodes_list(obj_episode_manager) -> str:
    """
    Display episodes list and handle user input.

    Returns:
        last_command (str): Last command entered by the user.
    """

    # Set up table for displaying episodes
    table_show_manager = TVShowManager()
    table_show_manager.set_slice_end(10)

    # Add columns to the table
    column_info = {
        "Index": {'color': 'red'},
        "Name": {'color': 'magenta'},
    }
    table_show_manager.add_column(column_info)

    # Populate the table with episodes information
    for i, media in enumerate(obj_episode_manager):
        table_show_manager.add_tv_show({
            'Index': str(i+1),
            'Name': media.get('name'),
        })

    # Run the table and handle user input
    last_command = table_show_manager.run()

    if last_command == "q":
        console.print("\n[red]Quit [white]...")
        sys.exit(0)

    return last_command
