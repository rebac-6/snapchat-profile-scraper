thonimport json
from extractors.snapchat_parser import parse_snapchat_profile
from outputs.exporter import export_data
from config.settings import load_settings

def run_scraper(usernames):
    settings = load_settings()
    data = []
    
    for username in usernames:
        profile_data = parse_snapchat_profile(username, settings)
        data.append(profile_data)
    
    export_data(data, settings)

if __name__ == "__main__":
    usernames = ["bobbysolez", "johndoe", "janedoe"]
    run_scraper(usernames)