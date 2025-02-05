from importlib_resources import files
from attotools import data

def setStyle(plt, name='sci'):
    stylename=f'{name}.mplstyle'
    plt.style.use(files(data).joinpath(stylename))