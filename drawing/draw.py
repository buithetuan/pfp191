h = int(input("Enter number of rows (h): "))

# 1) Full Pyramid of *
# Ví dụ (h = 5):
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
print("\n1) Full pyramid of * (centered, odd counts)")
# Mỗi hàng có số sao lẻ: 1,3,5,...; dùng unit_width để căn giữa chính xác
unit = '* '
unit_width = len(unit)  # 2
for i in range(1, h + 1):
    stars = (2 * i - 1)
    line = unit * stars
    # left padding: (h-i) units
    padding = ' ' * ((h - i) * unit_width)
    print(padding + line.rstrip())

# 1b) Full Pyramid of *
print("\n1. Full Pyramid of *")
for i in range(1, h + 1):
    print(" " * (h - i) + "* " * i)

print("\n1b) Full pyramid of * (inverted)")
for i in range(h,0,-1):
    print(" " * (h - i) + "* " * i)
for i in range(2, h + 1):
    print(" " * (h - i) + "* " * i)

# 1c) Full pyramid (increasing counts, centered)
print("\n1c) Full pyramid (increasing counts, centered)")
for i in range(1, h + 1):
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * i).rstrip())


# 2) Inverted full pyramid of *
print("\n2) Inverted full pyramid of * (variant A, simple)")
for i in range(h, 0, -1):
    # variant A: using i stars per row (mirrors earlier half-pyramid style centered)
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * i).rstrip())

print("\n2b) Inverted full pyramid of * (variant B, odd-star counts)")
for i in range(h, 0, -1):
    padding = ' ' * ((h - i) * unit_width)
    stars = 2 * i - 1
    print(padding + (unit * stars).rstrip())

print("\n2c) Inverted full pyramid (increasing counts centered)")
for i in range(h, 0, -1):
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * i).rstrip())

# 3) Half pyramid of *
# Ví dụ (h = 5):
"""
*
* *
* * *
* * * *
* * * * *
"""
print("\n3) Half pyramid of *")
for i in range(1, h + 1):
    print('* ' * i)

# 4) Inverted half pyramid of *
print("\n4) Inverted half pyramid of *")
for i in range(h, 0, -1):
    print('* ' * i)

