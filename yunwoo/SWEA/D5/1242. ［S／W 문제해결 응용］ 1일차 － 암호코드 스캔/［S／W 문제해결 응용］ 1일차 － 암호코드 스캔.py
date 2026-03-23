
hex_to_bin = {
    '0':'0000','1':'0001','2':'0010','3':'0011',
    '4':'0100','5':'0101','6':'0110','7':'0111',
    '8':'1000','9':'1001','A':'1010','B':'1011',
    'C':'1100','D':'1101','E':'1110','F':'1111'
}

secret = {
    (2,1,1):0, (2,2,1):1, (1,2,2):2, (4,1,1):3,
    (1,3,2):4, (2,3,1):5, (1,1,4):6, (3,1,2):7,
    (2,1,3):8, (1,1,2):9
}

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    maze = [input().strip() for _ in range(n)]

    visited = set()
    result = 0
    for row in maze:
        if set(row) == {'0'}:
            continue
        binary = ''.join(hex_to_bin[ch] for ch in row)
        idx = len(binary) - 1

        while idx >= 55:

            if binary[idx] == '1':

                numbers = []

                for _ in range(8):

                    c = b = a = 0

                    while idx >= 0 and binary[idx] == '1':
                        c += 1
                        idx -= 1
                    while idx >= 0 and binary[idx] == '0':
                        b += 1
                        idx -= 1
                    while idx >= 0 and binary[idx] == '1':
                        a += 1
                        idx -= 1

                    if a == 0 or b == 0 or c == 0:
                        break

                    div = min(a, b, c)
                    ratio = (a//div, b//div, c//div)

                    if ratio not in secret:
                        break

                    numbers.append(secret[ratio])

                    while idx >= 0 and binary[idx] == '0':
                        idx -= 1

                if len(numbers) == 8:
                    numbers.reverse()
                    code = tuple(numbers)

                    if code not in visited:
                        visited.add(code)

                        odd = sum(numbers[i] for i in range(0,8,2))
                        even = sum(numbers[i] for i in range(1,8,2))

                        if (odd*3 + even) % 10 == 0:
                            result += sum(numbers)

            else:
                idx -= 1

    print(f'#{tc} {result}')