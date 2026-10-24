marks=[88,45,92,67,30,75]
count=0
for mark in marks:
    if mark>=50:
        count+=1

Average=sum(marks)/len(marks)
highest=max(marks)
lowest=min(marks)
print("Passed:",count)
print(f"Average:{Average:.1f}")
print("Highest:",highest)
print("Lowest:",lowest)
