# pyproject-template

[![Makefile CI](https://github.com/obar1/onepage_job_lister/actions/workflows/makefile.yml/badge.svg)](https://github.com/obar1/onepage_job_lister/actions/workflows/makefile.yml) 
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/obar1/onepage_job_lister?quickstart=1)

> (very) simple job website lister (in one page)
> I know very little about web - `feel free to add more to this repo`


![alt text](30d61c00-070a-4399-912d-eb295a14342e.png)
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