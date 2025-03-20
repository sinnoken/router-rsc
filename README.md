# router-rsc
將 IP 清單轉換為 RouterOS 新增 IP 清單指令

要使用 GitHub Actions 將一個 IP 清單文字檔轉換成 RouterOS 的新增 IP 清單指令，你可以按照以下步驟進行：

建立 GitHub 儲存庫：

如果你還沒有專案，先在 GitHub 上建立一個新的儲存庫。
撰寫轉換腳本：

撰寫一個 Python 腳本來下載 IP 清單並轉換成 RouterOS 指令格式。
例如，使用 Python 來完成這個任務：
```
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
```
將腳本上傳到 GitHub：

將這個腳本（例如 convert_to_routeros.py）上傳到你的 GitHub 儲存庫。
設定 GitHub Actions：

在你的儲存庫中，建立一個 .github/workflows 目錄。

在這個目錄中，建立一個 YAML 檔案（例如 convert.yml）來定義 GitHub Actions 工作流程：
```
name: Convert IP List to RouterOS Commands

on:
  workflow_dispatch:  # 手動觸發工作流程

jobs:
  convert:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install requests
      run: pip install requests

    - name: Run conversion script
      run: python convert_to_routeros.py

    - name: Upload converted file
      uses: actions/upload-artifact@v2
      with:
        name: routeros-commands
        path: routeros_commands.txt
```
執行工作流程：

這個工作流程設定為手動觸發（workflow_dispatch），你可以在 GitHub Actions 頁面手動啟動它。
轉換後的 RouterOS 指令檔案會作為 artifact 上傳，你可以從 GitHub Actions 的執行結果頁面下載。
這樣，你就可以自動化地將 IP 清單轉換成 RouterOS 的新增 IP 清單指令。記得根據你的實際需求調整腳本和工作流程設定。
