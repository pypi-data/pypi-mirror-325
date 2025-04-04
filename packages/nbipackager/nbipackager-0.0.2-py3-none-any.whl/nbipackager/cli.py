# packager/cli.py
import click
from .config import PackagerConfig
import os

@click.group()
@click.pass_context
def main(ctx):
    """Package manager for Singularity images."""
    ctx.obj = PackagerConfig()

# -=== [ addpackage ] ===-
@main.command()
@click.option('--image', '-i', required=True, help='Path to Singularity image')
@click.option('--name', '-n', required=True, help='Package name')
@click.option('--version', '-v', required=True, help='Package version')
@click.pass_obj
def addpackage(config, image, name, version):
    """Add a singularity package to the configuration."""
    from .commands.addpackage import add_package_command
    
    success, error = add_package_command(config, image, name, version)
    if not success:
        click.echo(f"Error: {error}", err=True)
        exit(1)
    click.echo(f"Successfully added {name} version {version} to configuration")

# -=== [ scanpackages ] ===-
@main.command()
@click.option('--dir', '-d', help='Directory to scan (uses config default if not provided)')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing entries')
@click.option('--verbose',  is_flag=True, help='Enable verbose output')
@click.pass_obj
def scanpackages(config, dir, force, verbose):
    """Scan for packages in the singularity path."""
    from .commands.scanpackages import scan_packages_command
    
    try:
        added, skipped, skipped_packages = scan_packages_command(config, dir, force)
        click.echo(f"Successfully added {added} new package(s)")
        if skipped:
            click.echo(f"Skipped {skipped} existing package(s):")
            for key, path in skipped_packages.items():
                click.echo(f"  {key}: {path}")
            click.echo("\nUse --force to overwrite existing entries")
    except click.ClickException as e:
        click.echo(f"Error: {str(e)}", err=True)
        exit(1)

# -=== [ makebundle ] ===-
@main.command()
@click.option('--name', '-n', required=True, help='Bundle name')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing entries')
@click.option('--verbose', is_flag=True, help='Enable verbose output')
@click.argument('packages', nargs=-1)  # This allows any number of positional arguments
@click.pass_obj
def makebundle(config, name: str, packages: tuple, force: bool = False, verbose: bool = False):
    """Create a new bundle.
    
    Optional PACKAGES can be specified in the format PACKAGE=VERSION
    
    Example: packager makebundle -n mybundle package1=1.0.0 package2=2.0.0
    """
    from .commands.makebundle import make_nbi_bundle_command
    
    # Parse package arguments
    package_versions = {}
    for pkg in packages:
        try:
            package, version = pkg.split('=')
            package_versions[package] = version
        except ValueError:
            click.echo(f"Error: Invalid package format '{pkg}'. Use PACKAGE=VERSION format.")
            exit(1)
    
    status, message = make_nbi_bundle_command(config, name, force, verbose, package_versions)
    if status == "success":
        click.echo(message)
    elif status == "exists":
        click.echo(f"Error: {message}")
        click.echo("Use --force to overwrite existing entries")
        exit(1)
    else:  # status == "error"
        click.echo(f"Error: {message}")
        exit(1)

# -=== [ addtobundle ] ===-
@main.command()
@click.option('--name', '-n', help='Bundle name (defaults: $NBI_PACKAGE)')
@click.option('--package', '-p', required=True, help='Package name')
@click.option('--version', '-v', required=True, help='Package version')
@click.option('--force', '-f', is_flag=True, help='Overwrite existing entries')
@click.option('--verbose', is_flag=True, help='Verbose')
@click.argument('aliases', nargs=-1)
@click.pass_obj
def addtobundle(config, name, package, version, force, verbose, aliases):
    """Add a package to an existing bundle.
    
    Optional ALIASES can be specified as additional names for the package.
    
    Example: packager addtobundle -n mybundle -p bwa -v 0.7.17 bwasw bwaaln
    """
    from .commands.addtobundle import add_to_bundle_command
    if name is None:
        name = os.environ.get('NBI_PACKAGE')
        if name is None:
            click.echo("Error: Bundle name must be provided either via --name option or $NBI_PACKAGE environment variable", err=True)
            exit(1)
    status, message = add_to_bundle_command(config, name, package, version, force, verbose, aliases)
    if status == "success":
        click.echo(message)
    else:
        click.echo(f"Error: {message}")
        exit(1)

# -=== [ findpackage ] ===-
@main.command()
@click.argument('search_term')
@click.option('--verbose', is_flag=True, help='Enable verbose output')
@click.pass_obj
def find(config, search_term, verbose):
    """Search for packages matching SEARCH_TERM.
    
    Example: packager findpackage fastq
    """
    from .commands.findpackage import find_package_command
    
    matches = find_package_command(config, search_term, verbose)
    
    if not matches:
        click.echo(f"No packages found matching '{search_term}'")
        exit(0)
    
    click.echo(f"Found {len(matches)} matching package(s):")
    max_name_len = max(len(name) for name, _ in matches) if matches else 0
    
    for name, version in matches:
        # Format output with aligned versions
        click.echo(f"  {name:<{max_name_len}} = {version}")


if __name__ == '__main__':
    main()