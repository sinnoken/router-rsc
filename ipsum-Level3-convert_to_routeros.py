import os
import requests
import ipaddress

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

    # 過濾並排序 IP 地址
    valid_ips = []
    for line in ip_list:
        if line.startswith('#') or not line.strip():  # 跳過註解或空行
            continue
        ip_address = line.split()[0]  # 取每行的第一個欄位作為 IP
        try:
            # 驗證 IP 地址並添加到清單
            valid_ips.append(ipaddress.ip_address(ip_address))
        except ValueError:
            continue

    # 排序 IP 地址
    valid_ips.sort()

    # 轉換並寫入 RouterOS 指令
    with open(output_file, 'w') as f:
        for ip in valid_ips:
            f.write(f'/ip firewall address-list add address={str(ip).ljust(15)} comment={comment} list={list_name}\n')

    print(f'已儲存 {output_file}')
