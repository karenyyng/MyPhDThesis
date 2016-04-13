# Detect the tex files in this folder and make them a target 
PROJECT:= $(shell echo *.tex)

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

ucdthesis.pdf : $(PROJECT)
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode " -use-make ucdthesis.tex 

%.pdf : %.tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode " -use-make $< 

# make sure that .aux files are not removed since they tell latex 
# if a file has been changed or not!!
clean:
	rm *.bbl *.fls *.fdb_latexmk *.log *.blg *.out *.pdf
