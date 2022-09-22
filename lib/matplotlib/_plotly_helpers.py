import builtins

from datetime import datetime
from plotly import tools

__cell_id__ = 0

class Plotly:

    @classmethod
    def save(cls, fig):
        try:
            plot = tools.mpl_to_plotly(fig)
            json = plot.to_json()
            cell_id = __cell_id__
            timestamp = datetime.utcnow().timestamp()
            file = open("plots/{}-{}.json".format(cell_id, timestamp), "w")
            file.write(json)
            file.close()
        except:
            print('An error occurred while writing the plot to JSON.')