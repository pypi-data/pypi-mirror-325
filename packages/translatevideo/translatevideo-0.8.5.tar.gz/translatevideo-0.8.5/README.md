# translatevideo
```
-Bulk scans video files and transribes and translates video audio into srt subtitle files. Places srt files adjacent to video files.

--Runs on windows/linux/mac

--AMD/Intel/Nvidia GPU compatibility on windows/mac/linux using whisper CPP - Vulkan. Unlike whisper python which is only compatible with NVIDIA GPU's.

Currently only translates into English from other languages. Fastest when transcribing english audio.

Free, all processing is done locally. There is no api. Uses whisper cpp and argos translate to do the transribing and transcription.

```

## Install
```
- Download and install ffpmeg (https://www.ffmpeg.org/download.html)
	- Add bin path to enviornment path variable

- Download and install Whisper CPP. https://github.com/ggerganov/whisper.cpp.
	Windows:
	- For GPU support install the Vulkan SD and add to enviornment paths prior to compiling for Vulkan
	- Install w64devkit for C++ compiler. When compiling insert the flag -G "MinGW Makefiles"
		Example if compiling with Vulkan GPU support: cmake -B build -DGGML_VULKAN=1 -G "MinGW Makefiles"
	- After compiling download some models. See github.
	- Add whispercpp build/bin to windows enviornment variables

- Install TranslateVideo
	required: need python 3.8 or 3.9 (https://www.python.org/downloads/release/python-390/)
	pip install --upgrade translatevideo
	or
	pip install --upgrade  translatevideo@git+https://github.com/codexhound/translatevideo

	Or download and unzip the release for windows

- See examples for usage
	- Setup config.tsv (tab delimited, seperate options by tab)
	- Need to set an english only and nonenglish model as below in config
		C:\Software\whisper.cpp\models\ggml-large-v3-turbo-q5_0.bin	Model	nonenglishmodel
		C:\Software\whisper.cpp\models\ggml-small.en-q5_0.bin	Model	englishmodel
	- Need to set at least 1 videos path:
		D:\Share\VIDEOS\Movies	Movies	videopath
	- Need to set a temporary directory
		D:\Share\tempgensubtitles	Temp	tempdir

- Usage Command Line:
	translatevideo
	translatevideo --rescan ## this rescans directories for subtitles even if database file exists for video path
- Usuage Python
	import translatevideo.gensubtitles as gensubtitles
	gensubtitles.generatesubtitles()
	
```

# Future additions:
```

Translate into other languages besides English

Generate merged srt files (with the from language and the translated too language side by side

```





