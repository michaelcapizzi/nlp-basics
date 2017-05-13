# NLP Basics

## Preparation

You can clone this repository:

```
git@github.com:michaelcapizzi/nlp-basics.git
```

## Docker install

You can run the Jupyter notebooks in this repository with [Docker](http://docs.docker.com/installation) by running

```
% docker build -t michaelcapizzi/nlp-basics .
% docker run -p 8888:8888 --rm -it michaelcapizzi/nlp-basics # to start a Jupyter notebook server
[I 19:41:11.459 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[W 19:41:11.591 NotebookApp] Widgets are unavailable. Please install widgetsnbextension or ipywidgets 4.0
[W 19:41:11.598 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 19:41:11.742 NotebookApp] JupyterLab alpha preview extension loaded from /opt/conda/lib/python3.5/site-packages/jupyterlab
[I 19:41:11.802 NotebookApp] Serving notebooks from local directory: /code
[I 19:41:11.802 NotebookApp] 0 active kernels 
[I 19:41:11.802 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:8888/?token=f6925975b83f14758e79c55f81f1bec1267300747d5d6b08
[I 19:41:11.802 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 19:41:11.803 NotebookApp] 
    
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=f6925975b83f14758e79c55f81f1bec1267300747d5d6b08
```

Your specific token will be different.

## Manual pip / virtualenv install

To run the `jupyter` notebook you'll need a `python` environment for `python 3` with the following requirements:

 - jupyter
 - gensim
 - sklearn
 - numpy
 - beautifulsoup4

All of these can be installed via `pip` or using the `requirements.txt` file:

```
pip install -r requirements.txt
```

Then to open the notebook, simply run the following in the root folder of the cloned project:

```
jupyter notebook
```

This will open a new window in your default browser.  You can then open the notebook file of choice (ending in `.ipynb`) by clicking on it.

It will open in a new window.

You can edit a given cell by clicking on it.  To run the cell, push `CTRL-c`.




