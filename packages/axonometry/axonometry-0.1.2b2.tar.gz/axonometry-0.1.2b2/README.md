<!--
SPDX-FileCopyrightText: 2024 Julien Rippinger

SPDX-License-Identifier: CC-BY-4.0
-->

[![pypi](https://img.shields.io/pypi/v/axonometry?label=PyPI&logo=pypi&color=blue)](https://pypi.org/project/axonometry/)
[![license](https://img.shields.io/pypi/l/axonometry?color=blue)](https://axonometry.readthedocs.io/en/latest/license.html)
[![reuse-status](https://api.reuse.software/badge/codeberg.org/mononym/axonometry)](https://api.reuse.software/info/codeberg.org/mononym/axonometry)
[![rtd-status](https://img.shields.io/readthedocs/axonometry?label=Read%20the%20Docs&logo=read-the-docs)](https://axonometry.readthedocs.io/en/latest/)
[![pipeline-status](https://ci.codeberg.org/api/badges/14144/status.svg?branch=beta)](https://ci.codeberg.org/repos/14144/branches/beta)

#### Contents

* [What is _axonometry_?](#what-is-_axonometry_)
* [How does it work?](#how-does-it-work)
* [Examples](#examples)
* [Installation](#installation)
* [Contributing](#contributing)
* [License](#license)

## What is _axonometry_?

_axonometry_ is a scripting library to generate axonometric drawings. It implements axonometric projection operations common in the context of architectural representation. _axonometry_ enables the exploration of three dimensional representation through the definition of projecitonal operations. Think of it as a tool for generative drawing art, oriented towards architectutral representation.

_axonometry_ is the top of the iceberg of a PhD project at the [AlICe laboratory](https://alicelab.be). It is the result of a practical experimentations around questions related to the field of architectural representation, the role of computer graphics and drawing practices.

Check the [documentation](https://axonometry.readthedocs.io/en/latest/) for a more thorough introduction to _axonometry_.

## How does it work?

_axonometry_ is basically a wrapper for [compas](https://compas.dev) geometry objects and produces SVG vector files with the help of [vpype](https://vpype.readthedocs.io).

## Examples

You don't like computers and just want an axonometry layout and continue drawing by hand:
```python
import axonometry as axo
my_axo = axo.Axonometry(15,45)
my_axo.save_svg("new_drawing")
```

## Installation

Detailed installation instructions are available in the [latest documentation](https://axonometry.readthedocs.io/en/latest/install.html).

TL;DR:
- Python 3.12 is recommended, but _axonometry_ is also compatible with Python 3.10 and 3.11.
- _axonometry_ is published on the [Python Package Index](https://pypi.org/project/axonometry/).

```bash
python -m pip install axonometry
```

## Contributing

All type of feedback is welcome. Contributions can take any form and do not necessarily require software development skills! Check the
[Contributing section](https://axonometry.readthedocs.io/en/latest/contributing.html) of the documentation for more
information.

## License

This project is licensed under the GPLv3 License - see the [LICENSE](./LICENSES/GPL-3.0-or-later.txt) file for details. Check the
[Liceneses section](https://axonometry.readthedocs.io/en/latest/license.html) for more information.
