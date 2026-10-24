numbers=[4,8,15,16,23,42]
def stats(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    average=sum(numbers)/len(numbers)
    return minimum,maximum,average
result=stats(numbers)
print(result)


lo, hi , avg=result
print("lo:", lo,"hi:" ,hi,"avg:" ,avg)

def grade(marks , passing=50):
    if marks>=passing:
        return "pass"
    else:
        return "fail"
print(grade(55),grade(55,passing=60))
    