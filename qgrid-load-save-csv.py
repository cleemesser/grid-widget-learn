# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python [conda env:jupyter] *
#     language: python
#     name: conda-env-jupyter-py
# ---

# %% [markdown]
# ### working out how to do a basic interactive CSV/dataframe in jupyter
# try using qgrid + buttons first

# %%
import pandas as pd
import ipywidgets
import qgrid

# note may want to try with %asyncio to do automatic updating

# %%
# set up defaults
qgrid.set_defaults(precision=2)

# allow jupyternotebook to use full width
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# %%
class CsvGridWidget:
    """
    Idea is to make it easy to view and edit a csv file (or anyting loadable by pandas)
    into jupyter notebook. 
    """
    def __init__(self, file_name, **kwargs_read_csv):
        self.file_name = file_name
        default_options = {"keep_default_na": False}
        default_options.update(kwargs_read_csv)

        self.df = pd.read_csv(file_name, **default_options)
        # gui
        self.qgrid_widget = qgrid.show_grid(self.df)
        # save button
        self.savebutton = ipywidgets.Button(
            description="Save",
            tooltip="click to save and resyncronize the dataframe back to file",
            disabled=False,
        )
        def on_save_button_clicked(b):
            print(f"Saved {self.file_name}") #type(b), repr(b))
            self.save()
        self.savebutton.on_click(on_save_button_clicked)
        # container/layout
        self.topwidget = ipywidgets.VBox([self.qgrid_widget, self.savebutton])

    def save(self):
        updated_df = self.qgrid_widget.get_changed_df()
        updated_df.to_csv(self.file_name, index=False)  # quoting=csv.QUOTE_NONNUMERIC)
        self.df = updated_df

    def show(self):
        """really this just returns the widget
        maybe add Display call?"""
        display(self.topwidget)


# %%
# #!wget http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv # source url https://support.spatialkey.com/spatialkey-sample-csv-data/
datacsv = CsvGrid("SalesJan2009.csv")

# %% [markdown]
# ### Try out the grid
# Note, you can reorder the sorting by clicking on the column headers
# Try editing a field to change its value
#
# Note you can save the data frame back to its original file by clicking the "save" button

# %%
datacsv.show()


# %%
# can also call functions directly: 
datacsv.save()

# %%
datacsv.df.head()

# %%
