class ShaxmatOlimpyadasi:
    ishtirokchilar_SONI=0
    hakamlar_SONI=0
    tomoshabinlar_SONI=0
a=ShaxmatOlimpyadasi()
a.hakamlar_SONI=5
a.ishtirokchilar_SONI=20
a.tomoshabinlar_SONI=175
jami=a.hakamlar_SONI+a.ishtirokchilar_SONI+a.tomoshabinlar_SONI
# print(jami, a.hakamlar_SONI, a.ishtirokchilar_SONI, a.tomoshabinlar_SONI)
class JahonOlimpiyada(ShaxmatOlimpyadasi):
    ishchilar_soni=0
b=JahonOlimpiyada()
b.ishchilar_soni=20
print(jami, b.ishchilar_soni, a.hakamlar_SONI, a.ishtirokchilar_SONI, a.tomoshabinlar_SONI)
