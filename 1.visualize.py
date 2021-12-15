import matplotlib.pyplot as plt
x = [30, 20, 30,10]
y = [0, -10, -30, -20]
links =[(1,2), (1,4), (2,3),(2,4),(3,4)]
fig, ax = plt.subplots()
ax.plot(x, y, "p")
for link in links:
    f, t = link
    ax.plot([x[f-1], x[t-1]], [y[f-1], y[t-1]], "b")
    time=(((x[t-1]-x[f-1])**2) + ((y[t-1]-y[f-1])**2))**0.5  
    ax.annotate('time=%.0f'%time,xy=((x[t-1]+x[f-1])/2,(y[t-1]+y[f-1])/2))
    
    
for i, (xi, yi) in enumerate(zip(x, y)):
    ax.annotate(chr(i+65), (xi, yi), fontsize=20)