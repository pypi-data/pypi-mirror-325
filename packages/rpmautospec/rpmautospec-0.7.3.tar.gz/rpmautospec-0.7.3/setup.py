# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpmautospec', 'rpmautospec.subcommands']

package_data = \
{'': ['*']}

install_requires = \
['babel>=2.8,<3.0',
 'click-plugins>=1.1.1,<2.0.0',
 'click>=8,<9',
 'pygit2>=1.4.0,<2.0.0',
 'rpm',
 'rpmautospec_core>=0.1.4,<0.2.0']

entry_points = \
{'console_scripts': ['rpmautospec = rpmautospec.cli:cli'],
 'rpmautospec.cli': ['calculate-release = '
                     'rpmautospec.subcommands.release:calculate_release',
                     'convert = rpmautospec.subcommands.convert:convert',
                     'generate-changelog = '
                     'rpmautospec.subcommands.changelog:generate_changelog',
                     'process-distgit = '
                     'rpmautospec.subcommands.process_distgit:process_distgit']}

setup_kwargs = {
    'name': 'rpmautospec',
    'version': '0.7.3',
    'description': 'A package and CLI tool to generate RPM release fields and changelogs.',
    'long_description': 'Automatically Maintain RPM Release Fields and Changelogs\n========================================================\n\n.. note::\n\n   Documentation is available at\n   https://fedora-infra.github.io/rpmautospec-docs/\n\nThis project hosts the ``rpmautospec`` python package and command line tool, which automatically\ncalculates release numbers and generates the changelog for RPM packages from their dist-git\nrepository.\n\nDependencies:\n\n* Python >= 3.9\n* babel >= 2.8\n* pygit2 >= 1.4\n* rpmautospec-core >= 0.1.4\n\nOptional dependencies:\n\n* poetry >= 1.2 (if using poetry to install)\n\nGeneral\n-------\n\nThe command line tool ``rpmautospec`` can calculate the release and generate the changelog from the\nspec file of an RPM package and its git history, as well as process that spec file into a form which\ncan be consumed by rpmbuild, and convert traditional spec files to using these automatic features.\n\n\nRunning the Examples\n--------------------\n\nTo run the examples with the ``rpmautospec`` command line tool from this repository (as opposed to a\nversion that may be installed system-wide), you can install it into a Python virtualenv, managed\neither manually or by the ``poetry`` tool. For the latter, substitute running ``rpmautospec`` by\nrunning ``poetry run rpmautospec`` below.\n\nTo install the package, run this (optionally, within an activated virtualenv)::\n\n  poetry install\n\nThe examples work with the ``guake`` package. Clone its dist-git repository this way, in a location\nof your choice, and then change into the repository worktree::\n\n  fedpkg clone guake\n  cd guake\n\n\nGenerate the Changelog\n^^^^^^^^^^^^^^^^^^^^^^\n\nThis will generate the changelog from the contents of the repository and the history::\n\n  rpmautospec generate-changelog\n\n\nCalculate the Release Field Value\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\nThis will generate the numerical value for the release field from the number of commits since the\n``Version`` field was last updated::\n\n  rpmautospec calculate-release\n\n\nThe ``rpmautospec`` Python module is not thread/multiprocess-safe\n-----------------------------------------------------------------\n\n``rpmautospec`` redefines some RPM macros when parsing spec files or expanding macros.  These\ndefinitions are only relevant to the current instance of the ``rpm`` module imported in Python, they\nare not persistent.  ``rpmautospec`` cleans those definitions when it is done by reloading the RPM\nconfiguration.\n\nHowever, if another thread or process running from the same Python interpreter instance\nattempts to change or expand RPM macros in the meantime, the definitions might\nclash and the cleanup might override other changes.\n\nIn case this breaks your use case, please open an issue to discuss it.\nWe can cooperate on some locking mechanism.\n\n\nContributing\n------------\n\nYou need to be legally allowed to submit any contribution to this project. What this\nmeans in detail is laid out in the file ``DCO.txt`` next to this file. The mechanism by which you\ncertify this is adding a ``Signed-off-by`` trailer to git commit log messages, you can do this by\nusing the ``--signoff/-s`` option to ``git commit``.\n\n\n---\n\nLicense: MIT\n',
    'author': 'Pierre-Yves Chibon',
    'author_email': 'pingou@pingoured.fr',
    'maintainer': 'Fedora Infrastructure',
    'maintainer_email': 'admin@fedoraproject.org',
    'url': 'https://github.com/fedora-infra/rpmautospec',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
