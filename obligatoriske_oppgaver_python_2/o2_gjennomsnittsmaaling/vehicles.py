class Vehicle:
    def __init__(self, merke, ars_Modell, km, pris, regNr):
        self.__merke = merke
        self.__ars_Modell = ars_Modell
        self.__km = km
        self.__pris = pris
        self.__regNr = regNr
        self.__speedTicket = []

    def setSpeedTicket(self, reg, tid, hastighet, fartsgrense):
        ticket = SpeedTicket(reg, tid, hastighet, fartsgrense)
        self.__speedTicket.append(ticket)

    def getSpeedTicket(self):
        if len(self.__speedTicket) == 0:
            print(f'No speedtickets recorded')
        else:
            for i in range(len(self.__speedTicket)):
                print(f'Speedticket {i+1}:')
                print(
                    f'Tid: {self.__speedTicket[i].getTid()}, hastighet: {self.__speedTicket[i].getHastighet()}, fartsgrense: {self.__speedTicket[i].getFartsgrense()}')

    def getMerke(self):
        return self.__merke

    def merke(self, merke):
        self.__merke = merke

    def getArsModell(self):
        return self.__ars_Modell

    def ars_Modell(self, ars_Modell):
        self.__ars_Modell = ars_Modell

    def getKm(self):
        return self.__km

    def km(self, km):
        self.__km = km

    def getPris(self):
        return self.__pris

    def pris(self, pris):
        self.__pris = pris

    def getRegNr(self):
        return self.__regNr

    def regNr(self, regNr):
        self.__regNr = regNr

    def __str__(self):
        return f'Merke: {self.__merke}, Modell: {self.__ars_Modell}, Kilometer: {self.__km}, Pris: {self.__pris}, RegNr: {self.__regNr}'


class Car(Vehicle):
    def __init__(self, merke, ars_Modell, km, pris, regNr, dører):
        super().__init__(merke, ars_Modell, km, pris, regNr)
        self.__dører = dører

    def getDører(self):
        return self.__dører

    def dører(self, dører):
        self.__dører = dører

    def __str__(self):
        return (super().__str__() + f', Antall dører: {self.__dører}')


class Truck(Vehicle):
    def __init__(self, merke, ars_Modell, km, pris, regNr, hjuldrift):
        super().__init__(merke, ars_Modell, km, pris, regNr)
        self.__hjuldrift = hjuldrift

    def getHjuldrift(self):
        return self.__hjuldrift

    def hjuldrift(self, hjuldrift):
        self.__hjuldrift = hjuldrift

    def __str__(self):
        return (super().__str__() + f', Hjuldrift: {self.__hjuldrift}')


class SUV(Vehicle):
    def __init__(self, merke, ars_Modell, km, pris, regNr, passasjerer):
        super().__init__(merke, ars_Modell, km, pris, regNr)
        self.__passasjerer = passasjerer

    def getPassasjerer(self):
        return self.__passasjerer

    def passasjerer(self, passasjerer):
        self.__passasjerer = passasjerer

    def __str__(self):
        return (super().__str__() + f', Antall passasjerer: {self.__passasjerer}')


class SpeedTicket:
    def __init__(self, reg_nummer, tid, hastighet, fartsgrense):
        self.__reg_nummer = reg_nummer
        self.__tid = tid
        self.__hastighet = hastighet
        self.__fartsgrense = fartsgrense

    def getReg_nummer(self):
        return self.__reg_nummer

    def reg_nummer(self, reg):
        self.__reg_nummer = reg

    def getTid(self):
        return self.__tid

    def tid(self, tid):
        self.__tid = tid

    def getHastighet(self):
        return self.__hastighet

    def hastighet(self, hastighet):
        self.__hastighet = hastighet

    def getFartsgrense(self):
        return self.__fartsgrense

    def fartsgrense(self, fartsgrense):
        self.__fartsgrense = fartsgrense
