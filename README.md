\# dot-abyss-scripts



Toolkit for extracting bundle files for Dot Abyss, translating and re-packaging them.



Quickstart:



```

// about 2GB DL, unless you already have bundles\_cache

python ./toolkit/download\_bundles.py --match .txt\_ --match r18-only-novel\_assets

// .bundle -> .json (/translations)

python ./toolkit/extract\_story.py

// .json -> .txt (/unity)

python ./toolkit/unity\_generate\_story\_assets.py

```



