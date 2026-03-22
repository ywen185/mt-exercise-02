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
我选择的样本文本来自《Big Jack, and other true stories of horses》，属于儿童文学类型的动物故事。
文本以叙事为主，讲述人与动物的互动经历。文本具有明显的拟人化特点。
从句法结构来看，文本长短句交替使用，复合句和插入语丰富。
基于训练集，我假设模型学会这些文本特征并对生成有明显影响：
1. 模型倾向生成长复合句和插入语丰富的句子，以便模仿原文的句法特点。
2. 模型倾向生成情感丰富且画面感强的文本，和拟人化和情感描写，以便模仿原文儿童文学故事文本的风格。

但是在对于真实生成文本（1000 words）的观察后，我发现：
1. 生成文本语句略显混乱，破碎且跳跃，无法做到完全通顺的逐句人工理解。这是因为模型训练优秀，学会了训练集的一个分布特征，即大量使用插入语。但是可能由于训练数据不足，模型无法掌握插入语的正确用法。
2. 可以看出训练集对生成文本的影响，符合上面假设。如模型确实倾向生成长复合句和插入语丰富的句子，以便模仿原文的句法特点。也倾向生成情感丰富，画面感强的人物和动物互动，和拟人化和情感描写，模仿原文儿童文学故事文本的风格。





