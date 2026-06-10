import requests
import csv

url = "https://www.chinamoney.com.cn/english/bdInfo/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("获取数据成功")

        data = []

        with open(
            "treasury_bond_2023.csv",
            "w",
            newline="",
            encoding="utf-8-sig"
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "ISIN",
                "Bond Code",
                "Issuer",
                "Bond Type",
                "Issue Date",
                "Latest Rating"
            ])

        print("CSV导出成功")

    else:
        print("请求失败:", response.status_code)

except Exception as e:
    print("发生错误:", e)