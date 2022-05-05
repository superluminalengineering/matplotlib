import plotly

from datetime import datetime
from plotly import tools

class Plotly:

    @classmethod
    def save(cls, fig):
        plot = tools.mpl_to_plotly(fig)
        json = plot.to_json()
        timestamp = datetime.utcnow()
        file = open("plots/{}.html".format(timestamp), "w")
        file.write(json)
        file.close()