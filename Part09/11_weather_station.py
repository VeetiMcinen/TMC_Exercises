class WeatherStation:
    def __init__(self, city:str) -> None:
        self.__city = city
        self.__observations = []

    def add_observation(self, observation:str):
        self.__observations.append(observation)
    
    def latest_observation(self):
        if len(self.__observations) == 0:
            return ""
        else:
            return self.__observations[-1]
    
    def number_of_observations(self):
        return (len(self.__observations))
    
    def __str__(self):
        return (f"{self.__city}, {self.number_of_observations()} observations")