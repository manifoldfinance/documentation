## `manifold finance documentation`

### development

#### generate `mkdocs.yml` nav

```python3
$ python3 gen-menu.py
```
This will auto-populate the `mkdocs.yml` file.

> Note: Remove everything out of the `mkdocs.yml` file except the `nav:` items before running

##### deployment

```sh
mkdocs build --clean
```

```sh
mkdocs gh-deploy
```

#### support & feedback

[Visit our discourse forums](https://forums.manifoldfinance.com)


### license

SPDX-License-Identifier: MIT
Documentation: CC-NC-2.5


