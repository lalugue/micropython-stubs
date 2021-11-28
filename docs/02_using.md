(using-the-stubs)=
# Using the MicroPython stubs

In order to use the stubs you need to do a few things:  
## Clone or download a copy of the Micropython-Stubs repo
 1.  Download a copy of this repo , either via `git clone` or by download a zip file with it's contents
     - store this in a folder, for example 'next to' your software projects such as in `c:\develop\micropython-stubs`  
     this contains a `stubs` folder that contains all stubs
        ```
        git clone https://github.com/Josverl/micropython-stubs.git
        ```

 2. Over time you may want to periodically update this folder using
    ```
    git fetch && git pull
    ```

## Project configuration 
For each project where you want to use the stubs you need to configure vscode and any linters that you use to use the correct stubs.
This is not as complex as it seems initially, and once you have configured your first project, you can copy /paste that structure for other projects. 

## Create a symlink to the stubs folder  
Create a symlink to the `c:\develop\micropython-stubs\stubs` from inside your project.
This will allow you to reference the same stub files from multiple projects, and limit the space
needed. This a recommendation, and things work equally well if you copy or clone the `stubs` folder into your project.  
For details on how to create a symlink, please see : {ref}`create-symbolic-link`

## Quick start: 
Copy the [samples][] folder to your project  
This contains the template files you need to improve syntax highlighting wyioth Pylance and linting with pylint.

## Select which stub folders you need to reference
- The order will influence results. place the 'higher quality' folders first.
- Use forward slashes `/` rather than backslashes, also on Windows.
- for example for micropython 1.13 on an ESP32 select:
    1. "./src/lib",
    2. "all-stubs/cpython_patch",
    3. "all-stubs/mpy_1_13-nightly_frozen/esp32/GENERIC", 
    4. "all-stubs/esp32_1_13_0-103",


## Configure Pylance to use the selected stub folders  
This instructs the VSCode Pylance to consider your libs folder and the stubs for static code evaluation.
VSCode allows this configuration to be set on **_workspace_** or _user_ level. I prefer setting it per workspace as that allows different settings for different projects, but you could do either.
     
The below configuration is [Pylance][] specific
, and is simplified compared to the now deprecated 'Microsoft Python Language Server' 
     
    - use the {download}`samples/.VSCode/settings.json`  located in the sample folder
    - you can open this file in VSCode itself, or use the settings menu 
    - add the folders to the `python.autoComplete.extraPaths` section. 
    - it can be on a single line or split across lines. 
        - make sure it is a valid json array 

```json
    "python.languageServer": "Pylance",
    "python.analysis.autoSearchPath": true,
    "python.autoComplete.extraPaths": [
        "src/lib", 
        "all-stubs/cpython_patch", 
        "all-stubs/mpy_1_13-nightly_frozen/esp32/GENERIC", 
        "all-stubs/esp32_1_13_0-103",
    ]
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
```
 ## Pylint: Configure pylint to use the selected stub folders
This instructs pylint to insert the list of paths into `sys.path` before performing linting, thus allowing it to find the stubs and use them to better validate your code. 

- use the {download}`.pylintcr sample file <samples/.pylintrc>`.

- edit the line that starts with `init-hook=`  
        ``` ini
        init-hook='import sys;sys.path[1:1] = ["src/lib", "folder1","folder2", "folder3",];'
        ```
- replace the folders with your selection of stub folders.
**Note that in `.pylintrc` In this case they MUST be on a single line**
- the result should look like:
        ``` ini
        init-hook='import sys;sys.path[1:1] = ["src/lib", "all-stubs/cpython_patch","all-stubs/mpy_1_13-nightly_frozen/esp32/GENERIC", "all-stubs/esp32_1_13_0-103",];'
        ```


## Pymakr: Update pymakr.conf 
 
Depending on the tools and configuration you are using it may be needed to exclude the 
To avoid the "all-stubs" folder to be uploaded to your Micropython MCU

**Pymakr:**

 - add "all-stubs" to the "py_ignore" section

 ``` json 
{
    "address": "192.168.4.1",
    "username": "micro",
    "password": "python",
    "sync_folder": "",
    "open_on_start": true,
    "safe_boot_on_upload": false,
    "py_ignore": [
        "all-stubs",
        "pymakr.conf",
        ".vscode",
        ".gitignore",
        ".git",
        "project.pymakr",
        "env",
        "venv",
        ".venv"
    ],
    "fast_upload": false
}
 ```


## Restart VSCode  
VSCode must be restated for so that Pylance and linters such as Pylint to read the updated configuration.

You can use: 
- the `Developer: Reload Window` command.
- or stop / start the editor

[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
[samples]: https://github.com/josverl/micropython-stubs/tree/master/docs/samples