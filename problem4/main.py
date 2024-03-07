def muncul_sekali(angka):
    # num = int(angka)
    digits = [int(digit) for digit in str(angka)]
    jum_digit = {}
    digit_muncul_sekali = []

    for digit in digits:
        if digit in jum_digit:
            jum_digit[digit] += 1
        else:
            jum_digit[digit] = 1
    
    for digit in jum_digit:
        if jum_digit[digit] == 1:
            digit_muncul_sekali.append(digit)
    
    return digit_muncul_sekali

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]