import os, requests, json, sys

def get_latest_version():
    try:
        response = requests.get('https://api.github.com/repos/YureiNox/YureiMultitool/releases/latest')
        response.raise_for_status()
        return response.json()['tag_name']
    except Exception as e:
        print('Failed to check for updates:', e)
        return None