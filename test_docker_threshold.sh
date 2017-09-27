#!/usr/bin/env bash
docker run -t -v /home/mehrtash/github/DeepInfer-Example-Model/models/threshold/sample/:/data \
       deepinfer/example\
       --ModelName threshold \
       --InputVolume /data/MRHead.nrrd \
       --OutputLabel /data/MRHead-label.nrrd
