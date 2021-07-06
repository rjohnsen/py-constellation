import argparse
import glob
import os

from jinja2 import Template

class IconMapper:
    def index(self, constellation_install_path: str) -> bool:
        search_path = os.path.join(
            constellation_install_path,
            "constellation/modules/ext/icons"
        )

        if os.path.isdir(search_path):
            const_list = self.__index_icons(search_path)
            return self.__create_constants(const_list)
        else:
            raise FileNotFoundError(
                f"Directory '{search_path}' not found!"
            )

    def __index_icons(self, search_path: str) -> list:
        dir_list = glob.glob(
            os.path.join(search_path, "**/*.png"),
            recursive = True
        )

        const_list = []

        for icon in dir_list:
            icon_set = icon.replace(search_path, "")\
                .replace(os.path.sep, "", 1)\
                .split(os.path.sep)

            for index in range(0, len(icon_set)):
                icon_set[index] = icon_set[index].replace(".png", "").capitalize()

            name = ("_".join(icon_set)).upper().replace("-", "_").replace("'", "_")
            value = ".".join(icon_set)

            if name[0].isdigit():
                name = f"NS{name}"

            const_list.append({
                "name": name,
                "value": value
                })

        return const_list

    def __create_constants(self, constants: list) -> bool:
        script_dir = os.path.abspath(os.path.dirname(__file__))

        template_path = os.path.join(
            script_dir,
            "templates",
            "icons.tpl"
        )

        with open(template_path, "r") as template_file:
            template = Template(template_file.read())
            rendered = template.render(constants=constants)

        output_dir = os.path.join(
            script_dir,
            "..",
            "kernel",
            "lib",
            "icons.py"
        )

        with open(output_dir, "w") as class_file:
            class_file.write(rendered)

        return True

def run():
    parser = argparse.ArgumentParser(
        description = "Index icons in Constellation-App installation directory"
    )

    parser.add_argument(
        "installation_path",
        metavar = "p",
        type =str,
        help = "Path to where Constellation-App is installed"
    )

    args = parser.parse_args()

    try:
        icon_mapper = IconMapper()
        icon_mapper.index(args.installation_path)
    except FileNotFoundError as err:
        print(f"ERROR: {err}")

if __name__ == "__main__":
    run()
