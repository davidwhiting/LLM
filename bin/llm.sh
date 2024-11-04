#!/bin/bash

# These options are available for all models. They mostly take a floating point value between 0.0 and 1.0.
#
# - temperature: A higher temperature encourages more diverse outputs, while a lower temperature produces more deterministic outputs.
# - top_p: At each step, we select tokens from the minimal set that has a cumulative probability exceeding this value.
# - repetition_penalty: Controls the likelihood of the model generating repeated texts.
# - max_gen_len: Takes an integer, which controls the maximum length of the generated text.

llm -m llama2 \
  -o temperature 0.5 \
  -o top_p 0.9 \
  -o repetition_penalty 0.9 \
  -o max_gen_len 100 \
  'five names for a cute pet ferret'
