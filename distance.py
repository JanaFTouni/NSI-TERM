
def hamming(ch1: str, ch2: str) -> int:
    dist = 0
    for i in range(min(len(chr1), len(chr2))):
        dist =+ 1
    return dist + abs(len(ch1 - ch2))