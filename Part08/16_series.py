class Series:
    def __init__(self, name:str, seasons:int, genres:list):
        self.name = name
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
    def __str__(self):
        if len(self.ratings) == 0:
            return (f"{self.name} ({self.seasons} seasons)\ngenres: {', '.join(map(str, self.genres))}\nno ratings")
        else:
            average_rating = sum(self.ratings)/len(self.ratings)
            return (f"{self.name} ({self.seasons} seasons)\ngenres: {', '.join(map(str, self.genres))}\n{len(self.ratings)}  ratings, average {round(average_rating,1)} points")
    
    
    def rate(self, rating:int):
        self.ratings.append(rating)
    def minimum_grade(self, grade:float, series_list:list):
        newlist = []
        for series in series_list:
            average_rating = sum(self.ratings)/len(self.ratings)
            if series

dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

#2/3 points