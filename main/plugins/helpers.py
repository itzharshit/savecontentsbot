#Github.com/Vasusen-code

from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import errors, events

import asyncio, subprocess, re, os, time
from pathlib import Path

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        hash_ = invite_link.split("+")[1]
        await client(ImportChatInviteRequest(hash_))
        return True, "✅ **This channel is now supported, Now send me post link to get that post.**"
    except errors.UserAlreadyParticipantError:
        return False, "LOL, I have already joined this channel."
    except errors.InviteHashExpiredError:
        return False, "Invite link is expired or invalid."
    except FloodWaitError:
        return False, "Flood wait error, Please report in support group!"
    
#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
#Screenshot---------------------------------------------------------------------------------------------------------------

async def screenshot(video, time_stamp, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    out = str(video).split(".")[0] + ".jpg"
    cmd = (f"ffmpeg -i {video} -ss {time_stamp} -frames:v 1 {out} -y").split(" ")
    process = await asyncio.create_subprocess_exec(
         *cmd,
         stdout=asyncio.subprocess.PIPE,
         stderr=asyncio.subprocess.PIPE)
        
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    print(x)
    print(y)
    if os.path.exists(str(Path(out))):
        return out
    else:
        None
        
