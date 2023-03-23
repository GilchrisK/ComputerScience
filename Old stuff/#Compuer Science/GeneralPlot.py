# importing the required module
import matplotlib.pyplot as plt
#called plt as an abbreviated version. #matplotlib.pyplot =plt



def plotIt(x,y,xl,yl,t):
    plt.plot(x,y)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.title(t)
    plt.show()







