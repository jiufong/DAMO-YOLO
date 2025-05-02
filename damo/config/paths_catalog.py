# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# Copyright (C) Alibaba Group Holding Limited. All rights reserved.
"""Centralized catalog of paths."""
import os

class DatasetCatalog(object):
    DATA_DIR = os.environ["SM_CHANNEL_TRAIN"]
    TRAIN_IMAGE_DIR = 'train/images'
    TRAIN_ANNOTATION_FILE = 'train/annotations/annotations.coco.txt'

    VALID_IMAGE_DIR = 'valid/images'
    VALID_ANNOTATION_FILE = 'valid/annotations/annotations.coco.txt'

    TEST_IMAGE_DIR = 'test/images'
    TEST_ANNOTATION_FILE = 'test/annotations/annotations.coco.txt'

    DATASETS = {
        'train_coco': {
            'img_dir': TRAIN_IMAGE_DIR,
            'ann_file': TRAIN_ANNOTATION_FILE
        },
        'valid_coco': {
            'img_dir': VALID_IMAGE_DIR,
            'ann_file': VALID_ANNOTATION_FILE
        },
        'test_coco': {
            'img_dir': TEST_IMAGE_DIR,
            'ann_file': TEST_ANNOTATION_FILE
        }
    }

    @staticmethod
    def get(name):
        if 'coco' in name:
            data_dir = DatasetCatalog.DATA_DIR
            attrs = DatasetCatalog.DATASETS[name]
            args = dict(
                root=os.path.join(data_dir, attrs['img_dir']),
                ann_file=os.path.join(data_dir, attrs['ann_file']),
            )
            return dict(
                factory='COCODataset',
                args=args,
            )
        else:
            raise RuntimeError('Only support coco format now!')
        return None
