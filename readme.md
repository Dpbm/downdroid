# Download [Android X86](https://www.android-x86.org/) on your terminal

This python script list and download your required version of android-x86. To run this you need to have:

* python3
* pip (or similar)

## Commands

| command   | arguments               | 
| --------- | ----------------------- |
| --list    | all, versions, releases |
| --help    | -                       |
| --add     | {android-x86 version}   |

## Download a version

List Versions and releases

```bash
    downdroid --list versions
    downdroid --list releases
    or 
    downdroid --list all

```

select a version and then:

```bash
    downdroid --add {selected-version}
```

now, wait, in some minutes your file will be downloaded to you `Downloads` folder and you can use your android-x86

## DEV

if you want to run this by your own, clone this repo and run:

pipenv
```
    pipenv install
    pipenv shell
```

or with pip
```
    pip install -r requirements.txt
```

and finally run those commands with python3 as:


```bash
    python3 downdroid.py --list versions
    python3 downdroid.py --list releases
    python3 downdroid.py --list all
    python3 downdroid.py --add {selected-version}
```

or with executable commands listed on [Download a version](#download-a-version) 