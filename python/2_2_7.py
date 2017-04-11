def cmp_ignore_case(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    print s1, s2
    if s1[0] > s2[0]:
        return 1
    if s1[0] < s2[0]:
        return -1
    if s1[0] == s2[0]:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
