import plotly as pl
import plotly.graph_objects as go
import numpy as np
import plotly.offline.offline

def cubes(x, y, z, w, h, l, color):
    # create points
    x, y, z = np.meshgrid(
        np.linspace(x - w, x + w, 2), 
        np.linspace(y - h, y + h, 2), 
        np.linspace(z - l, z + l, 2),
    )
    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    
    return go.Mesh3d(x=x, y=y, z=z, alphahull=1, flatshading=True, color=color, lighting={'diffuse': 0.1, 'specular': 2.0, 'roughness': 0.5})

fig = go.Figure()
# set edge length of cubes
size = 5

# add outer cube
fig.add_trace(cubes(0,0,0, 10,10,10, 'rgba(255,100,0,0.1)'))

# add inner center cube
fig.add_trace(cubes(-5,5,5, -5,-5,-5, 'rgba(100,0,100,0.1)'))

# # add inner cubes
# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))
# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))

# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))
# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))

# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))
# fig.add_trace(cubes(0,0,0, 'rgba(100,0,100,0.1)'))

# embedable_chart = pl.offline.plot(fig, include_plotlyjs=True, output_type='div')
# f = open("embedable_chart.html", "w")
# f.write(embedable_chart)
# f.close()
fig.show()