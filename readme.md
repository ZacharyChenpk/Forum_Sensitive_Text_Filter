### Requirement installation

Run "pip install -r requirements.txt"



## Algorithm Part

### Corpus Segmentation

1. Put "holes_github_dict.pkl" in directory "../"
2. Run "python word_seg.py"



### LSTM Model Training

1. Put "holes_github_dict.pkl"、"pids_github.pkl"、"deleted_pids.pkl" in directory "../"
2. Run through "LSTM_train.ipynb"



### Corpus statistics

1. Put "holes_github_dict.pkl"、"pids_github.pkl"、"deleted_pids.pkl" in directory "../"
2. Run through "statistics.ipynb"



## Local Demo

Note that the local demo is based on XMAPP( Apache+MySQL+PHP+PERL ).

1. Put the entire folder "./bbs" into "xmapp/htdocs"
2. Put all other files into the folder "xmapp/htdocs/bbs"
3. Execute "xampp-control.exe" and Start the "Apache" Module
4. Visit  http://localhost:8080/bbs/index.html  by your favorite explorer



## Server Demo and Background Interface

Directly visit  http://188.131.234.63:8080/  by your favorite explorer