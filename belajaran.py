# Make pyramids of star with "row" level(s)
# Code to refresh my mind
# Praditya (dewantara@live.com)

inputbaris=input("masukkan berapa baris piramid: ")
row=int(inputbaris)
row=row+1

for i in range (1,row+1):
    for j in range(row-i):
        print (end=" ")

    for k in range(i,row,row-1):
        k=k*2-1
        print("*"*k)
