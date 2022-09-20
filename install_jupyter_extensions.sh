#!/bin/bash

jupyter labextension install dask-labextension  \
			     jupyter-matplotlib \
                             @jupyter-widgets/jupyterlab-manager \
                             @pyviz/jupyterlab_pyviz 
