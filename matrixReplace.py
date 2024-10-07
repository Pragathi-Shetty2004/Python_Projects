#replace the given ro-column with X
row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
list=[row1,row2,row3]
print(f"{list[0]}\n{list[1]}\n{list[2]}")
i=input('Enter row and column')
#32
row=int(i[0])-1
column=int(i[1])-1
list[row][column]=0
print(f"{list[0]}\n{list[1]}\n{list[2]}")


