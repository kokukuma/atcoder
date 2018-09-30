import collections

n = int(raw_input())
v = map(int, raw_input().split())

even = [vi for i,vi in enumerate(v) if i % 2 == 0]
odd  = [vi for i,vi in enumerate(v) if i % 2 == 1]

evenc = collections.Counter(even)
oddc = collections.Counter(odd)

evenc_most_common = evenc.most_common(len(set(even)))
oddc_most_common = oddc.most_common(len(set(odd)))

# print(evenc_most_common)
# print(oddc_most_common)

if evenc_most_common[0][0] != oddc_most_common[0][0]:
    a = len(even) - evenc_most_common[0][1]
    b = len(odd) - oddc_most_common[0][1]
    print(a+b)
else:
    if evenc_most_common[0][1] >= oddc_most_common[0][1]:
        a = len(even) - evenc_most_common[0][1]
        b = len(odd)
        if len(oddc_most_common) > 1:
            b = len(odd) - oddc_most_common[1][1]
        print(a+b)
    elif evenc_most_common[0][1] < oddc_most_common[0][1]:
        a = len(odd) - oddc_most_common[0][1]
        b = len(even)
        if len(evenc_most_common) > 1:
            b = len(even) - evenc_most_common[1][1]
        print(a+b)

