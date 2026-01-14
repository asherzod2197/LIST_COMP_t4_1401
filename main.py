gap = "Python juda qiziqarli dasturlash tili"
uzun_sozlar = [s for s in gap.split() if len(s) > 5]
print(uzun_sozlar)

sonlar = [-5, 3, -2, 7, 0, -1, 4]
yangi = [x if x > 0 else 0 for x in sonlar]
print(yangi)
