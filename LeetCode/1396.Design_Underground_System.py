class UndergroundSystem:

    def __init__(self):
        self.id_station = {}
        self.id_time = {}
        self.station_duration = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_station[id] = stationName
        self.id_time[id] = t
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        duration = t - self.id_time[id]
        trip = (self.id_station[id], stationName)
        if trip in self.station_duration.keys():
            self.station_duration[trip].append(duration)
        else:
            self.station_duration[trip] = [duration]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        return sum(self.station_duration[trip]) / len(self.station_duration[trip])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)