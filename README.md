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

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh


# Findings
https://www.gutenberg.org/cache/epub/78260/pg78260.txt
这是我选择的数据集，收录于古腾堡计划的公共版权英文作品，是一本充满英式幽默风格的小说。
这本书的特点在于大量使用英国上层社会相关词汇，也包括古英语和或文学化词汇，也加入了口语化的词汇和大量形象化比喻。
在句法上多从句，插入语和描述性修饰，长句 + 突然短句）
因此模型学到的应该会是小说体裁，并高度口语化和文学化混合的生成模式，输出文本应既像聊天，又带书面修辞的手法


