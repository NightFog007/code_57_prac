# 第一题
# 创建一个简单的小费计算程序。该程序应该提示用户输入账单金 额和小费比例。该程序必须计算出小费，并显示小费和总金额。

# 提示用户输入账单金额和小费比例
account = input("please input account: ")
account = float(account)

per = input("please input per: ")
per = float(per)
#计算小费
res_fee = account * per / 100
# res_fee = str(res_fee)

# 显示总额
res_all = res_fee + account
print("The result of fee is : %.2f " % res_all)
