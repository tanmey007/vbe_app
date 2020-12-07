import re
import numpy as np


def fci_util(A):
    A = re.sub('[-]', ' ', A).lower()
    # print(A)
    L = A.split(" ")
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
        print(d)
        minl = np.min([len(i) for i in d])
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
        # print(ct)
        if len(d) > 1:
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
        # print('Fci = ', fci)
        i = i + 4

    return fci


if __name__ == "__main__":
    A = "creme creming cremated cremlin cromo"
    print(fci_util(A))
