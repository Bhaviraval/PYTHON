def final_lst(lst1,i=0):
    if i==len(lst1):
        return lst1

    else:
        if lst1[i]<0:
           lst1[i]=0
        return final_lst(lst1,i+1)

lst1=[1,2,3,-2,-4,5,-1]
print(final_lst(lst1))
