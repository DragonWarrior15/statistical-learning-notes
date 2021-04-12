# use tabs for indentation when writing recipes
# run the command twice to build the toc and links as well
prob = probability-notes
prob_dir = tex_files/probability/

linalg = linear_algebra
linalg_dir = tex_files/linalg/

.Phony: clean .FORCE

.FORCE:# a dummy file so that build of all pdf is forced everytime

$(prob_dir)$(prob).pdf: .FORCE
	cd $(prob_dir); pdflatex $(prob).tex; cd ../../
	cd $(prob_dir); pdflatex $(prob).tex; cd ../../

$(linalg_dir)$(linalg).pdf: .FORCE
	cd $(linalg_dir); pdflatex $(linalg).tex; cd ../../
	cd $(linalg_dir); pdflatex $(linalg).tex; cd ../../

clean:
	rm -rf $(prob_dir)$(prob).pdf
	rm -rf $(linalg_dir)$(linalg).pdf

install:
	sudo apt-get update
	sudo apt-get install pandoc
	sudo apt-get install texlive-latex-recommended
	sudo apt-get install texlive-latex-extra

# sed 's/\\newline/\\newline INSERTLINE/g' _notes/linalg/vector_spaces/orthogonal.tex | \
# sed 's/\\\\/\\newline/g' | pandoc -f latex -t markdown --wrap=preserve --atx-headers | \
# sed 's/$$\\begin{aligned}/\\begin{align}/g' | \
# sed 's/\\end{aligned}\$\$/\\end{align}/g' | sed 's/INSERTLINE/\n/g' |\
# sed 's/}_/}\\_/g' | sed 's/]_/]\\_/g' | sed 's/)_/)\\_/g' |\
# sed '1 i\---\ntitle: "Orthogonal and Orthonormal Vectors"\n---\n' \
# > _notes/linalg/vector_spaces/orthogonal.md

