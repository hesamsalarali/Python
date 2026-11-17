# آموزش ساختارهای شرطی و حلقه‌ها در پایتون
# شامل: if / elif / else ، حلقه for و حلقه while

print("=== بخش اول: دستور if ===")

# مثال 1: بررسی مثبت، منفی یا صفر بودن عدد
number = int(input("یک عدد وارد کنید: "))

if number > 0:
    print("عدد مثبت است.")
elif number < 0:
    print("عدد منفی است.")
else:
    print("عدد صفر است.")


print("\n=== بخش دوم: حلقه for ===")

# مثال 2: چاپ اعداد 1 تا 5
for i in range(1, 6):
    print(i)

# مثال 3: پیمایش اعضای یک لیست
names = ["علی", "رضا", "مریم"]
for name in names:
    print("سلام", name)


print("\n=== بخش سوم: حلقه while ===")

# مثال 4: شمارش از 1 تا 5
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# مثال 5: تکرار تا زمانی که رمز درست وارد شود
password = ""
while password != "1234":
    password = input("رمز را وارد کنید: ")

print("رمز صحیح است. خوش آمدید!")


print("\n=== پایان برنامه ===")
