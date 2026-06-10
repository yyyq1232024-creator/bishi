import re

def reg_search(text, regex_list):
    result = {}

    for item in regex_list:
        for field, pattern in item.items():
            matches = re.findall(pattern, text)

            if len(matches) == 1:
                result[field] = matches[0]
            else:
                result[field] = matches

    return [result]


text = """
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份有限公司股票
（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。

换股期限：即2023年6月2日至2027年6月1日止。
"""

regex_list = [{
    "标的证券": r"股票代码：([0-9]{6}\.[A-Z]{2})",
    "换股期限": r"(\d{4}年\d{1,2}月\d{1,2}日)"
}]

print(reg_search(text, regex_list))
