
with open('input.txt', 'r') as f:
    data = f.read().split('\n\n')
new_item=[]
for item in data:
    sub_item = item.split('\n')
    new_item.append(sum([int(x) for x in sub_item]))

new_item.sort()
print(f"total: {new_item[-1]}")
total_2 = sum(new_item[-3:])
print(f"top 3 total: {total_2}")