def fibo(n) :
    global cnt
    cnt += 1
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

cnt = 0             # 호출 횟수 기록
print(fibo(10), cnt)
# 10개의 피보나치수열을 호출하기 위해선 177개나 재귀호출이 일어남
