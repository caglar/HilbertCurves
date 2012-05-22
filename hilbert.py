import sys, math
import numpy as np

data = np.zeros((256, 256))
edges = []

def make_line(edges, X, Y):
#    import pudb; pudb.set_trace()
    if edges:
        i, j = edges[-1]
        xstart = int(min(i, X))
        xend = int(max(i, X))
        ystart = int(min(j, Y))
        yend = int(max(j, Y))
        if xstart == xend:
            for y in xrange(ystart, yend):
                data[xstart][y] = 1
        if ystart == yend:
            for x in xrange(xstart, xend):
                data[x][ystart] = 1
def hilbert_curves(xi, yj, level):
    if xi != yj:
        raise Exception("must be square.")
    elif (2**level >= xi):
        raise Exception("xi should be less then the power of two.")
    else:
        hilbert(0.0, 0.0, xi, 0.0, 0.0, yj, level)

def hilbert(x0, y0, xi, xj, yi, yj, n):
    if n <= 0:
        X = x0 + (xi + yi)/2
        Y = y0 + (xj + yj)/2
        # Merge the dots
        make_line(edges, X, Y)
        edges.append((X, Y))
    else:
        hilbert(x0,               y0,               yi/2, yj/2, xi/2, xj/2, n - 1)
        hilbert(x0 + xi/2,        y0 + xj/2,        xi/2, xj/2, yi/2, yj/2, n - 1)
        hilbert(x0 + xi/2 + yi/2, y0 + xj/2 + yj/2, xi/2, xj/2, yi/2, yj/2, n - 1)
        hilbert(x0 + xi/2 + yi,   y0 + xj/2 + yj,  -yi/2,-yj/2,-xi/2,-xj/2, n - 1)

if __name__=="__main__":
    hilbert_curves(256, 256, 7)
    import pylab
    pylab.axis("off")
    pylab.gray()
    pylab.imshow(data)
    pylab.show()
