import os
from seo_description import * 

def yt_upload_video(filename, title, description):
    # topic = ""
    # keywords = get_top_keywords(topic)
    new_description = description.replace('"', '')
    working_directory = os.getcwd().replace('\\', '/')
    print(working_directory)
    os.system(f''' python edictai/app/upload_video.py --file="{working_directory}/videos/{filename}" --title="{title}" --description="{new_description}" --keywords="Edict.AI" --category="22" --privacyStatus="unlisted" ''')

# upload_video("news_edicted_7.mp4")