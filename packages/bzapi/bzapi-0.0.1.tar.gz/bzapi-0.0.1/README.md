# BoltzbitPythonAPI
Python API for talking to Boltzbit services.

## To generate

From `bz-backend/flowbackend` run the `build_bzapi.sh` script. This will generate the client code under `src/bz-api`

## To package
```
pip install --upgrade build
python3 -m build
```

## To publish
Increment the version in the .toml file. Delete the `dist` folder then re-package (`python3 -m build`) then:
```
pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

