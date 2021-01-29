# use tabs for indentation when writing recipes

do = md_files/discrete_optimization/discrete_optimization_notes

$(do).pdf: $(do).md
	pandoc -f markdown -t latex --pdf-engine=pdflatex \
	-o $(do).pdf $(do).md

clean: 
	rm -rf $(dso).pdf
