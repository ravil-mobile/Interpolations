import numpy as np
import math
import matplotlib.pyplot as plt

MIN = 0;
MAX = 50;
POINT_NUMBER = 21;
PERIOD = 2.0 * ( MAX - MIN ) /  ( POINT_NUMBER - 1 )

def main():

    # Get finite data from the real function
    RealFunction = getPointsFromFunction( np.linspace( MIN, MAX, 500 ) )

    # Get some set of data from the real function to make interpolation
    Nodes \
         = getPointsFromFunction( np.linspace( MIN, MAX, POINT_NUMBER ) )

    # Interpolation processing
    InterpolationInterval = RealFunction[ 0 ]
    InterpolationFunction = np.zeros( len( InterpolationInterval ) )
    for i in range ( 0, POINT_NUMBER ):
        Temp = computeSincFunction( Nodes[0][i], Nodes[1][i], \
                                    PERIOD, InterpolationInterval )
        InterpolationFunction += Temp
        #plt.plot(InterpolationInterval, Temp, '--')

    # Depict the results
    fig = plt.figure(1)
    fig.canvas.set_window_title('Sinc Interpolation')
    plt.plot(RealFunction[0], RealFunction[1], 'k-')
    plt.plot(Nodes[0], Nodes[1], 'ro')
    plt.plot(InterpolationInterval, InterpolationFunction, 'g--')
    plt.grid()
    plt.show();


def computeSincFunction( PivotPointX, PivotPointY, Period, XCoord ):
    Array = []
    Scale = ( 2.0 * np.pi ) / Period
    for i in range( 0, len( XCoord ) ):
        # Avoid the pivot point
        if ( XCoord[ i ] == PivotPointX ):
            Array.append( PivotPointY )
            continue

        # Compute the function
        Argument = Scale * ( XCoord[ i ] - PivotPointX )
        Array.append( PivotPointY * np.sin( Argument ) / Argument )
    return Array


def getPointsFromFunction( Array ):
    Temp = []
    for i in range( 0, len( Array ) ):
        Temp.append( function( Array[i]) )

    NewArray = np.array( [ Array, Temp ] )
    return NewArray


def function( x ):
    #y = math.cos( 0.7 * x ) + math.log1p( x + 1 )
    y = x**2 * math.cos(x) * math.log1p( x + 1 )
    return y


main()