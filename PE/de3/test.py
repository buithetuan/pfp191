def print_triangle(n):
    for i in range(n):
        left_part = ''.join(chr(65 + j) for j in range(i + 1))  # Tạo chuỗi tăng dần
        right_part = left_part[-2::-1]  # Tạo chuỗi giảm dần (bỏ ký tự cuối)
        full_row = left_part + right_part  # Ghép hai phần
        print(full_row.center(2 * n - 1))  # Căn giữa theo độ rộng phù hợp


if __name__ == "__main__":
    print("1. Test f1 (1 mark)")
    print("2. Test f2 (1 mark)")
    print("3. Test f3 (1 mark)")

    choice = int(input("Your selection (1 -> 3): "))
    if choice == 2:
        rows = int(input("Enter the number of rows: "))
        print("OUTPUT")
        print_triangle(rows)
        print("FINISH")

def compress_string(s):
    if not s:
        return ""

    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # Ký tự giống ký tự trước đó
            count += 1
        else:
            result.append(s[i - 1] + str(count))  # Thêm ký tự + số lần xuất hiện
            count = 1  # Reset bộ đếm

    # Thêm ký tự cuối cùng vào kết quả
    result.append(s[-1] + str(count))

    return "".join(result)

# Test
input_string = "pppppppppfffffffffpppppppppp"
output = compress_string(input_string)
print(output)  # Output: p9f9p8


def sum_of_series(n):
    total = 0
    num = 0

    for i in range(n):
        num = num * 10 + 1  # Tạo số dạng 1, 11, 111, 1111, ...
        total += num

    return total

# Nhập từ người dùng
n = int(input("Enter number of terms: "))
print("Sum of series:", sum_of_series(n))