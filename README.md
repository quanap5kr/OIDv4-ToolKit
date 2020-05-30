# OIDv4-ToolKit
Download image from Open Image Dataset v4 https://storage.googleapis.com/openimages


## Clone this repository
```
git clone https://github.com/quanap5kr/OIDv4-ToolKit.git
```

## Install the required packages
```
pip3 install -r requirements.txt
```

Peek inside the requirements file if you have everything already installed. Most of the dependencies are common libraries.

## Configuration to download image from OID

Use the following statement.

```
python3 main.py downloader --classes Apple Orange --type_csv train
```

## Change label file to YOLO format

```
python3 convert_annotation.py
```

## Check by visualization tool !(https://github.com/tzutalin/labelImg)
