def designerPdfViewer(h, s):
    result = []
    for w in s:
        result.append(h[ord(w) - 97])

    return max(result) * len(s)

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
s = 'abc'
print(designerPdfViewer(h, s))