# GeoIP Country Counter

這是一個使用 GeoLite2 資料庫來查詢 IP 位址的來源國家並統計每個國家出現次數的 Python 程式。

## 安裝

1. Clone repo：
    ```bash
    git clone <repository-url>
    cd geoip-country-counter
    ```

2. 安裝所需的 Python Library：
    ```bash
    pip install geoip2
    ```

3. 下載 [GeoLite2-City](https://dev.maxmind.com/geoip/geoip2/geolite2/) 資料庫，並將其放置於指定路徑。

## 使用方法

1. 將你需要查詢的 IP 位址列表放入 `ip.txt` 文件中，每行一個 IP 位址。
2. 修改 `geoip_counter.py` 中的 `ip_file_path` 和 `db_path` 變數，確保它們指向正確的文件路徑。
3. 運行程式：
    ```bash
    python geoip_counter.py
    ```

## 注意事項

- 確保 `ip.txt` 文件和 `GeoLite2-City.mmdb` 文件位於正確的路徑。
- 若有大量 IP 位址需要查詢，建議分批處理，以避免超時或資源不足。

## 貢獻

歡迎提交 Pull Request 來改進這個專案。如有任何問題，請提出 Issue。
