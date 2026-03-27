# MT Exercise 2: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/marcamsler1/mt-exercise-02
    cd mt-exercise-02

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

## Change
### Finding an new dataset
In `download_data.sh`:
The download process from https://www.gutenberg.org/cache/epub/78260/pg78260.txt is logged to the file pg78260, and the downloaded text pg78260.txt is moved to $data/grimm/raw/tales.txt.

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh

## Change
### Parameter tuning: Experimenting with dropout
1.	In `main.py`:
Added --ppl_log flag: Enables logging of training, validation, and test perplexity 
Data storage: Uses pandas to record ppl and save them to separate csv files for each dataset.
2.	New `file datt_lineplot.py`:
Added functionality to plot training and validation PPL as line charts.

Modified the dropout parameter from 0.0 to 0.5 in `train.sh`:
Train at least five language models with different dropout rates, including one model that uses zero dropout.

Train a model:
    ./scripts/train.sh

Generate (sample) some text from a trained model with:
    ./scripts/generate.sh

Plot train and valid ppl:
    ./tools/pytorch-examples/word_language_model/data_lineplot.py





