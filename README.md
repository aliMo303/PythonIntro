[![Shipping files](https://github.com/neuefische/ds-python-basics/actions/workflows/workflow-02.yml/badge.svg?branch=main&event=workflow_dispatch)](https://github.com/neuefische/ds-python-basics/actions/workflows/workflow-02.yml)
# Python Basics

In this Repository you can find Jupyter-Notebooks that you should **work on together as Pair-Programmers**. 

The notebooks contain repetitions from the preparation repository, but also new content on the required Python basics. 

Please work on the notebooks in the order listed below:

1. [Intro to Jupyter Lab](./Intro_to_Jupyter_Lab.ipynb)

2. [Coding best practices](./Coding_best_practices.ipynb)

# Basics

1. [Numeric Variable Types](./Basics/1_Numeric_Variable_Types.ipynb)
2. [Strings](./Basics/2_Strings.ipynb)
3. [If Statements](./Basics/3_If_Statements.ipynb)
4. [Loops](./Basics/4_Loops.ipynb)

# Data Structures in Python

1. [Lists](./Data_Structures_in_Python/1_Lists.ipynb) 
2. [Tuples](./Data_Structures_in_Python/2_Tuples.ipynb)
3. [Dictionaries](./Data_Structures_in_Python/3_Dictionaries.ipynb)
4. [Sets](./Data_Structures_in_Python/4_Sets.ipynb)
5. [Comprehension](./Data_Structures_in_Python/5_Comprehension.ipynb)

# Functions

1. [Introduction to functions](./Functions/1_Introduction_to_Functions.ipynb)
2. [Function definitions](./Functions/2_Function_Definitions.ipynb)
3. [Calling Functions](./Functions/3_Calling_Functions.ipynb)
4. [Function challenge](./Functions/4_Functions_Challenge.ipynb)

# Environment

## Set up your Environment

### For **`MacOS`** :

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyterlab
```
-------------------------------------------

### For **`WindowsOS`** : 

Open `PowerShell` CLI (as an administrator) :

```Bash
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install jupyterlab
```

Open `Git-Bash` CLI (as an administrator) :

```Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
pip install jupyterlab
```
### *Note :*

If you encounter an error, try using the following command:

```Bash
python.exe -m pip install --upgrade pip
```
