#!/usr/bin/env python

PAGES = {
    'index.html': {
        'lang': 'en',
        'title': 'Landing Page',
        'heading': 'Welcome',
        'body': 'This is my cool website',
        'footer': 'Index Footer',
    },
    'contact.html': {
        'lang': 'en',
        'title': 'Contact Me',
        'heading': 'Get In Touch',
        'body': 'me@example.com',
        'footer': 'Contact Footer',
    },
}


def render_template(template_path, output_path, values):
    """render a template with values in a dict"""
    with open(template_path) as template_file:
        template = template_file.read()

    rendered = template.format(**values)
    with open(output_path, 'w') as output_file:
        output_file.write(rendered)


def render_all(template_path, pages):
    """use a single template to render multiple pages with their own values"""
    for output_path, values in pages.items():
        render_template(template_path, output_path, values)


if __name__ == '__main__':
    render_all('template.html', PAGES)
