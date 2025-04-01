from datetime import date
date1 = (15, 1, 2025)
date2 = (19, 2, 2025) 
	

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

delta = d2 - d1
print("Number of days between dates:", delta.days)
