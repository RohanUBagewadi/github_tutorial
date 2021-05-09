
# Python tutorials

This repository contains python tutorials and python practice files. The tutorial is divided into following sections:


## Table of Contents
1. [Requirements](#1-requirements)
2. [Installation](#2-installation)
3. [List of Tutorials](#3-list-of-tutorials)


## 1. Requirements

* Python 3.7.6
* Jupyter Notebook

## 2. Installation 

1. Jupyter Notebook installation:
   
   follow procedures as mentioned in: [here](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

2. Create python virtual environment.

   ```bash
   conda create --name python_classic
   conda activate python_classic
   ```

3. AddPython environment to jupyter notebook:
   
   follow procedures as mentioned in: [here](https://janakiev.com/blog/jupyter-virtual-envs/)
   
   ```bash
   pip install --user ipykernel
   python -m ipykernel install --user --name=python_classic
   ```

This should print the following:
Installed kernelspec myenv in /home/user/.local/share/jupyter/kernels/python_classic

## 3. List of Tutorials

  * [Advanced Python](#31-advanced-python)

### 3.1. Advanced Python
This repository is contains tricks and tutorial from [Patrick](https://www.python-engineer.com/).
This course contains 21 videos with a total duration of around 5 hours and covers topics like **collections**, **decorators**, **generators**, **multithreading**, **logging**, and much more.
For more detailed videos tutorials can be found [here](https://www.python-engineer.com/courses/advancedpython/).

