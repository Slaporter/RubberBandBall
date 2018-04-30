import plotly
import plotly.plotly as py
import pandas as pd
izip = zip

df = pd.read_csv('latLng.csv')


flight_paths = []
for i in range(len(df)):
    flight_paths.append(
        dict(
            type='scattergeo',
            lon=[df['long1'][i], df['long2'][i], df['long3'][i],df['long4'][i],df['long5'][i],df['long6'][i]],
            lat=[df['lat1'][i], df['lat2'][i],df['lat3'][i],df['lat4'][i],df['lat5'][i],df['lat6'][i]],
            mode='lines',
            line=dict(
                width=1
            ),
        )
    )





layout = dict(
    title='Flight Paths over globe<br>(Click and drag to rotate)',
    showlegend=False,
    geo=dict(
        showland=True,
        showlakes=True,
        showcountries=True,
        showocean=True,
        countrywidth=0.5,
        landcolor='rgb(230, 145, 56)',
        lakecolor='rgb(0, 255, 255)',
        oceancolor='rgb(0, 255, 255)',
        projection=dict(
            type='orthographic',
            rotation=dict(
                lon=-100,
                lat=40,
                roll=0
            )
        ),
        lonaxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        ),
        lataxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        )
    )
)

fig = dict(data=flight_paths, layout=layout)
plotly.offline.plot(fig, validate=False, filename='d3-globe.html')

"""Reference:
https://plot.ly/python/lines-on-maps/
"""