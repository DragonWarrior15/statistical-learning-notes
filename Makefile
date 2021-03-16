# use tabs for indentation when writing recipes

prob = probability-notes
prob_dir = tex_files/probability/

$(prob_dir)$(prob).pdf: $(prob_dir)$(prob).tex
	cd $(prob_dir); pdflatex $(prob).tex; cd ../../

clean:
	rm -rf $(prob_dir)$(prob).pdf
