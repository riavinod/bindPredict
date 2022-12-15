#!/bin/bash

#SBATCH --mail-user=ria_vinod@brown.edu
#SBATCH --mail-type=ALL

#SBATCH --output=/users/rvinod/scratch/repos/egnn/batch_jobs/output-%j.out
#SBATCH --error=/users/rvinod/scratch/repos/egnn/batch_jobs/output-%j.err


#SBATCH --partition=gpu
#SBATCH --gres=gpu:1

#SBATCH --cpus-per-task=8
 
# Request an hour of runtime:
#SBATCH --time=100:00:00

#SBATCH --mem=150G

#SBATCH -J bindPredict


# Run a command
source ~/venvs/e3_diff/bin/activate

module load python/3.7.4

#python3 seq_model.py --timesteps 10 --epochs 5 --loss 'l2'
python3 run_bindEmbed21DL.py