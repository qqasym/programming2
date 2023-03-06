string = "asdASDsssSS"
cnt = 0
for i in string:
    if i.islower():
        cnt+=1

print(f"Lowercase : {cnt}")
print(f"Uppercase : {len(string) - cnt}")