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


# Parameter tuning: Experimenting with dropout
change：
在main.py中新增一个flag:'--ppl_log',用于开启train，valid，test ppl日志，新增datt_lineplot.py文件进行绘制train，valid ppl折线图
修改train.sh中的dropout参数0.0-0.5后，Train at least 5 language models with varying dropout settings (including a model without any dropout)
command：
修改train.sh中的dropout参数0.0-0.5后，命令行执行./scripts/train.sh，运行datt_lineplot.py绘制train，valid ppl折线图，命令行执行./scripts/generate.sh
观察迭代中的train，valid ppl和训练后test ppl可以发现，在最初几轮迭代，模型在训练集表现良好（低ppl），在验证集表现较差（高ppl），发生了过拟合。但是随着迭代次数的增加，训练集，验证集和测试集的ppl都下降到较低的数值，说明模型学到了一定通用规律。
观察训练结束后的train ppl可以发现，dropout=0.0时ppl最低，说明此时模型在训练集上的效果最好。观察验证结束后的ppl可以发现，不同dropout下的模型都获得了较低的ppl，说明由于epoch次数足够多，模型得到了充分的训练。如果只观察前20轮的训练，在保证模型训练热身结束的情况下，模型在dropout=0.0时效果最好。因此最优dropout参数应该为0.0。通过观察测试集的ppl，可以发现dropout=0.0时ppl最低模型效果最好。这是因为dropout是用来打破神经元之间的相关性，保证神经元独立训练，用来缓解过拟合。而模型没有出现过拟合问题，说明无需过度考虑神经元高相关性，高dropout对训练学到规律无利。在这种情况下让所有神经元参与训练，任务相对简单，模型表现更好。
观察可见，训练dropout=0.0最优ppl 1.4495622158096466）并进行文本生成发现：dropout=0.0时文本稍短，可读性更高，文本逻辑清晰，句法更完整，内容衔接更自然。
训练dropout=0.8（高ppl 80.67528262767686）的模型进行对比，dropout=0.8时文本长，文本可读性低，逻辑更混乱，句子结构松散，内容衔接更不流畅。
观察可见，对比训练集文本，dropout=0.0和0.8训练出来的模型都基于训练集文本词汇，词汇选择范围大致相同，但dropout=0.8文本可读性，连贯性不如训练文本，文本风格也偏离训练文本。而dropout=0.0可读性，连贯性，文本风格更符合训练文本。
总结：为了保证模型有最好的性能，我们应该选择dropout=0.0作为最优参数，保证ppl最低，模型学到了训练文本中的规律，生成更还原训练文本。



