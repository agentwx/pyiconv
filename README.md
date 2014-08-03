pyiconv
=======

A Text Enconding Detector and Conveter in Python

最近在Mac下写代码，一不小心就遭遇了编码问题，蛋疼的GBK陷阱，代码里面的中文注释全乱套了。本来不想自己造轮子的，但是iconv不具备自动探测文本编码的功能，这个很是痛点。Mac App Store里有一个[TextPal](https://itunes.apple.com/us/app/textpal/id677976033)，看起来很不错，但是好贵，要30大洋。

周末早上无聊就造了一会轮子，把代码写出来了，算是iconv的Python复刻，增加了自动识别编码的功能，就当是练习用Python解析命令行参数了。

用法在程序的help里，执行`pyiconv [-h|--help]`就能看到。

另外，我为了方便检测文本编码，使用了一个叫`chardet`的库。通过`pip install chardet`安装该依赖即可。

如果需要批量转换，可以结合`find`和`xargs`来使用，像这样子：

```
# 批量转换文本为UTF-8格式，覆盖原文件
find . -name "*.java" | xargs -I{} ./pyiconv -i {} -o {}
```

```
usage: pyiconv [-h] [-d] [-i FILE] [-o FILE] [-f ENCODING] [-t ENCODING] [-a]

detect and convert text encodings

optional arguments:
  -h, --help            show this help message and exit
  -d, --detect-only     detect the encoding of input end exit
  -i FILE, --input FILE
                        read from input file, or stdin instead
  -o FILE, --output FILE
                        write to output file, or stdout instead
  -f ENCODING, --from ENCODING
                        the encoding that convert from, if not given, auto
                        detect by default
  -t ENCODING, --to ENCODING
                        the encoding that convert to, if not given, UTF-8 by
                        default
  -a, --auto-detect     auto detect encoding of input
```