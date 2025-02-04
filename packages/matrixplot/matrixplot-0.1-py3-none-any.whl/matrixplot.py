import matplotlib.pyplot

def plot(matrix, values=False, box=True):
    matplotlib.pyplot.gca().xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    matplotlib.pyplot.gca().yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))

    if box: matplotlib.pyplot.gca().set_box_aspect(1)

    matplotlib.pyplot.imshow(matrix, aspect="auto")
    
    midpoint = (matrix.min()+matrix.max())/2
    matplotlib.pyplot.colorbar(ticks=[matrix.min(), midpoint, matrix.max()])

    if values:
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                # x->columns, y->rows
                matplotlib.pyplot.text(j, i, "%.2f" % matrix[i,j], color="white" if matrix[i,j]<midpoint else "black", verticalalignment="center", horizontalalignment="center")
    
    matplotlib.pyplot.show()

    matplotlib.pyplot.clf()
