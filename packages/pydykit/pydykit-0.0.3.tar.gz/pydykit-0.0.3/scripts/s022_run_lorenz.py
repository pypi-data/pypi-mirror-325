import plotly.graph_objects as go

import pydykit
from pydykit.plotters import Plotter

manager = pydykit.managers.Manager()

name = "lorenz"
path_config_file = f"./pydykit/example_files/{name}.yml"

manager.configure_from_path(path=path_config_file)

result = pydykit.results.Result(manager=manager)
result = manager.manage(result=result)

df = result.to_df()

plotter = Plotter(results_df=df)

fig = go.Figure()
plotter.plot_3d_trajectory(
    figure=fig,
    x_components=df["x"],
    y_components=df["y"],
    z_components=df["z"],
    time=df["time"],
)

fig.update_layout(font_family="Serif")

fig.show()

df.to_csv(f"test/reference_results/{name}.csv")
