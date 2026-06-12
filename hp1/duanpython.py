hs = []

while True:
    ten = input("Nhap ten(nhap ! de dung):")
    if ten == "!":
        break
    while True:
        dt = float(input("nhap diem toan(tu 0 - 10): "))
        if dt >= 0 and dt <= 10:
            break
    while True:
        dv = float(input("nhap diem van(tu 0 - 10): "))
        if dv >= 0 and dv <= 10:
            break
    while True:
        dta = float(input("nhap diem tieng anh(tu 0 - 10): "))
        if dta >= 0 and dta <= 10:
            break
    dtb = (dt + dv + dta) / 3
    hs.append([ten,dt,dv,dta,round(dtb,2)])

m1 = hs[0][4]

for i,v in enumerate(hs):
    print(f"Ten: {v[0]}")
    print(f"Diem toan {v[1]}")
    print(f"Diem van {v[2]}")
    print(f"Diem tieng anh {v[3]}")
    print(f"Diem trung binh {v[4]}")
    #So:.2f(lam tron toi vi tri thu 2)#
    if m1 < v[4]:
        m1 = v[4]

# hs.pop()
# hs.remove("khang")# xoa phan tu co ten la khang dau tien



hang = 1
while hs:
    m1 = hs[0][4]
    count = 0
    for v in hs:
        if v[4] > m1:
            m1 = v[4]
    for i in range(len(hs)-1,-1,-1):
        if hs[i][4] == m1:
            print(f"Hang {hang}: {hs[i][0]} diem:{hs[i][4]}")
            del hs[i]
    

        
    print("=================================")
    hang+=1

gfchcvhfc