#!/bin/bash

jupyter serverextension enable --sys-prefix --py nbserverproxy
jupyter labextension install dask-labextension@1.0.0-rc.0  \
                             @pyviz/jupyterlab_pyviz 
