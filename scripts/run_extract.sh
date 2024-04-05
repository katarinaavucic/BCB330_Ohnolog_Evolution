#!/bin/bash
#SBATCH --nodes=1
#SBATCH --gpus-per-node=a100:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100000
#SBATCH --time=5:55:00

#testing: salloc --time=0:40:0 --ntasks=1 --cpus-per-task 4 --mem=320G --gres=gpu:1 --account=def-jagillis


#module load python
module load cuda/11.4

#source /home/leon/virtual_env_test/bioembed/bin/activate
#python extract.py

source /home/vucickat/virtual_env/bioembed/bin/activate
/home/vucickat/virtual_env/bioembed/bin/python extract_embeddings.py
