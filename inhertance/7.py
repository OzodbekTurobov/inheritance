class Odam:
    def __init__(self,ism,fam,yosh,yili):
        self.ism = ism
        self.fam = fam
        self.yosh =yosh
        self.yili = yili

    def parol(self):
        print(self.ism, self.fam, self.yosh, self.yili)

o1 = Odam("Ozodbek", "Turobov", 14, 2008)
o2 = Odam("Abdurahmon", "Isroilov", 10, 2012)
o3 = Odam("Ubaydullo", "Jumayev", 21 ,2002)
o4 = Odam("Shoxjaxon", "Turobov", 12 ,2010)

o1.Odam()
o2.Odam()

class Mashina:
    def __init__(self,nomi,rangi,qandayligi,yili):
        self.nomi = nomi
        self.rangi = rangi
        self.qandayligi = qandayligi
        self.yili = yili

    def parol(self):
        print(self.nomi, self.rangi, self.qandayligi, self.yili)

m1 = Mashina("Rols Roys", "Kulrang", "zo`r", 2022)
m2 = Mashina("Cobalt", "oq","zo`r", 2022)
m3 = Mashina("Lada", "qora", "zo`r",2022)
m4 = Mashina("BMW", "qizil", "zo`r",2022)

m1.Mashina()
m2.Mashina()

class Telefon:
    def __init__(self,nomi,rangi,qandayligi,yili):
        self.nomi = nomi
        self.rangi = rangi
        self.qandayligi = qandayligi
        self.yili = yili

    def parol(self):
        print(self.nomi, self.rangi, self.qandayligi, self.yili)

t1 = Telefon("Apple", "kok","zo`r", 2022)
t2 = Telefon("samsung", "qora","zo`r", 2022)
t3 = Telefon("A", "oq", "zo`r",2022)
t4 = Telefon("Redmi", "qizil", "zo`r",2022)

t1.Telefon()
t2.Telefon()

class Hayvon:
    def __init__(self,nomi,rangi,qandayligi,turi):
        self.nomi = nomi
        self.rangi = rangi
        self.qandayligi = qandayligi
        self.turi = turi

    def parol(self):
        print(self.nomi, self.rangi, self.qandayligi, self.yili)

h1 = Hayvon("oqvoy", "oq", "chiroyli", 2020)
h2 = Hayvon("qoravoy", "qora", "zor", 2020)
h3 = Hayvon("jig", "jigarrang", "bo`ladi" ,2020)
h4 = Hayvon("oq panja", "kulrang", "yaxshi" ,2020)

h1.Hayvon()
h2.Hayvon()