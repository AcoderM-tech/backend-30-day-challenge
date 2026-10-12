from inkapsulatsiya import Seyf
seyf = Seyf("1234", 500)
print(seyf.qoldiq("1234"))
print(seyf.pul_sol(200))
print(seyf.pul_ol("1234",300))
print(seyf.qoldiq("1234"))

try:
    seyf.qoldiq("0000")
except ValueError as e:
    print(e)

try:
    seyf.qoldiq("9999")
except ValueError as e:
    print(e)

try:
    seyf.qoldiq("5555")
except ValueError as e:
    print(e)

try:
    seyf.qoldiq("1234")
except ValueError as e:
    print(e)

try:
    s2 = Seyf("123", 100)
except ValueError as e:
    print(e)

try:
    s3 = Seyf("12a4", 100)
except ValueError as e:
    print(e)

try:
    s4 = Seyf("1234", -50)
except ValueError as e:
    print(e)
