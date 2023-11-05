from  service import Point3D



class Scene:
    def __init__(self,indeficator, models, flashes, cameras):

        if len(models) > 0:
            self.Models = models
        else:
            raise Exception ("Должна быть одна модель")

        self.Flashes = flashes

        if len(cameras) > 0:
            self.Cameras = cameras
        else:
            raise Exception ("No cameras")

    def method_1(self, type):
        return None

    def method_2(self, type1, type2):
        return None
class Texture:
    pass

class Poligon:
    def __init__(self,point):
        self.point = [point]

class PolygonalModel:
    def __init__(self, textures):
        self.Poligons = []
        self.Textures = textures
        self.Poligons.append(Poligon(Point3D))

class Flash:
    def __init__(self):
        self.Location = None
        self.Angle = None
        self.Color = None
        self.Power = None

    def Rotate(self, angleAction):
        pass

    def Move (self, pointAction):
        pass

class Camera:
    def __init__(self):
        self.Location = None
        self.Angle = None

    def Rotate(self, angleAction):
        pass

    def Move (self, pointAction):
        pass

