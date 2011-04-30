SLIDES = slides


all:
	pdflatex $(SLIDES).tex
	pdflatex $(SLIDES).tex
	-rm *.aux *.log *.nav *.out *.snm *.toc *.vrb 

    
clean:
	-rm *.aux *.log *.nav *.out *.snm *.toc *.vrb


view:
	-evince $(SLIDES).pdf &

