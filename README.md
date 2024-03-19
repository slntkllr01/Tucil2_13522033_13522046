# Tugas Kecil 2 IF2211 Strategi Algoritma<br>Semester II tahun 2023/2024<br>Divide and Conquer Algorithm For Making Bezier Curve
> by Bryan Cornelius Lauwrence & Raffael Boymian Siahaan

## Table of Contents

- [General Information](#general-information)
- [File Structures](#file-structures)
- [Requirement](#requirement)
- [Setup and Usage](#setup-and-usage)
- [Authors](#authors)

## General Information
Drawing Bezier Curve with divide and conquer algorithm and brute force algorithm<br>
<br>For Brute Force Algorithm, we use the equation for Bezier Curve. Then, algorithm will do (2^n)+1 iterations.<br>
In each iteration, the t value will be assigned as i/(2^n) with i is the number of iteration (starting from 0).<br>
<br>For Divide and Conquer Algorithm, we first find the middle point from every input points. Then, the algorithm <br>
will divide the points for the left side and the right side and recursively find the middle point for each side.<br>
In each recursion, the number of iteration will be decremented. When the iteration reach 0. It will return an empty list.


## File Structures
```
*
├───doc
├───src
│   └───__pycache__
└───test
```

## Requirement
- `Python` 3.X
- `Matplotlib`
- `Tkinter`

## Setup and Usage
1. Clone this repository using command `git clone https://github.com/slntkllr01/Tucil2_13522033_13522046.git`
2. Change to root directory using command `cd Tucil2_13522033_13522046`
3. Install python dependencies with `pip install -r requirements.txt`
4. Run the program `python3 src/main.py`
5. Fill the control points, iteration number, and press 'START'

## Authors

| ID       | Name                      |
| -------- | ------------------------- |
| 13522033 | Bryan Cornelius Lauwrence |
| 13522046 | Raffael Boymian Siahaan   |