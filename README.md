# Configura

Configura is a Python configuration library that enables you to convert a folder of .json files into an easily accessible configuration folder.

## Usage

Say you have a folder with the following structure:

```
config_folder /
    main.json
    server.json
    misc.json
```

You can use configura to access those configurations like so:

```python
from configura import config

# Optionally, set your config folder here
# base_path defaults to "./config" so if your folder is named config, you don't have to modify this at all
config.base_path = "./config_folder"

# Print a misc.json as a dictionary
print(config.misc)
...

# Access data inside the misc.json as a dictionary
print(config.misc["model"])
```

# LICENSE

MIT License

Copyright (c) 2023 Philippe Mathew

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without plimitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
