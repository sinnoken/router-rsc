import os
import requests

# 確保目錄存在
output_dir = './rsc/'
os.makedirs(output_dir, exist_ok=True)

# 設定下載的 URL 清單
urls = [
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/1.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/2.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/3.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/4.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/5.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/6.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/7.txt',
    'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/8.txt'
]

# RouterOS 設定
comment = 'IPsum-Threat-Intelligence-Feed'

for url in urls:
    level = url.split('/')[-1].split('.')[0].replace('level', '')  # 取得 Level 數字
    list_name = f'HN-BLACKLIST-IPSUM-L{level}'
    output_file = os.path.join(output_dir, f'ipsum-Level{level}.rsc')

    # 下載資料
    response = requests.get(url)
    ip_list = response.text.splitlines()

    # 轉換並寫入 RouterOS 指令
    with open(output_file, 'w') as f:
        for line in ip_list:
            if line.startswith('#') or not line.strip():  # 跳過註解或空行
                continue
            ip_address = line.split()[0]  # 取每行的第一個欄位作為 IP
            f.write(f'/ip firewall address-list add address={ip_address.ljust(15)} comment={comment} list={list_name}\n')

    print(f'已儲存 {output_file}')
