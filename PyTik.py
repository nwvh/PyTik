import requests # << This Library will help tikvid to download the video
import tikvid   # << This is the main library used to get tiktok's video data
import pystyle  # << This is library used for styling
import random   # << This will be used to generate random file names
import os       # << We will use this library to execute commands
from sys import platform # << This library is used to detect operating system for the clear() function

from pystyle import Colors, Colorate, Write, Center 

def clear():
    if platform == "linux" or platform == "posix" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

clear()
banner = """
╔═╗┬ ┬  ╔╦╗ ┬ ┬┌─     github.com/nwvh
╠═╝└┬┘   ║  │ ├┴┐     github.com/nwvh
╩   ┴    ╩  ┴ ┴ ┴     github.com/nwvh

"""

#print(Colorate.Horizontal(Colors.blue_to_red, banner, 1))
#writing = Write.Print(f"{banner}", Colors.red_to_purple, interval=0)
print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(banner), 1))


link = Write.Input("Video Link >> ", Colors.red_to_purple, interval=0.040)
if link is None or link == "":
    clear()
    errortext = """
╔═╗╦═╗╦═╗╔═╗╦═╗
║╣ ╠╦╝╠╦╝║ ║╠╦╝
╚═╝╩╚═╩╚═╚═╝╩╚═
No video link was specified.

    """
    print(Colorate.Horizontal(Colors.red_to_purple, errortext, 1))
    exit()

video_id = tikvid.parseLink(link)

clear()
downtext = """
╔╦╗  ┌─┐  ┬ ┬  ┌┐┌  ┬    ┌─┐  ┌─┐  ┌┬┐  ┬  ┌┐┌  ┌─┐   
 ║║  │ │  │││  │││  │    │ │  ├─┤   ││  │  │││  │ ┬   
═╩╝  └─┘  └┴┘  ┘└┘  ┴─┘  └─┘  ┴ ┴  ─┴┘  ┴  ┘└┘  └─┘ooo
"""
print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(downtext), 1))

download_link = tikvid.downloadLink(video_id)
vidcont = requests.get(download_link)

randomname = random.randint(0,99999999)
with open(f"PyTik_{randomname}.mp4","wb") as f:
    f.write(vidcont.content)
clear()
successtext = f"""
╔═╗┬ ┬┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┬ ┬┬  ┬ ┬ ┬  ╔╦╗┌─┐┬ ┬┌┐┌┬  ┌─┐┌─┐┌┬┐┌─┐┌┬┐
╚═╗│ ││  │  ├┤ └─┐└─┐├┤ │ ││  │ └┬┘   ║║│ ││││││││  │ │├─┤ ││├┤  ││
╚═╝└─┘└─┘└─┘└─┘└─┘└─┘└  └─┘┴─┘┴─┘┴   ═╩╝└─┘└┴┘┘└┘┴─┘└─┘┴ ┴─┴┘└─┘─┴┘

            File has been saved as PyTik_{randomname}.mp4
"""
print(Colorate.Horizontal(Colors.blue_to_red, Center.XCenter(successtext), 1))
