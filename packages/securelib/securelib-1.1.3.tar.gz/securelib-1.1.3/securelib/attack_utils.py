import requests

def load_wordlist_from_file(file_path):
    with open(file_path, 'r') as file:
        wordlist_from_file = [line.strip() for line in file.readlines()]
    return wordlist_from_file

def directory_bruteforce(url: str, wordlist: list, file_path: str) -> list:
    # txtファイルからワードリストを読み込んで既存のリストに結合
    file_wordlist = load_wordlist_from_file(file_path)
    full_wordlist = wordlist + file_wordlist  # 既存のリストと結合
    
    found_paths = []
    for word in full_wordlist:
        target_url = f"{url}/{word}"
        response = requests.get(target_url)
        if response.status_code == 200:
            found_paths.append(target_url)
    
    return found_paths
