n = int(input("Masukkan nilai n untuk angka ganjil: "))

print(f"Angka ganjil hingga {n}:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()