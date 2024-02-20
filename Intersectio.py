#Intersection
def inter(strArr):
    list1 = list(map(int, strArr[0].split(", ")))
    list2 = list(map(int, strArr[1].split(", ")))
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    if intersection:
        return ",".join(map(str, sorted(intersection)))
    else:
        return "false"
print(inter(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]))