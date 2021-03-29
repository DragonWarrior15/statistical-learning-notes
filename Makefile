# use tabs for indentation when writing recipes
prob = probability-notes
prob_dir = tex_files/probability/

linalg = linear_algebra
linalg_dir = tex_files/linalg/

$(prob_dir)$(prob).pdf: $(prob_dir)$(prob).tex
	cd $(prob_dir); pdflatex $(prob).tex; cd ../../

$(linalg_dir)$(linalg).pdf: $(linalg_dir)$(linalg).tex
	cd $(linalg_dir); pdflatex $(linalg).tex; cd ../../

clean:
 	rm -rf $(prob_dir)$(prob).pdf
	rm -rf $(linalg_dir)$(linalg).pdf
