# use tabs for indentation when writing recipes

linalg = linear_algebra
linalg_dir = tex_files/linalg/

$(linalg_dir)$(linalg).pdf: $(linalg_dir)$(linalg).tex
	cd $(linalg_dir); pdflatex $(linalg).tex; cd ../../

clean:
	rm -rf $(linalg_dir)$(linalg).pdf
