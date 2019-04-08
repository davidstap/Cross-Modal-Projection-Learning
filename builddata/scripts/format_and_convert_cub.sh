#!/bin/bash
#
GPU_ID=$1
export CUDA_VISIBLE_DEVICES=$1

IMAGE_DIR=
TEXT_DIR=
OUTPUT_DIR=
DATASET_NAME=cub

echo "Building the TFRecords for CUB dataset..."

python convert_data.py \
    --image_dir=${IMAGE_DIR} \
    --text_dir=${TEXT_DIR} \
    --output_dir=${OUTPUT_DIR} \
    --dataset_name=${DATASET_NAME} \
    --min_word_count=3 \
    --train_shards=32

echo "Done!"
