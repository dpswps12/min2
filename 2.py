str1 = input("문자열 : ")

print("개별 문자 출력 : ",end="")
for i in str1:
    range(len(i))
    print(i,end="")
print("")

print("역순 개별 문자 출력 : ",end="")
for j in reversed(str1):
    print(j,end="")
