{% comment %}
This combined.md file will not work one level up as its unable to refer to \_notes folder.
The syntax given below also does not work
{% for item in site.data.navigation["probability"] %}
    {% capture curr_link %}{{ item.link | replace: "html", "md" | replace: "/notes/", "" }}{% endcapture %}
    {% include blank.html path=curr_link %}
{% endfor %}

where blank.html contains {% include_relative include.path %} because include functions cannot work with string data, that is returned after our replace statements used above.

Only solution feasible right now is to use python to iterate over the yaml and then generate the combined md file that jekyll can process.
{% endcomment %}
