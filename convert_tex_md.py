import os

line1 = r"sed 's/\\newline/\\newline INSERTLINE/g' {}.tex | "
line2 = r"sed 's/\\\\/\\newline/g' | pandoc -f latex -t markdown --wrap=preserve --atx-headers | " +\
        r"sed 's/$$\\begin{aligned}/\\begin{align}/g' | " +\
        r"sed 's/\\end{aligned}\$\$/\\end{align}/g' | " +\
        r"sed 's/$$\\begin{gathered}/\\begin{align}/g' | " +\
        r"sed 's/\\end{gathered}\$\$/\\end{align}/g' | " +\
        r"sed 's/INSERTLINE/\n/g' |" +\
        r"sed 's/}_/}\\_/g' | sed 's/]_/]\\_/g' | sed 's/)_/)\\_/g' | " +\
        r"sed 's/{\*/{\\\*/g' | " +\
        r"sed 's/\\bm{/\\boldsymbol{/g' | " +\
        r"sed r'1 i\---\ntitle: '" + r'"ARMA(p,q) Process"' + r'\n---\n '
line3 = r"> {}.md"

def convert(folder):
    for root_dir, folder_list, file_list in os.walk(folder):

        # create the folder to store the files
        out_dir = root_dir.replace('tex_files', '_notes')
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

        # convert all the files
        for f in file_list:
            f_name, f_ext = os.path.splitext(f)
            if f_ext == '.tex':
                input_file = os.path.join(root_dir, f_name)
                output_file = os.path.join(out_dir, f_name)
                command = line1.format(input_file) + line2 + line3.format(output_file)
                print(input_file, output_file)
                os.system(command)

        # call the function again on the subfolders
        for f in folder_list:
            convert(os.path.join(root_dir, f))

if __name__ == '__main__':
    convert('tex_files/probability')
