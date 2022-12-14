# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(year, country, co2)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Masking for year 2000
mask_2000 = dataset['year'] == 2000
df_2000  = dataset[mask_2000]
df_2000 = pd.DataFrame(df_2000.groupby('country')['co2'].sum()).reset_index().sort_values(by='co2', ascending = False)

# Masking for year 2020
mask_2020 = dataset['year'] == 2020
df_2020  = dataset[mask_2020]
df_2020 = pd.DataFrame(df_2020.groupby('country')['co2'].sum()).reset_index().sort_values(by='co2', ascending = False)

# Finally, creating the barchart
fig = go.Figure(data = [
    go.Bar(
        name = '2020',
        x = df_2020['country'][:5], 
        y = df_2020['co2'][:5],
        marker = dict(color = '#f5c064'),
        text = df_2020['co2'][:5],
        textposition = "outside"),

    go.Bar(
        name = '2000',
        x = df_2000['country'][:5], 
        y = df_2000['co2'][:5],
        marker = dict(color = '#6e0000'),
        text = df_2000['co2'][:5],
        textposition = "outside"    
    )
]
)
fig.update_layout(barmode = 'group', title = 'CO2 Gas Emissions Ranked 5 Countries: 2000 vs 2020',
                  width = 800, height = 600,
                  paper_bgcolor = '#F2F3FD')
pio.write_image(fig, "fig.png")