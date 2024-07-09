import geoip2.database
from collections import Counter

def get_country(ip, reader):
    try:
        response = reader.city(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return None

def count_countries_from_file(file_path, db_path):
    country_counter = Counter()
    with geoip2.database.Reader(db_path) as reader:
        with open(file_path, 'r') as file:
            for line in file:
                ip = line.strip()
                if ip:  # 確保不是空行
                    country = get_country(ip, reader)
                    if country:
                        country_counter[country] += 1
    return country_counter

if __name__ == "__main__":
    # 設定 IP 位址列表文件的路徑
    ip_file_path = '/path/to/iplist.txt'

    # 設定 GeoLite2-City 資料庫的路徑
    db_path = '/path/to/GeoLite2-City.mmdb'

    country_count = count_countries_from_file(ip_file_path, db_path)
    # 按照出現次數從多到少排序
    sorted_country_count = sorted(country_count.items(), key=lambda item: item[1], reverse=True)

    for country, count in sorted_country_count:
        print(f"{country}: {count}")

