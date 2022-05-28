# 55
USD_to_GBP = 0.79
USD_to_EUR = 0.93
USD_to_JPY = 126.77

GBP_sign = "\u00A3"
EUR_sign = "\u20AC"
JPY_sign = "\u00A5"

dollars = 1000

pounds = dollars * USD_to_GBP
euros = dollars * USD_to_EUR
yen = dollars * USD_to_JPY

print(f"Today, ${dollars}")
print(f"converts to {GBP_sign}{pounds}")
print(f"converts to {EUR_sign}{euros}")
print(f"converts to {JPY_sign}{yen}")
print()

# 56
USD_to_GBP = 0.79
USD_to_EUR = 0.93
USD_to_JPY = 126.77
USD_to_KOR = 1265.5

GBP_sign = "\u00A3"
EUR_sign = "\u20AC"
JPY_sign = "\u00A5"
KOR_sign = "\u20A9"

dollars = 1000

pounds = dollars * USD_to_GBP
euros = dollars * USD_to_EUR
yen = dollars * USD_to_JPY
won = dollars * USD_to_KOR

print(f"Today, ${dollars}")
print(f"converts to {GBP_sign}{pounds}")
print(f"converts to {EUR_sign}{euros}")
print(f"converts to {JPY_sign}{yen}")
print(f"converts to {KOR_sign}{won}")
print()

# 57
USD_to_GBP = 0.79
USD_to_EUR = 0.93
USD_to_JPY = 126.77
USD_to_KOR = 1265.5

dollars = 1000

pounds = dollars * USD_to_GBP
euros = dollars * USD_to_EUR
yen = dollars * USD_to_JPY
won = dollars * USD_to_KOR

print(f"Today, ${dollars}")
print(f"converts to £{pounds}")
print(f"converts to €{euros}")
print(f"converts to ¥{yen}")
print(f"converts to ₩{won}")
print()

# 59
b = 12345678

kb = b / 1024
mb = kb / 1024
gb = mb / 1024

print(f"Bytes = {b}")
print(f"KiloBytes = {kb}")
print(f"MegaBytes = {mb}")
print(f"GigaBytes = {gb}")
print()

# 60
sec_per_music = 180
stereo_size = 180 * 44100 * 32
print(f"Stereo Size = {stereo_size}bits")
