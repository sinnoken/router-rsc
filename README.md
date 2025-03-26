# IPsum Threat Intelligence Feed Processor

這個 Python 程式用於從 IPsum 項目中下載威脅情報資料，並生成適用於 RouterOS 的防火牆地址列表配置文件。

## 功能

- 從多個 URL 下載 IP 地址清單。
- 驗證並去重 IP 地址。
- 生成 RouterOS 防火牆地址列表的配置指令。
- 支援多線程處理以加速下載和處理過程。

## 使用方法

1. 確保已安裝 Python 3.x 和 `requests` 套件。
2. 將程式碼克隆或下載到本地。
3. 執行程式：

   ```bash
   python script_name.py

4. 生成的 .rsc 配置文件將儲存在 ./rsc/ 目錄中。

## 需求

- Python 3.x
- requests 套件

## 注意事項

- 請確保目標設備的 RouterOS 版本支援生成的配置指令。
- 根據需要調整 urls 列表以匹配不同的威脅情報等級。

## 貢獻

歡迎提交問題報告和功能請求，或通過提交 Pull Request 來貢獻代碼。
