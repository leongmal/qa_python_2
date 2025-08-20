class PointsForPlace:
  
    @staticmethod
    def get_points_for_place(place):
        points = 0
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101-place

        return int(points)

class PointsForMeters:

    @staticmethod
    def get_points_for_meters(meters:int):
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        
        return int(points)

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        self.points = 0
    
    def get_total_points(self, meters, place):
        point_place = PointsForPlace.get_points_for_place(place)
        point_meter = PointsForMeters.get_points_for_meters(meters)
        total = point_place + point_meter
        return total


print(PointsForPlace.get_points_for_place(10))
print(PointsForMeters.get_points_for_meters(10))

total_points = TotalPoints()
print(PointsForPlace.get_points_for_place(10))
print(PointsForMeters.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))