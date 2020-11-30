def merge(leftList, rightList):
    i = 0
    j = 0
    resultList = []
    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            resultList.append(leftList[i])
            i = i + 1
            continue
        if leftList[i] == rightList[j]:
            resultList.append(leftList[i])
            resultList.append(rightList[j])
            i = i + 1
            j = j + 1
            continue
        if leftList[i] > rightList[j]:
            resultList.append(rightList[j])
            j = j + 1
            continue
    if i < len(leftList):
        resultList = resultList + leftList[i:]
    if j < len(rightList):
        resultList = resultList + rightList[j:]
    return resultList
