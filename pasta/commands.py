import click
import os
from pasta.core import merge_pdfs_from_folder

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    if filename == ".":
        click.echo(os.path.abspath(filename))    
    click.echo(click.format_filename(filename))


@click.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--cover/--no-cover', '-c', 'is_title_page', default=False)
@click.option('--output', '-o', 'output_file_name', default="merged_output.pdf")
@click.option('--output-path', '-op', 'output_file_path')
def merge(directory, output_file_name, is_title_page, output_file_path):
    returned_path = merge_pdfs_from_folder(directory, output_file_name, is_title_page, output_file_path)
    click.echo(click.style(f"Merged PDF created successfully: {returned_path}", fg='green'))