import requests

# 下載 IP 清單
url = 'https://github.com/stamparm/ipsum/raw/refs/heads/master/levels/3.txt'
response = requests.get(url)
ip_list = response.text.splitlines()

# 轉換成 RouterOS 指令
output_file = 'routeros_commands.txt'
with open(output_file, 'w') as f:
    for line in ip_list:
        # 跳過註解行
        if line.startswith('#') or not line.strip():
            continue
        ip_address = line.split()[0]  # 假設 IP 位址在每行的第一個位置
        f.write(f'/ip firewall address-list add list=drop_traffic address={ip_address}/32\n')