# 5) Full pyramid of numbers
# Ví dụ (h = 5):
"""
1
2 3 2
3 4 5 4 3
4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""
print("\n5) Full pyramid of numbers (centered)")
# Tạo chuỗi cho từng hàng rồi căn giữa theo chiều rộng hàng dưới cùng
max_num = 2 * h - 1
cell_w = len(str(max_num))
bottom = [str(num).rjust(cell_w) for num in list(range(h, h + h)) + list(range(h + h - 2, h - 1, -1))]
total_width = len(' '.join(bottom))
for i in range(1, h + 1):
    nums = list(range(i, i + i)) + list(range(i + i - 2, i - 1, -1))
    row = ' '.join(str(n).rjust(cell_w) for n in nums)
    print(row.center(total_width))

# 6) Half pyramid of numbers
print("\n6) Half pyramid of numbers")
for i in range(1, h + 1):
    print(' '.join(str(j) for j in range(1, i + 1)))

# 7) Inverted half pyramid of numbers
print("\n7) Inverted half pyramid of numbers")
for i in range(h, 0, -1):
    print(' '.join(str(j) for j in range(1, i + 1)))

# 8) Pascal's Triangle
# Mỗi số là tổ hợp chập k của hàng i
print("\n8) Pascal's Triangle")
for i in range(h):
    row = []
    val = 1
    for k in range(i + 1):
        if k == 0:
            val = 1
        else:
            val = val * (i - k + 1) // k
        row.append(str(val))
    print(' ' * (h - i) + ' '.join(row))

# 9) Floyd's Triangle
print("\n9) Floyd's Triangle")
num = 1
for i in range(1, h + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    print(' '.join(row))

# 10) Unfilled (hollow) pyramid of *
# Viền ngoài là sao, phần trong là khoảng trắng
print("\n10) Unfilled (hollow) pyramid of * (centered odd counts)")
for i in range(1, h + 1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    if i == 1:
        print(padding + '*')
    elif i == h:
        print((unit * (2 * h - 1)).rstrip())
    else:
        # tạo mảng length stars, chỉ hai đầu là '*', giữa là ' '
        items = ['*'] + [' ' for _ in range(stars - 2)] + ['*']
        print(padding + ' '.join(items))

# 11) Unfilled half pyramid of * (hollow half pyramid)
print("\n11) Unfilled half pyramid of *")
for i in range(1, h + 1):
    if i == 1:
        print('*')
    elif i == h:
        print('*' * h)
    else:
        print('*' + ' ' * (i - 2) + '*')

# 12) Inverted unfilled pyramid of *
print("\n12) Inverted unfilled pyramid of * (centered odd counts)")
for i in range(h, 0, -1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    if i == h:
        print((unit * (2 * h - 1)).rstrip())
    elif i == 1:
        print(padding + '*')
    else:
        items = ['*'] + [' ' for _ in range(stars - 2)] + ['*']
        print(padding + ' '.join(items))

# Diamond (hình kim cương) - độ cao tổng là 2*h-1
print("\nDiamond shape (filled, centered odd counts)")
for i in range(1, h + 1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * stars).rstrip())
for i in range(h - 1, 0, -1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * stars).rstrip())

print("\nDiamond")
for i in range(h, 0, -1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * stars).rstrip())
for i in range(2, h + 1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    print(padding + (unit * stars).rstrip())

# -------------------------
# Các biến thể bổ sung để "đa dạng hơn các trường hợp"
# Mục đích: cho sinh viên thấy nhiều cách hiển thị (tight/compact, left-aligned, hollow diamond,...)
# -------------------------
print("\n--- Variants: additional styles for diversity ---")

# Variant 1: Full pyramid (tight) - không có dấu cách giữa các sao
print("\nVariant 1: Full pyramid (tight, no inner spaces)")
for i in range(1, h + 1):
    padding = ' ' * (h - i)
    print(padding + '*' * (2 * i - 1))

# Variant 2: Full pyramid (compact single-space) - mỗi sao cách nhau 1 space, nhưng padding tính bằng 1 char
print("\nVariant 2: Full pyramid (compact single-space)")
for i in range(1, h + 1):
    stars = ' '.join(['*'] * (2 * i - 1))
    padding = ' ' * (h - i)
    print(padding + stars)

# Variant 3: Left-aligned pyramid (just for variety)
print("\nVariant 3: Left-aligned full pyramid")
for i in range(1, h + 1):
    print('*' * (2 * i - 1))

# Variant 4: Inverted tight (no inner spaces)
print("\nVariant 4: Inverted tight pyramid")
for i in range(h, 0, -1):
    padding = ' ' * (h - i)
    print(padding + '*' * (2 * i - 1))

# Variant 5: Number pyramid (alternate style) - 1..i..1 pattern centered
print("\nVariant 5: Number pyramid (1..i..1 centered)")
max_w = len(' '.join(str(x) for x in list(range(h)) + list(range(h-1, -1, -1))))
for i in range(1, h + 1):
    asc = [str(x) for x in range(1, i + 1)]
    desc = [str(x) for x in range(i - 1, 0, -1)]
    row = ' '.join(asc + desc)
    print(row.center(max_w))

# Variant 6: Hollow diamond (unfilled diamond) - giống hình 7/combined shapes
print("\nVariant 6: Hollow diamond (unfilled)")
for i in range(1, h + 1):
    stars = 2 * i - 1
    padding = ' ' * (h - i)
    if i == 1:
        print(padding + '*')
    else:
        inner = ' ' * (stars - 2)
        # ghép với 1 space giữa các ký tự để trông cân hơn
        print(padding + '*' + inner + '*')
for i in range(h - 1, 0, -1):
    stars = 2 * i - 1
    padding = ' ' * (h - i)
    if i == 1:
        print(padding + '*')
    else:
        inner = ' ' * (stars - 2)
        print(padding + '*' + inner + '*')

# Variant 7: Hollow diamond with spaced stars (visual closer to attachment)
print("\nVariant 7: Hollow diamond (spaced stars)")
for i in range(1, h + 1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    if i == 1:
        print(padding + '*')
    else:
        # create spaced interior: put single spaces between outer stars
        inner = ' ' * ((stars - 2) * unit_width)
        print(padding + '*' + inner + ' *')
for i in range(h - 1, 0, -1):
    stars = 2 * i - 1
    padding = ' ' * ((h - i) * unit_width)
    if i == 1:
        print(padding + '*')
    else:
        inner = ' ' * ((stars - 2) * unit_width)
        print(padding + '*' + inner + ' *')

print("\n--- End of additional variants ---")

# -------------------------
# Tiếp: thêm nhiều biến thể nữa để đa dạng tình huống (theo yêu cầu)
# - Butterfly (2 tam giác đối xứng)
# - Numeric diamond (số tăng rồi giảm, căn giữa)
# - Hourglass (đồng dạng kim cương đảo)
# - Inverted hollow half pyramid
# - Framed rectangle (ký tự khác)
# - Right-shifted/offset pyramid
# -------------------------
print("\n--- More variants (butterfly / numeric diamond / hourglass / inverted hollow half / framed rectangle / right-shifted) ---")

# Butterfly: hai half-pyramid đối xứng (top -> bottom)
print("\nButterfly pattern")
for i in range(1, h + 1):
    left = '* ' * i
    mid = '  ' * (h - i)
    right = '* ' * i
    print(left + mid + right)
for i in range(h, 0, -1):
    left = '* ' * i
    mid = '  ' * (h - i)
    right = '* ' * i
    print(left + mid + right)

# Numeric diamond: 1..i..1 with numbers increasing per row, căn giữa
print("\nNumeric diamond")
max_w = len(' '.join(str(x) for x in list(range(1, h + 1)) + list(range(h - 1, 0, -1))))
for i in range(1, h + 1):
    asc = [str(x) for x in range(1, i + 1)]
    desc = [str(x) for x in range(i - 1, 0, -1)]
    row = ' '.join(asc + desc)
    print(row.center(max_w))
for i in range(h - 1, 0, -1):
    asc = [str(x) for x in range(1, i + 1)]
    desc = [str(x) for x in range(i - 1, 0, -1)]
    row = ' '.join(asc + desc)
    print(row.center(max_w))

# Hourglass (đồng dạng kim cương nhưng in ngược đầu tiên)
print("\nHourglass (filled)")
for i in range(h, 0, -1):
    padding = ' ' * ((h - i) * unit_width)
    stars = 2 * i - 1
    print(padding + (unit * stars).rstrip())
for i in range(2, h + 1):
    padding = ' ' * ((h - i) * unit_width)
    stars = 2 * i - 1
    print(padding + (unit * stars).rstrip())

# Inverted hollow half pyramid
print("\nInverted hollow half pyramid")
for i in range(h, 0, -1):
    if i == h:
        print('* ' * h)
    elif i == 1:
        print('*')
    else:
        # 1 star + spaces + final star
        inner = ' ' * (2 * i - 3)
        print('*' + inner + ' *')

# Framed rectangle with custom char (ví dụ '#')
print("\nFramed rectangle 10x5 with '#'")
fw, fh = 10, 5
for r in range(fh):
    if r == 0 or r == fh - 1:
        print('# ' * fw)
    else:
        print('# ' + '  ' * (fw - 2) + '# ')

# Right-shifted pyramid (offset to the right) - useful để minh họa căn phải
print("\nRight-shifted pyramid (offset)")
for i in range(1, h + 1):
    # offset tăng theo i để đưa đỉnh sang phải
    offset = ' ' * (i - 1)
    print(offset + '* ' * i)

print("\n--- End of more variants ---")

# II. Rectangle examples (ví dụ minh hoạ) - không yêu cầu nhập thêm
m = 7
n = 4
print(f"\nRectangle filled {m}x{n}")
for _ in range(n):
    print('* ' * m)

print(f"\nRectangle unfilled {m}x{n}")
for r in range(n):
    if r == 0 or r == n - 1:
        print('* ' * m)
    else:
        # một sao ở đầu và cuối, giữa là khoảng trắng
        print('* ' + '  ' * (m - 2) + '* ')

# III. Half pyramid of Alphabets (ký tự hoa)
print("\nHalf pyramid of Alphabets")
for i in range(0, min(h, 26)):
    ch = chr(ord('A') + i)
    # in ch i+1 lần trên hàng i (cách nhau 1 space)
    print(' '.join([ch] * (i + 1)))

print("\n-- End of patterns --")