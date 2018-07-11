1. chat.txt——>train.txt,把原数据集处理为QAQAQA+空行的形式。
2. 预处理：运行preProcess.py中的generate_raw_dataset()，seg_sen_for_word2vec()
3. 训练词向量：运行preProcess.py中的pre_train_word_embedding()
4. 运行word_embedding = load_word_embedding()，transfer_words_to_index(word_embedding.vocab_hash, with_unk=False)，transfer_data_format_for_scn(random_sampling_during_train=True, with_unk=False)
5. 训练网络：运行LCMN_and_SMN.py中的train_onehotkey()
6. 获得候选集：运行TFIDF_baseline下runModel.py
6. 准备问题文件：question50.txt——>Evalution_test50.pkl，运行preProcess.py中的word_embedding = load_word_embedding()，generate_test_pkl('data/test50.txt', 'data/result50.txt', 'data/result50.raw.pkl', 'data/result50.seg.pkl', word_embedding.vocab_hash, 'data/result50.index.pkl', with_unk=False)
7. 生成答案：运行LCMN_and_SMN.py中的gen_response()，在response.txt中。













