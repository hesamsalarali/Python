

print("=== بخش اول: دستور if ===")
number = int(input("یک عدد وارد کنید: "))

if number > 0:
    print("عدد مثبت است.")
elif number < 0:
    print("عدد منفی است.")
else:
    print("عدد صفر است.")


print("\n=== بخش دوم: حلقه for ===")

for i in range(1, 6):
    print(i)


names = ["علی", "رضا", "مریم"]
for name in names:
    print("سلام", name)


print("\n=== بخش سوم: حلقه while ===")

counter = 1
while counter <= 5:
    print(counter)
    counter += 1

password = ""
while password != "1234":
    password = input("رمز را وارد کنید: ")

print("رمز صحیح است. خوش آمدید!")


print("\n=== پایان برنامه ===")
