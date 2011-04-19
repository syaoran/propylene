SLIDES = slides


all:
	pdflatex $(SLIDES).tex
	pdflatex $(SLIDES).tex
	-rm *.aux *.log *.nav *.out *.snm *.toc 

    
clean:
	-rm *.aux *.log *.nav *.out *.snm *.toc 


view:
	-evince $(SLIDES).pdf &

