import math

class Point:

    def __init__( self, PointX, PointY, Value ):
        self.__PointX = PointX
        self.__PointY = PointY
        self.__Value = Value
        pass


    def getPointX(self):
        return self.__PointX

    def getPointY(self):
        return self.__PointY

    def getValue(self):
        return self.__Value

    def getDistanceToPoint( self, Point ):
        DeltaX = self.__PointX - Point.getPointX()
        DeltaY = self.__PointY - Point.getPointY()
        Length = math.sqrt( ( DeltaX**2 ) + ( DeltaY )**2 )
        return Length

    def setValue(self, Value):
        self.__Value = Value