# Detect the tex files in this folder and make them a target 
CONTENT:= $(shell echo *.tex)
TEXFILE:= $(shell echo ./Chapters/*.tex)
FRONT:= $(shell echo ./Front/*.tex)
BIB:= $(shell echo *.bib)

# You want latexmk to *always* run, because make does not have all the info.
# Also, include non-file targets in .PHONY so they are run regardless of any
# file of the given name existing.
.PHONY: all clean

# The first rule in a Makefile is the one executed by default ("make"). It
# should always be the "all" rule, so that "make" and "make all" are identical.
all : ucdthesis.pdf 

# MAIN LATEXMK RULE

# -pdf tells latexmk to generate PDF directly (instead of DVI).
# -pdflatex="" tells latexmk to call a specific backend with specific options.
# -use-make tells latexmk to call make for generating missing files.

# -interactive=nonstopmode keeps the pdflatex backend from stopping at a
# missing file reference and interactively asking you for an alternative.

ucdthesis.pdf : ./style/style.tex $(CONTENT) $(TEXFILE) $(BIB) $(FRONT) ucdthesis.tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode " -use-make ucdthesis.tex 

# You must have a bibliography file of the same file prefix 
# Use a symbolic link if you want to reuse bib file of another chapter
%.pdf : %.tex ./style/style.tex %.bib 	
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode " -use-make  

# make sure that .aux files are not removed since they tell latex 
# if a file has been changed or not!!
clean:
	latexmk -CA
