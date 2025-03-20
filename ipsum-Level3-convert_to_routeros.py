import requests

# 下載 IP 清單
url = 'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/3.txt'
#
comment = 'IPsum-Threat-Intelligence-Feed'
#
list    = 'HN-BLACKLIST-IPSUM-L3'

response = requests.get(url)
ip_list = response.text.splitlines()

# 轉換成 RouterOS 指令
output_file = 'rsc/ipsum-Level3.rsc'
with open(output_file, 'w') as f:
    for line in ip_list:
        # 跳過註解行
        if line.startswith('#') or not line.strip():
            continue
        ip_address = line.split()[0]  # 假設 IP 位址在每行的第一個位置
        f.write(f'/ip firewall address-list add address={ip_address} comment={comment} list={list}\n')
