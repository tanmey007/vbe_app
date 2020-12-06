import re


def fci_util(A):
    A = A + ' '
    A = re.sub('[-]', ' ', A)
    A = A.lower()
    L = []
    a = ''
    for i in A:
        # print(i)
        if i != ' ':
            # print(a)
            a = a + i
        else:
            # print(a)
            L.append(a)
            a = ''
    SL = list(set(L))
    SL.sort()
    # print(SL)
    fci = ''
    i = 0
    while i < len(SL):
        nt = 0
        d = []
        for j in range(0, 4):
            if i + j < len(SL):
                d.append(SL[i + j])
        minl = len(d[0])
        for k in d:
            if minl > len(k):
                minl = len(k)
        nct = 0
        ct = ''
        for m in range(0, minl):
            var = True
            for p in range(0, len(d)):
                if d[0][m] == d[p][m]:
                    continue
                else:
                    var = False
                    break
            if var == True:
                ct = ct + d[0][m]
                nct += 1
            else:
                break
        for n in range(0, len(d)):
            d[n] = d[n][nct:]

        ct = str(len(d[0]) + len(ct)) + ct
        for q in range(0, len(d)):
            if q == 0:
                # print(d)
                ct = ct + '*' + d[q] + str(len(d[q + 1]))
            else:
                if q + 1 < len(d):
                    ct = ct + '<>' + d[q] + str(len(d[q + 1]))
                else:
                    ct = ct + '<>' + d[q]
        fci = fci + ct
        i = i + 4

    return fci


if __name__ == "__main__":
    A = "Stream streaming streamed Streamer"
    print(fci_util(A))
