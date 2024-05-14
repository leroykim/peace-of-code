#!/bin/bash

if test -f ./Anaconda3-2024.02-1-Linux-x86_64.sh
then
    echo "Anaconda installation file exists."
else
    echo "Anaconda installation file does not exist. Downloading installation file:"
    wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh
fi

echo "Start Anaconda installation:"
bash Anaconda3-2024.02-1-Linux-x86_64.sh 
eval "$(/home/ubuntu/anaconda3/bin/conda shell.bash hook)"

echo "Create conda environment:"
conda create -n mhgpt python=3.11
conda activate mhgpt

echo "Upgrade pip:"
pip install --upgrade pip

echo "Install required packages:"
pip install huggingface_hub transformers datasets torch deepspeed peft bitsandbytes accelerate evaluate jupyter ipywidgets widgetsnbextension scikit-learn -U