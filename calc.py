import pandas as pd

file_path = './data/sample.csv'

df = pd.read_csv(file_path, index_col='乗車 ID')

df = df.drop(
    ["ドライバーの名前", "電話番号", "メール アドレス", "種類", "日付 / 時刻", "保証金"],
    axis=1).fillna("0").applymap(lambda x: int(float(str(x).replace(",", ""))))

df_sum = df.sum()
print(df_sum)

tips = df_sum["チップ"]

# 売上
sales = df_sum[["料金", "ピーク", "ブースト"]].sum()
# サービス手数料
fee = abs(df_sum["Uber 手数料 Jct を含む"])
# 現金
cash = 30648

print()
print(tips, sales, fee)

print()

# assert fee == cash, "test"

print("売掛金:{}, 雑収入:{}".format(tips, tips))
print("支払手数料:{}, 普通預金:{}".format(fee, fee))
print("売掛金:{}, 現金:{}, 売上高:{}".format(0, cash, sales))
print("普通預金:{}, 売掛金:{}".format(0, 0))
