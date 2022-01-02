import pyupbit

access = "ZI0OtgTyQ1ZiQoxosxZ77OPx9k6xm5P3ONlKu4x1"          # 본인 값으로 변경
secret = "saASaDgULz5ZTohR0pNclQgOa1JC6E1PNHVxlW4O"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회