import pandas as pd
import matplotlib.pyplot as plt

df_train = pd.read_csv('/Users/yangwen/mt-exercise-02/tools/pytorch-examples/word_language_model/train_data.csv')
df_valid = pd.read_csv('/Users/yangwen/mt-exercise-02/tools/pytorch-examples/word_language_model/valid_data.csv')

fig,(as1,as2,as3) = plt.subplots(1,3,figsize=(10,6))
for colu in df_train.columns[1:]:
    as1.plot(range(1,df_train.shape[0]+1), df_train[colu], label=colu, linestyle='-')
as1.legend()
as1.set_title('Training Perplexity')
as1.set_xlabel('Epoch')
as1.set_ylabel('Training Ppl')
#as1.tick_params('x',rotation=45)
as1.grid(True)

for colu in df_valid.columns[1:]:
    as2.plot(range(1,df_valid.shape[0]+1), df_valid[colu], label=colu, linestyle='-')
as2.legend()
as2.set_title('Validation Perplexity')
as2.set_xlabel('Epoch')
as2.set_ylabel('Validation Ppl')
# as2.set_xticks(range(1,df.shape[0]+1))
as2.grid(True)

for colu in df_valid.columns[1:]:
    as3.plot(range(30,df_valid.shape[0]+1), df_valid[colu][29:], label=colu, linestyle='-')
as3.legend()
as3.set_title('Validation Perplexity After 30 Epoches')
as3.set_xlabel('Epoch')
as3.set_ylabel('Validation Ppl')
# as2.set_xticks(range(1,df.shape[0]+1))
as3.grid(True)

plt.tight_layout()
plt.savefig('train_ppl_Val_ppl_val_ppl_after_30epoches_ppl.jpg', dpi=300)  
plt.show()