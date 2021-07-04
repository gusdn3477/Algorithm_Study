def check(cache, name):
    for i in range(len(cache)):
        if cache[i][0] == name:
            return True
    return False

def returnIdx(cache, name):
    for i in range(len(cache)):
        if cache[i][0] == name:
            return i

def solution(cacheSize, cities):
    answer = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache = []
    for i in cities:
        if cache:
            for j in range(len(cache)):
                cache[j][1] += 1
        flag = check(cache, i)
        if flag == True:
            answer += 1
            k = returnIdx(cache, i)
            cache[k][1] = 0
        else:
            answer += 5
            if cacheSize == 0:
                continue
            if len(cache) < cacheSize:
                cache.append([i,0])
            else:
                cache.sort(key = lambda x : x[1])
                cache.pop()
                cache.append([i,0])
    return answer