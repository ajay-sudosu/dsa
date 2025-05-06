def zig_zag(s, k):
    if k == 1:
        return s
    pointer = 0
    mov_dir = -1
    new = [""] * k
    for i in s:
        new[pointer] += i
        if pointer ==0 or pointer == (k-1):
            mov_dir *= -1
        pointer += mov_dir
    return "".join(new)


print(zig_zag("PAYPALISHIRING", 3))
