import os
import shutil
import m3u8_To_MP4
import requests
from colorama import Fore, init

init(autoreset=False)
headers = {'Mobile-Agent': 'Mobile-Android',
            'User-Agent': 'Mobile-Android',
           'X-Access-Token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6NTk2MDc5NjcsIm9yZ0lkIjoxMTgzMiwidHlwZSI6MSwibW9iaWxlIjoiOTE2MjM5OTA3NzQwIiwibmFtZSI6IkdhdXJhdiBWZXJtYSIsImVtYWlsIjoiZ2F1cmF2dmVybWE2NDc4NkBnbWFpbC5jb20iLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6ZmFsc2UsImZpbmdlcnByaW50SWQiOiIzMjMwYzRlZjljNmM4MTYyZmI3NDc0OGIxNWIwYTRhMCIsImlhdCI6MTY3OTQwNjQ4OCwiZXhwIjoxNjgwMDExMjg4fQ.pH2MjvbpCRqPx5uMtLw9oKDUGfzgOSbBDLJ0kftBBQ6mxGX8ItXXGDZppLDeCIBy'}


def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        shutil.rmtree(dir_name)
        os.mkdir(dir_name)


def clean_path(path):
    return path.replace(" ", "_").replace("/", "_").replace(":", "_").replace("\\", "_").replace("?", "_").replace(
        "\"", "_").replace("<", "_").replace(">", "_").replace("|", "_")


def get_all_course(course_id):
    make_dir(os.path.join("downloads", str(course_id)))
    res = requests.get(
        f"https://api.classplusapp.com/v2/course/content/get?courseId={course_id}&limit=100&offset=0&search=",
        headers=headers)
    for folder in res.json()['data']['courseContent']:
        make_dir(os.path.join("downloads", str(course_id), clean_path(str(folder['name']))))
        temp_res = requests.get(
            f"https://api.classplusapp.com/v2/course/content/get?courseId={course_id}&folderId={folder['id']}&limit=100&offset=0&search=",
            headers=headers)
        for lecture in temp_res.json()['data']['courseContent']:
            print(lecture)
            print(Fore.GREEN, folder['name'], lecture['name'], lecture['id'])
            get_content_from_id(lecture['url'], lecture['id'],
                                os.path.join("downloads", str(course_id), clean_path(str(folder['name']))),
                                filename=clean_path(str(lecture['name'] + ".mp4")))


def get_content_from_id(content_id_url, content_id, folder, filename):
    res = requests.get(
        f"https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={content_id_url}&contentId="
        f"{content_id}&offlineDownload=true",
        headers=headers)
    ori_link = res.json()['url']
    link = get_quality(ori_link)
    link = "/".join(ori_link.split("/")[:-1]) + "/" + link
    m3u8_To_MP4.multithread_download(link, mp4_file_dir=folder, mp4_file_name=filename)


def get_quality(url):
    res = requests.get(url)
    quality = [x.strip() for x in res.text.split("\n") if "videos/" in x or "RESOLUTION" in x]
    for i in range(len(quality)):
        if "1280x720" in quality[i]:
            return quality[i + 1]


get_all_course(130176)
