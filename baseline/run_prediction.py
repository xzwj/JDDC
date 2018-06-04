# !/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import sys
import time

import numpy as np
from six.moves import xrange
import tensorflow as tf
import codecs
import logging

sys.path.append('./baseline/')

import data_utils
import seq2seq_model



def get_config(config_file='./baseline/seq2seq.ini'):
    try:
        from ConfigParser import ConfigParser
    except:
        from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(config_file)
    # get the ints, floats and strings
    _conf_ints = [(key, int(value)) for key, value in parser.items('ints')]
    _conf_floats = [(key, float(value)) for key, value in parser.items('floats')]
    _conf_strings = [(key, str(value) if key=='mode' else './baseline/'+str(value)) for key, value in parser.items('strings')]
    return dict(_conf_ints + _conf_floats + _conf_strings)

# We use a number of buckets and pad to the closest one for efficiency.
# See seq2seq_model.Seq2SeqModel for details of how they work.


def create_model(session, forward_only, gConfig, _buckets):
    """Create model and initialize or load parameters"""
    model = seq2seq_model.Seq2SeqModel(gConfig['enc_vocab_size'], gConfig['dec_vocab_size'], _buckets,
                                       gConfig['layer_size'], gConfig['num_layers'], gConfig['max_gradient_norm'],
                                       gConfig['batch_size'], gConfig['learning_rate'],
                                       gConfig['learning_rate_decay_factor'], forward_only=forward_only)

    # load pre_model
    if 'pretrained_model' in gConfig:
      model.saver.restore(session,gConfig['pretrained_model'])
      return model
    ckpt = tf.train.get_checkpoint_state(gConfig['working_directory'])
    if ckpt and ckpt.model_checkpoint_path:
      print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
      model.saver.restore(session, ckpt.model_checkpoint_path)
    else:
      print("Created model with fresh parameters.")
      session.run(tf.global_variables_initializer())
    return model


def run_prediction(input_file_path, output_file_path):
    _buckets = [(40, 50), (50, 60), (60, 70), (70, 90), (90, 110), (110, 150), (150, 190), (190, 250), (250, 300), (300, 350), (350,400), (400,1000), (1000, 2000)]
    gConfig = get_config()
    for k,v in gConfig.items():
        print(k,'  ',v)
    with tf.Session() as sess:
        # Create model structrue and load parameters
        model = create_model(sess, True, gConfig, _buckets)
        model.batch_size = 1  # We decode one sentence at a time.

        # Load vocabularies.
        enc_vocab_path = os.path.join(gConfig['working_directory'], "vocab%d.enc" % gConfig['enc_vocab_size'])
        dec_vocab_path = os.path.join(gConfig['working_directory'], "vocab%d.dec" % gConfig['dec_vocab_size'])

        enc_vocab, _ = data_utils.initialize_vocabulary(enc_vocab_path)
        _, rev_dec_vocab = data_utils.initialize_vocabulary(dec_vocab_path)

        # Decode from standard input.
        test_path = input_file_path
        result_path = output_file_path
        print(test_path)
        print(result_path)
        with codecs.open(result_path, mode='w', encoding='utf-8') as wf:
            wf.truncate()
            wf.close()
        with codecs.open(test_path, mode='r', encoding='utf-8') as rf:
            with codecs.open(result_path, mode='a', encoding='utf-8') as wf:
                try:
                    sentence = rf.readline()
                    while sentence:
                        #print("sentence: ", sentence)
                        sentence = sentence.rstrip(',')
                        # Get token-ids for the input sentence.
                        token_ids = data_utils.sentence_to_token_ids(sentence, enc_vocab)
                        #print("token_ids: ", token_ids)
                        # Which bucket does it belong to?
                        bucket_id = min([b for b in xrange(len(_buckets))
                                         if _buckets[b][0] > len(token_ids)])
                        #print("bucket_id: ", bucket_id)
                        # Get a 1-element batch to feed the sentence to the model.
                        encoder_inputs, decoder_inputs, target_weights = model.get_batch(
                            {bucket_id: [(token_ids, [])]}, bucket_id)

                        # Get output logits for the sentence.
                        _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                                         target_weights, bucket_id, True)

                        # This is a greedy decoder - outputs are just argmaxes of output_logits.
                        outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
                        #print("outputs: ", outputs)
                        # If there is an EOS symbol in outputs, cut them at that point.
                        if data_utils.EOS_ID in outputs:
                            outputs = outputs[:outputs.index(data_utils.EOS_ID)]
                        # Print out French sentence corresponding to outputs.（corresponding to:与...一致...）
                        result = "".join([tf.compat.as_str(rev_dec_vocab[output]) for output in outputs if
                                          tf.compat.as_str(rev_dec_vocab[output]) not in [",", "_UNK"]])
                        #print("result: ", result)
                        wf.write(result + '\n')
                        sentence = rf.readline()
                except Exception as e:
                    logging.error("test failure", e)
                finally:
                    rf.close()
                    wf.close()


if __name__ == '__main__':
    if len(sys.argv) !=3:
        print("file name, input_file_path, output_file_path")
    else:
        run_prediction(sys.argv[1], sys.argv[2])


