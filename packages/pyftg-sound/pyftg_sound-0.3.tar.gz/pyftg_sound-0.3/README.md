# pyftg-sound

## Prerequisites

__Install OpenAL Soft__

- For Linux (Ubuntu, other distros should be similar)
```
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install libopenal-dev makehrtf openal-info
```

- For MacOS
```
brew install openal-soft
echo 'export DYLD_LIBRARY_PATH="/opt/homebrew/opt/openal-soft/lib:$DYLD_LIBRARY_PATH"' >> ~/.zshrc
```

# For developer only
Please refer to this [link](https://twine.readthedocs.io/en/stable/).

1. Increase version number in pyproject.toml

1. Build project
```sh
python -m build
```
if the above command doesn't work due to ```no module named build``` error, install ```build``` library then try again
```sh
pip install build
```
3. Push project to pypi
```sh
twine upload dist/*
```
