def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    idx, result = 0, []
    s = ''.join(S.split('-'))
    extra = len(s) % K
    if extra != 0:
        result.append(s[:extra].upper())
        idx = extra
    while idx < len(s):
        result.append(s[idx:idx + K].upper())
        idx += K
    return '-'.join(result)

l = '2-4A0r7-4k'
k=3
print(licenseKeyFormatting(l,k))