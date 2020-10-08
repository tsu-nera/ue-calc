import pandas as pd

file_path = './data/sample.csv'

df = pd.read_csv(file_path, index_col='乗車 ID')

df = df.drop(
    ["ドライバーの名前", "電話番号", "メール アドレス", "種類", "日付 / 時刻", "保証金"],
    axis=1).fillna("0").applymap(lambda x: int(float(str(x).replace(",", ""))))

df_sum = df.sum()
# print(df_sum)

tips = df_sum["チップ"]

# 売上
sales = df_sum[["料金", "ピーク", "ブースト"]].sum()
# サービス手数料
fee = abs(df_sum["Uber 手数料 Jct を含む"])
# 現金
cash = 28648
# 不明な調整
adjust = 2

# 売掛金
expected_receivable = 11488
receivable = tips + sales - fee - cash - adjust

# print()
# print(tips, sales, fee)
# print()
print("売り上げ:￥{}".format(sales))
print("集められた現金:￥{}".format(-cash))
print("支払い:￥{}".format(receivable))

print()

# print("売掛金:{}, 売掛金(期待値):{}".format(receivable, expected_receivable))
# print()
assert expected_receivable == receivable, "売掛金検算エラー"

print("売掛金:{}, 雑収入:{}".format(tips, tips))
print("支払手数料:{}, 普通預金:{}".format(fee, fee))
print("売掛金:{}, 現金:{}, 売上高:{}".format(receivable, cash, sales))

print("普通預金:{}, 売掛金:{}".format(receivable, receivable))
