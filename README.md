# Template for UC Davis PhD thesis in Physics (Cosmology) 
files cloned from [Will Dawson](https://github.com/wadawson/dissertation) and others

# To compile the entire thesis 
```
$ make ucdthesis.pdf
```
which makes use of `latexmk` and `pdflatex`.  

# To compile individual chapter
```
$ make CHAPTER_NAME.pdf
```
The file `$CHAPTER_NAME.tex` needs to be at this current directory level.

# Organization of the latex files    
* files inside the `Front` folder control what goes on the cover of your thesis
* `ucdthesis.tex` - holds the main skeleton of the thesis.  
* Other written components of the thesis files are in different folders. 
* `style/style.tex` - formats the thesis latex and include differnet package dependencies

# Outline
* Chapter 1 - Introduction - Overview of how to analyze weak lensing signals
* Chapter 2 - paper of El Gordo 
* Chapter 3 - Illustris analysis   
* Chapter 4 - Cosmic shear mass mapping using Gaussian Processes    
* Chapter 5 - Summary 
