import numpy as np
import math
import matplotlib.pyplot as plt
from PointClass import Point

COLOR_MAP = 'viridis_r'
SIZE = 100
MAX_COLOR_RANGE = 1
MIN_COLOR_RANGE = -1
SIZE = 200
DENSITY = 20

def main():
    # Define and print the base points
    BasePoints = [ Point(0.0, 0.0, 0.0), \
               Point(0.0, 1.0, 1.0), \
               Point(1.0, 1.0, 0.5), \
               Point(1.0, 0.0, -1.0) ]

    # Make matrix and vector using base points
    Matrix, Vector = getMatrixAndVector( BasePoints )

    # Compute the coneficients
    Coefficients = np.linalg.solve( Matrix, Vector )

    # Define and print interpolation points
    SpaceStepX = 1.0 / DENSITY
    SpaceStepY = 1.0 / DENSITY
    Points = []
    for i in range( 1, DENSITY ):
        for j in range( 1,DENSITY ):
            aPoint = Point( SpaceStepX * i, SpaceStepY * j , 0.0 )
            interpolate( Coefficients, aPoint )
            Points.append( aPoint )

    # Depict all data on the screen
    printPointsArray(BasePoints)
    printPointsArray(Points)
    plt.colorbar()
    plt.show()



def printPointsArray( Points ):
    for i in range( 0, len( Points ) ):
        plt.scatter( Points[ i ].getPointX(), Points[ i ].getPointY(),\
                     c=Points[ i ].getValue(), s = SIZE,\
                     vmin=MIN_COLOR_RANGE, vmax=MAX_COLOR_RANGE )


def getMatrixAndVector( BasePoints ):
    Size = len( BasePoints )
    Matrix = np.zeros( ( Size, Size ) )
    Vector = np.zeros( ( Size, 1 ) )


    # the governing equation is: a0 + a1 * X + a2 * Y + a3 * X * Y = F( X, Y )
    for i in range( 0, Size ):
        Matrix[ i, 0 ] = 1.0
        Matrix[ i, 1 ] = BasePoints[ i ].getPointX()
        Matrix[ i, 2 ] = BasePoints[ i ].getPointY()
        Matrix[ i, 3 ] = BasePoints[ i ].getPointX() * BasePoints[ i ].getPointY()
        Vector[ i ] = BasePoints[ i ].getValue()

    return Matrix, Vector


def interpolate( Coefficients, Point ):

    # the governing equation is: a0 + a1 * X + a2 * Y + a3 * X * Y = F( X, Y )

    Value = Coefficients[ 0 ] \
          + Coefficients[ 1 ] * Point.getPointX() \
          + Coefficients[ 2 ] * Point.getPointY() \
          + Coefficients[ 3 ] * Point.getPointX() * Point.getPointY()
    Point.setValue( Value )



main()