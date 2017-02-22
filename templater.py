#!/usr/bin/env python

VALUES = {
    'lang': 'en',
    'title': 'This is the Title',
    'heading': 'This is the Heading',
    'body': 'This is the Body',
    'footer': 'This is the Footer',
}


def render_template(template_path, output_path, values):
    """render a template with values in a dict"""
    with open(template_path) as template_file:
        template = template_file.read()

    rendered = template.format(**values)
    with open(output_path, 'w') as output_file:
        output_file.write(rendered)


if __name__ == '__main__':
    render_template('template.html', 'index.html', VALUES)
