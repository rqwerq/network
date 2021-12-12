import matplotlib.pyplot as plt
import numpy
def get_index(route):
    index ={'a':0,'b':1,'c':2,'d':3,'e':4}
    start,end =route
    return index[start],index[end]
def draw_network(network,flowBundle):
    plt.rcParams['font.sans-serif']=['SimHei'] 
    x =[]
    y =[]
    for i in range(len(network.nodes())):
        x.append(numpy.random.rand())
        y.append(numpy.random.rand())
    plt.scatter(x, y)
    for i in range(len(x)):
        plt.annotate(list(network.nodes())[i], xy = (x[i], y[i]), xytext = (x[i], y[i])) 
    network_links =network.links()[:] 
    for route in network_links:
        if route in network.links():
             if (route[1],route[0]) in network_links:
                 network_links.remove((route[1],route[0]))

    for route in network_links:
        start,end =get_index(route)
        plt.plot([x[start],x[end]],[y[start],y[end]],color='b')
    for temp in flowBundle.flows:
        route =temp[0]
        links =zip(route[:-1],route[1:])
        for link in links:
            start,end =get_index(link)
            plt.plot([x[start],x[end]],[y[start],y[end]],color='r')

    plt.show()  