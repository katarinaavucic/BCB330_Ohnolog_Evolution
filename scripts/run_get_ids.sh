#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=24
#SBATCH --mem=100000
#SBATCH --time=1:55:00

#testing: salloc --time=0:40:0 --ntasks=1 --cpus-per-task 8 --mem=320G --account=def-jagillis


module load cuda/11.4

source /home/vucickat/virtual_env/bioembed/bin/activate
/home/vucickat/virtual_env/bioembed/bin/python get_uniprot_ids.py

