from datetime import datetime

def main():
    flights = []
    flights.append(Flight("US230", 
        datetime(2014, 4, 5, 5, 5, 0),
        datetime(2014, 4, 5, 6, 15, 0)))
    flights.append(Flight("US235", 
        datetime(2014, 4, 5, 6, 55, 0),
        datetime(2014, 4, 5, 7, 45, 0)))
    flights.append(Flight("US237", 
        datetime(2014, 4, 5, 9, 35, 0),
        datetime(2014, 4, 5, 12, 55, 0)))
    
    itinerary = Itinerary(flights)
    print(itinerary.getTotalTravelTime())
    print(itinerary.getTotalFlightTime())

class Flight:
    def __init__(self, flightNo, departureTime, arrivalTime):
        self.flightNo = flightNo
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime
  
    def getFlightTime(self):
        return (self.arrivalTime.timestamp() - 
            self.departureTime.timestamp()) / 60
  
    def getDepartureTime(self):
        return self.departureTime

    def getArrivalTime(self):
        return self.arrivalTime
  
    def setArrivalTime(self,arrivalTime):
        self.arrivalTime = arrivalTime
  
    def setDepartureTime(self,departureTime):
        self.departureTime = departureTime

class Itinerary:
    def __init__(self, flights):
        self.flights = flights
  
    def getTotalTravelTime(self):
        totalTime = self.getTotalFlightTime()
        for i in range(len(self.flights) - 1):
            time = self.flights[i + 1].getDepartureTime().timestamp() - \
                self.flights[i].getArrivalTime().timestamp()
            totalTime += time / 60
        return totalTime;
  
    def getTotalFlightTime(self):
        flightTime = 0
        for flight in self.flights:
            flightTime += flight.getFlightTime()
        return flightTime

main()