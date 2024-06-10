from youtubesearchpython import VideosSearch
from rich.console import Console

console = Console()

def __clean_results__(result_var, vid_num):
    title = result_var['result'][vid_num]['title']
    channel_name = result_var['result'][vid_num]['channel']['name']
    vid_id = result_var['result'][vid_num]['id']
    
    return {'title':title, 'channel_name':channel_name, 'vid_id':vid_id}

def run(limit_video):
    search_input= input('> ')
    videosSearch = VideosSearch(str(search_input), limit = limit_video)
    results = videosSearch.result()
    
    vid_num = 0
    for vids in results['result']:
        console.print(f"[blue bold]NO. {vid_num}#[/blue bold]")
        console.print(f"{' '*2}{__clean_results__(results, vid_num)['title']}")
        console.print(f"{' '*8}[green]└──[/green] ./{__clean_results__(results, vid_num)['channel_name']}")
        print()
        
        vid_num += 1
    
    play_vid_input = input("(Q)uit > ")
    if play_vid_input.lower() == "q":
        return None
    elif int(play_vid_input) <= len(results['result'])-1:
        info = __clean_results__(results, int(play_vid_input))
        return info
    else:
        console.print('[red bold]ERROR: must enter a valid input.')
