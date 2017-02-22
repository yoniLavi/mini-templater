#!/usr/bin/env python

PAGES = [
    {
        'template': 'template.html',
        'output': 'index.html',
        'values': {
            'lang': 'en',
            'title': 'Landing Page',
            'heading': 'Welcome',
            'body': 'This is my cool website',
            'footer': 'Index Footer',
        },
    },
    {
        'template': 'template2.html',
        'output': 'contact.html',
        'values': {
            'lang': 'en',
            'title': 'Contact Me',
            'heading': 'Get In Touch',
            'body': 'me@example.com',
        },
    },
]


def render_template(template_path, output_path, values):
    """render a template with values in a dict"""
    with open(template_path) as template_file:
        template = template_file.read()

    rendered = template.format(**values)
    with open(output_path, 'w') as output_file:
        output_file.write(rendered)


def render_all(pages):
    """render multiple pages, each with its own template and values"""
    for page in pages:
        render_template(page['template'], page['output'], page['values'])


if __name__ == '__main__':
    render_all(PAGES)
