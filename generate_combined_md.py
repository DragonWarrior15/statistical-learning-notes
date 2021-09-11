import os
import yaml
import re

with open('_data/navigation.yml', 'r') as f:
    config = yaml.safe_load(f)

# a global list for all links
global links_list
links_list = []

def add_to_list(item):
    # this function will allow recursive printing of all the subnavs
    if 'link' in item and item['link'] is not None:
        links_list.append(item['link'])
    if 'subnav' in item:
        for item2 in item['subnav']:
            add_to_list(item2)

# this loop will iterate over the main keys of the navigation.yml file
# for k in config:
for k in ['probability']:
    for item in config[k]:
        add_to_list(item)


# now process all elements of the list to correct the links
def correct_link(s):
    s = s.replace('html', 'md').replace('/notes', '_notes')
    return s

links_list = list(map(correct_link, links_list))
# generate the final output
out_stream = ""

# regex to remove the md headers
regex = re.compile('---\ntitle: .+\n---')

for i in range(len(links_list)):
    with open(links_list[i], 'r') as f:
        content = f.read()
        content = re.sub(regex, '', content)
        out_stream += content

# append the title and layout
out_stream = '---\ntitle: "Combined Notes"\nlayout: default_wo_nav\n---' + out_stream

with open('combined.md', 'w') as f:
    f.write(out_stream)
