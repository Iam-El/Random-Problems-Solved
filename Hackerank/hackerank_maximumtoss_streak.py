def getMaxStreaks(toss):
    # Return an array of two integers containing the maximum streak of heads and tails respectively
    if toss is None:
        return [0, 0]

    if len(toss) == 1:
        if toss[0] == "Heads":
            return [1, 0]
        if toss[0] == "Tails":
            return [0, 1]

    heads = 0
    tails = 0
    headCount = 0
    tailCount = 0
    prev = None;
    for i in range(0, len(toss)):
        if prev is not None and toss[i] == toss[i - 1]:
            if toss[i] == 'Heads':
                headCount = headCount + 1
            if toss[i] == 'Tails':
                tailCount = tailCount + 1
        else:
            if toss[i] == "Heads":
                tailCount = 0
                headCount = 1
            if toss[i] == "Tails":
                tailCount = 1
                headCount = 0
        if headCount > heads:
            heads = headCount
        if tailCount > tails:
            tails = tailCount
        prev = toss[i]
    return [heads, tails]
