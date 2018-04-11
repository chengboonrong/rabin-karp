# plot a word counts graph offline
import plotly
from plotly.graph_objs import *

plotly.tools.set_credentials_file(username='toshio97', api_key='weuJwHwO3oJkMOQmSrn3')
plotly.tools.set_config_file(plotly_domain='',
                             plotly_streaming_domain='',
                             world_readable=False
                             )

plotly.offline.plot({
    "data": [Scatter(x=list(wordDict.keys()), y=list(wordDict.values()))],
    "layout": Layout(title="word count"),
})