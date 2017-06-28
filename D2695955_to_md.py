# coding: utf-8

COMPINDEX_JSON = 'D2695955.json'

def today():
    from time import gmtime, strftime
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def round_bracket(some_string):
    """Adds round brackets around a given string."""
    from string import Template
    return Template('($phrase)').substitute(phrase=some_string) 

def json2ordict(json_filename):
    """Given a JSON file, returns its contents as a Python ordered dictionary."""
    import json
    from collections import OrderedDict
    ord_dict = json.loads(open(json_filename).read(), object_pairs_hook=OrderedDict)
    return ord_dict

def ordict2selectn(ordered_dict):
    statementLabel = 'http://purl.org/ASN/schema/core/statementLabel'
    dcdescription = 'http://purl.org/dc/terms/description'
    selected_fields = []
    for item in ordered_dict:
        line = []
        if statementLabel in ordered_dict[item].keys():
            line.append(ordered_dict[item][statementLabel][0]["value"])
            line.append(item)
            line.append(ordered_dict[item][dcdescription][0]["value"])
            # line.append(item.replace("http://asn.desire2learn.com/resources/", "asn:"))
            selected_fields.append(line)
    return selected_fields

def mkmarkdown(selected_fields):
    just_lines = []
    prefix = """# LD4PE Competency Index

Version: %s <br>
View at: [https://dcmi.github.io/ldci/D2695955/](https://dcmi.github.io/ldci/D2695955/) <br>

| Code| Type          | Definition                                                    |
| --- | ------------- | --------------------------------------------------------------|
| A   | Topic Cluster |                                                               |
| B   | Topic         |                                                               |
| C   | Competency    | Tweet-length assertion of knowledge, skill, or habit of mind. |
| D   | Benchmark     | Action demonstrating accomplishment in related competencies.  |

Note: Hover over a code to see its URI.  Click on a code to visit its full definition on the [Achievement Standards Network](http://asn.desire2learn.com/resources/D2695955) website.

""" % today()
    just_lines.append(prefix)
    for line in selected_fields:
        line[1] = round_bracket(line[1])
        if line[0] == 'Topic Cluster':
            line[0] = '\n## [A:]'
        if line[0] == 'Topic':
            line[0] = '* [B:]'
        if line[0] == 'Competency':
            line[0] = '    * [C:]'
        if line[0] == 'Benchmark':
            line[0] = '        * [D:]'
        line[0] = ''.join([line[0], line[1]])
        del line[1]
        line = ' '.join(line)
        just_lines.append(line)
    return just_lines

def main():
    ordict = json2ordict(COMPINDEX_JSON)
    excerpt = ordict2selectn(ordict)
    lines = mkmarkdown(excerpt)
    with open('D2695955.md', 'w') as f:
        print("Writing", f)
        f.writelines("%s\n" % item for item in lines)

if __name__ == "__main__":
    main()
