import os

import click
import inquirer
import tomli
from pyfiglet import Figlet

from .libs.cls import EPoetryCmds
from .libs.func import run_exec, run_scripts
from .libs.ppinfo import AKPPInfo

"""
author:     dapk@gmx.net
license:    MIT

using:      - https://python-inquirer.readthedocs.io/
            - https://dslackw.gitlab.io/colored/tables/colors/
"""

DEFAULT_LINE_LENGTH = 72


@click.command()
@click.argument("check_poetry_path", type=click.Path(exists=True), required=False)
def main(check_poetry_path):
    """
    This tool is used exclusively for Poetry projects.
    As soon as you have a poetry project in front of you in the console,
    you can use this tool to quickly find out which script commands the poetry project contains.

    usage:
    set path of poetry project, eg.\n
    $ poetry run ppcheck ~/poetry-project
    """
    print(
        Figlet(font="small").renderText("PPCHECK"),
        "Poetry pyproject.toml check!",
        end="",
    )
    try:
        # get/load pyproject.yaml
        if not check_poetry_path:
            check_poetry_path = os.getcwd()
        toml_file = os.path.join(
            os.path.expanduser(check_poetry_path), "pyproject.toml"
        )
        toml_dir = os.path.dirname(toml_file)
        pp_dict = {}
        if os.path.isfile(toml_file):
            with open(toml_file, "rb") as f:
                pp_dict = tomli.load(f)
        pl_dict = {}
        if os.path.isfile("poetry.lock"):
            with open("poetry.lock", "rb") as f:
                pl_dict = tomli.load(f)

        # get title
        print(AKPPInfo.GetInfo(pp_dict, pl_dict, True))
        _continue = True
        while _continue:
            print("")
            # choose scripts or stndards commands
            q = [
                inquirer.List(
                    "intro",
                    message="Make your choice:",
                    choices=[
                        "use poetry run scripts",
                        "use poetry commands",
                        "get poetry info",
                        "< exit",
                    ],
                    default="no",
                ),
            ]
            start_seq = inquirer.prompt(q)

            if start_seq["intro"] == "use poetry run scripts":

                # check scripts with inputs
                if AKPPInfo.AttrExists(pp_dict, dict, "tool", "poetry", "scripts"):
                    run_scripts(pp_dict, toml_dir, DEFAULT_LINE_LENGTH)
                else:
                    print(
                        AKPPInfo.ColorOut(
                            f"No script command(s) available in {os.path.basename(toml_file)}.",
                            fore_256="light_red",
                        )
                    )
            elif start_seq["intro"] == "use poetry commands":
                # choice what do you want?
                _choices = list(EPoetryCmds._value2member_map_)
                if os.path.isdir(os.path.join(toml_dir, "tests")) == False:
                    _choices.remove(EPoetryCmds.PYTEST.value)
                q = [
                    inquirer.Checkbox(
                        "exec_cmds",
                        message="Run commands at first by selecting with key 'space', press 'enter' for next",
                        choices=_choices,
                    ),
                ]
                tasks = inquirer.prompt(q)

                if len(tasks["exec_cmds"]) > 0:
                    for cmd in _choices:
                        if cmd in tasks["exec_cmds"]:
                            run_exec(
                                cmd,
                                toml_dir,
                                DEFAULT_LINE_LENGTH,
                            )
            elif start_seq["intro"] == "get poetry info":
                if len(pp_dict) > 0:
                    print(AKPPInfo.GetInfo(pp_dict, pl_dict))
                else:
                    print(
                        AKPPInfo.ColorOut(
                            f"No pyproject.toml available in {toml_dir}.",
                            fore_256="light_red",
                        )
                    )
            elif start_seq["intro"] == "< exit":
                _continue = False
            else:
                print(
                    AKPPInfo.ColorOut(
                        f"{toml_file} does not exist.", fore_256="light_red"
                    )
                )
                quit()

    except Exception as e:
        print(
            AKPPInfo.ColorOut(
                f"Something goes wrong or you aborted ppcheck!", fore_256="light_yellow"
            )
        )


if __name__ == "main":
    main()
