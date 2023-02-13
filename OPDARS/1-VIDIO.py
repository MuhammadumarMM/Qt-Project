class Person:
    name=''
    surname=''
    birth=''
    adress=''
    psSeriya=''
    psDig=0
a=Person()
a.name='Abduhodi'
a.surname='Tursunboyev'
a.birth='05-09-1997'
a.adress='Asaka city'
a.psSeriya='AA'
a.psDig=1699727
print("{0:<20s} {1:<20s} {2:<11} {3:<15}".format(a.name,a.surname,a.birth,a.adress))