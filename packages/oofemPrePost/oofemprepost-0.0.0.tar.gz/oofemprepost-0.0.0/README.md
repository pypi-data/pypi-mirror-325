<h2 align="center">
  OOFEM PrePost-Processing Python Package (oofemPrePost)
</h2>


`oofemPrePost` is a simple Python package with following purposes:
* `log2csv`(log_file.log, output_file.csv): Process [OOFEM](https://github.com/cunyizju/oofem-vltava) simulation logs and export extracted data to a CSV file, based on which the computational efficiency can be analysed.
* Extract history variables such as force and displacement (to be done)
* `hm2oofem`(input_filename.inp, output_filename.in): Transform HyperMesh.input file to OOFEM.in files for [OOFEM](https://github.com/cunyizju/oofem-vltava)

## Prerequisite
* csv
* re
* twine (for build and upload to PyPi)

## Generate oofemPrePost

```
python setup.py sdist bdist_wheel
```

## Upload to PyPi

```
twine upload dist/*
```

## Installation

You can install or upgrade the package by running:

```
pip install oofemPrePost
```
To install the updatest version of oofemPrePost,
```
pip install --upgrade oofemPrePost
```

## How to use it?
#### Data transfer from hypermesh 2024.0/2024.1 to oofem/mole

Node, element, and node sets will be transferred. Specifically, for 2D model, 
```
from oofemPrePost import *
hm2of2d('*.inp','*.in')
```

for 3D model, 
```
from oofemPrePost import *
hm2of3d('*.inp','*.in')
```

Note that it can process 2 or 3 materials, i.e., 'mat 1 mat 2 mat 3' can appear in *.in file.

#### Extract time and number of iterations in each increment
```
timeCount.log2csv('*.log', '*.csv')
```
Then the data will look like
```
solutionSteps,userTimes,numIterations
1,1.18,1
2,1.2,1
3,1.2,1
4,1.16,1
```