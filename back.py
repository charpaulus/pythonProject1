import sys
stdin_fileno = sys.stdin
tmp = list(map(int, stdin_fileno.readline().split()))
n = tmp[0]
setN = set(range(1, n+1))
tmpList = set()
tmpYes = set()
tmpNo = set()
countYes = set()
for ln in stdin_fileno:
    if ln.strip() == 'HELP':
        break
    elif ln.strip() == 'YES':
        if len(countYes):
            tmpYes &= tmpList
        else:
            countYes.add('YES')
            tmpYes = tmpList
    elif ln.strip() == 'NO':
        tmpNo |= tmpList
    else:
        tmpList = set(ln.split())
    tmpNo = set(map(int, tmpNo))
    tmpYes = set(map(int, tmpYes))
if len(tmpYes):
    finishList = list(map(int, ((tmpYes - tmpNo))))
else:
    finishList = list(map(int, (setN - tmpNo)))
finishList.sort()
print(*finishList)
