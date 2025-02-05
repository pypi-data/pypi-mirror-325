# Developer

### Update Packages

- `poetry update --dry-run`


### Basic How To Develop

- activate environment: `poetry shell`
    - from project root
- install app packages: `poetry install`
- run app (if you run the app - e.g. `ib build ...` from the poetry shell terminal you will be using the shell (dev) instance vs the globally installed instance)
- 'clean' local dev env: `poetry env remove $(which python)`
    - this is useful after you have removed a package and you want to 'clean' things


### Developer 'Testing'

Often you will want to try a build of another version to get local ib changes. You can easily do this by getting a poetry shell (see above) and then `cd` to the project you want to build and run `ib` as you need (so long as you stay in the poetry shell you will be using the local (dev) `ib` instance.


### Publishing to Pypi

- build: `poetry build`
- publish: `poetry publish --build`