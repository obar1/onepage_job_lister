# pyproject-template

> (very) simple job website lister (in one page)
> I know very little about web - `feel free to add more to this repo`

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/0to100?quickstart=1)

just open this repo in your GitHub Codespace and run the demo as:

## usage 

```bash
bash demo.sh
``` 

tune contents of 
```
def get_engines() -> dict:
```

## debug
> vs code 
use [here](.vscode/launch.json)
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python:Streamlit",
            "type": "debugpy",
            "request": "launch", 
            "module": "streamlit",
            "args": ["run", "${file}"]
        }
    ]
}

```
and use it as
![alt text](8428dd40-2c0a-4b47-9aa7-6ab3707ddc8d.png)

with braskpoints where needed :)
![alt text](8b734a43-685a-40c3-9801-947cb48b065f.png)