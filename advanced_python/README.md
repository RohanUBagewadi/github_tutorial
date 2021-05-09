
#Advanced Python tutorials

This repository is contains tricks and tutorial from [Patrick](https://www.python-engineer.com/).
This course contains 21 videos with a total duration of around 5 hours and covers topics like **collections**, **decorators**, **generators**, **multithreading**, **logging**, and much more.
For more detailed videos tutorials can be found [here](https://www.python-engineer.com/courses/advancedpython/).

## Table of Contents
1. [Requirements](#1-requirements)
2. [Installation](#2-installation)
3. [Topics](#3-topics)


## 1. Requirements

+ Python 3.7.6
+ Jupyter Notebook

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

## 3. Topics

* [1. Lists](01_lists.ipynb)
* [2. Tuples](02_tuple.ipynb)
* [3. Dictionary](03_dictionaries.ipynb)
* [4. Sets](04_sets.ipynb)
* [5. Strings](05_strings.ipynb)
* [6. Collections](06_collections.ipynb)
* [7. Itertools](07_Itertools.ipynb)
* [8. Lambda function](08_lambda.ipynb)
* [9. Exceptions](09_exceptions.ipynb)
* [10. Logging](10_logging.ipynb)
* [11. JSON](11_json.ipynb)
* [12. Random Numbers](12_random.ipynb)
* [13. Decorators](13_decorators.ipynb)
* [14. Generators]()
* [15. Threading vs Multiprocessing](15_threading_and_multiprocessing.ipynb)
* [16. Threading Detailed](16_threading_deatails.ipynb)
* [17. Multiprocessing Detailed](17_multiprocessing_details.ipynb)
* [18. Functional arguments](18_function_arguments.ipynb)
* [19. The asterisk (*) operator]()
* [20. Shallow vs Deep copying]()
* [21. Context Managers]()


