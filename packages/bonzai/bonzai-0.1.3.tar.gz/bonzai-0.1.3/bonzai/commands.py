import click
import json
from bonzai.core import generate_directory_tree, visualize_tree, get_relative_path


@click.command(name="tree")
@click.argument('directory_path', type=click.Path(exists=True))
@click.option('--show-permissions', '--perm', '-p', is_flag=True, help="Include file permissions in the tree output.")
@click.option('--show-size', '--size', '-s', is_flag=True, help="Include file size in the tree output.")
def tree(directory_path: str, show_permissions: bool, show_size: bool) ->None:
    """
    Displays the directory tree structure for the given DIRECTORY_PATH.
    """
    generated_tree_structure = generate_directory_tree(directory_path,
        show_permissions=show_permissions, 
        show_size=show_size
    )
    tree_output = visualize_tree(generated_tree_structure)
    click.echo(tree_output)


@click.command(name="jtree")
@click.argument('json_file', type=click.File('r'))
@click.option('-p', '--show-permissions', is_flag=True, help="Include file permissions in the tree output.")
@click.option('-s', '--show-size', is_flag=True, help="Include file size in the tree output.")
def json_tree(json_file: click.File, show_permissions: bool, show_size: bool) -> None:
    """
    Display the directory tree structure from a JSON file.

    JSON_FILE: Path to the JSON file containing the directory tree structure.
    """
    # Load the JSON file
    json_tree_object = json.load(json_file)

    # Visualize the tree from the JSON object
    tree_output = visualize_tree(
        json_tree_object,
        show_permissions=show_permissions,
        show_size=show_size
    )
    click.echo(tree_output)


@click.command(name="save-tree")
@click.argument('directory_path', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path(writable=True))
def save_tree(directory_path: str, output_file: str) -> None:
    """
    Saves the directory tree structure of DIRECTORY_PATH as a JSON file.

    Args:
        directory_path (str): The path to the directory to generate the tree for.
        output_file (str): The file path where the JSON output will be saved.
    """
    # Validate that the output file has a .json extension
    if not output_file.endswith('.json'):
        raise click.BadParameter("Output file must have a '.json' extension.")
    
    # Generate the directory tree
    generated_tree_structure = generate_directory_tree(directory_path)

    # Write the JSON to the specified file
    with open(output_file, 'w') as json_file:
        json.dump(generated_tree_structure, json_file, indent=4)

    click.secho(f"Directory tree structure saved to '{output_file}'.", fg='green')



@click.command(name="relative")
@click.argument('destination_path', type=click.Path(exists=True))
@click.argument('base_path', type=click.Path(exists=True))
def relative(destination_path: str, base_path: str) -> None:
    click.echo(get_relative_path(destination_path, base_path))