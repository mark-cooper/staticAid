#!/usr/bin/env python

from ConfigParser import ConfigParser
from json import load
from os import listdir
from os.path import dirname, exists, join, splitext


configFilePath = join(dirname(__file__), 'local_settings.cfg')
config = ConfigParser()
config.read(configFilePath)

def get_json(filename):
    with open(join(src, filename)) as data_file:
        parsed_data = load(data_file)
    return parsed_data

def get_note(note):
    if note["jsonmodel_type"] == 'note_multipart':
        content = note["subnotes"][0]["content"]
    else:
        content = note["content"]
    return content

def make_pages(src, category):
    if exists(src):
        for f in listdir(src):
            if f.endswith(".json"):
                data = get_json(f)

                identifier = splitext(f)[0]
                if category == 'objects':
                    title = data["display_string"].strip().replace('"', "'")
                else:
                    title = data["title"].strip().replace('"', "'")
                raw_description = ''
                description = ''

                notes = data["notes"]
                for note in notes:
                    if note.has_key("type"):
                        if note["type"] == 'abstract':
                            raw_description = get_note(note)
                        elif note["type"] == 'scopecontent':
                            raw_description = get_note(note)
                        elif note["type"] == 'bioghist':
                            raw_description = get_note(note)
                        else:
                            pass
                    else:
                        pass
                description = (raw_description.strip().replace('"', "'")[:200] + '...') if len(raw_description) > 200 else description

                # see Gruntfile.js:
                # jekyll > build > options > src: 'build/page_data/',
                filename = join('build', 'page_data', category, '%s.html' % identifier)
                with open(filename, 'w+') as new_file:
                    new_file.write("---\nlayout: %s\n" % category)
                    new_file.write("title: \"%s\"\n" % title.encode('utf-8'))
                    new_file.write("id: %s\n" % identifier)
                    new_file.write("type: %s\n" % category)
                    new_file.write("permalink: %s/%s/\n" % (category, identifier))
                    new_file.write("description: \"%s\"\n" % description.encode('utf-8'))
                    new_file.write("---")
                    new_file.close

# ex: {people: _data/people}
for category, src in config.items('Destinations'):
    make_pages(src, category)
