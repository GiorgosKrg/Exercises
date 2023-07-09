total_cargo = 0
max = 0
s = 0
loops = 0
days_over_10 = 0
sum_in = 0

while True:
    cargo_in = int(input('Give cargo input: '))
    cargo_out = int(input('Give cargo output: '))
    if cargo_in-cargo_out<0 or cargo_in-cargo_out>170:
        continue
    total_cargo = total_cargo+(cargo_in-cargo_out)
    sum_in = cargo_in + sum_in
    s = cargo_in + cargo_out
    if max<cargo_in:
        max = cargo_in
    if total_cargo >= 10:
        days_over_10 = days_over_10 + 1
    loops +=1
    ans = input('Any more data to give? : ').lower()
    print(ans)
    if ans == "no":
        break


print('Max number of loaded cargo in a day: ', max)
print('Days with 10+ cargo loaded: ', days_over_10)
print('Average loaded cargo per day: ', sum_in/loops)

