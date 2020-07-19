# work out how to make simple grid widgets for jupyter

Motivation. Often need to view data and edit/clean it. Historically have done this with a spreadsheet program (excel, gnumeric, libreOffice).

jupyter lab has a great csv viewer for files

but need a way to view and edit 

### Initial strategy
base it around csv + pandas DataFrame

## options
1. build on qgrid
- seems to handle a lot of rows without progrom

2. build  on ipysheet
- very flexible, clearly plays nice with ipywidgets
- not good out of the box display of large DataFrames

3. ipyaggrid
- seems like js is supported by a company
- don't know know much about pros/cons but examples are more complicated
