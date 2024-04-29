#!/bin/bash
#SBATCH --job-name <job name>                       # Job name
#SBATCH --ntasks 2                                  # Number of tasks
#SBATCH --time 3-00                                 # Runtime
#SBATCH --mem-per-gpu=30G                           # Reserve 30 GB memory per GPU
#SBATCH --partition gpu                             # Partition to submit
#SBATCH --output job-log-%j.txt                     # Standard out will be written to this file
#SBATCH --error job-log-%j.txt                      # Standard err will be written to this file
#SBATCH --mail-user <email>                         # This is the email you wish to be notified at
#SBATCH --mail-type ALL                             # Alert types to get via email
#SBATCH --nodelist=<nodelist>                       # Node list to submit the job
#SBATCH --gres=gpu:2                                # Number of gpu to reserve
#SBATCH --requeue                                   # Requeue when the job is cancelled

spack load <dependency name>
module load <dependency name>

# ACTIVATE ANACONDA IF NEEDED
eval "$(conda shell.bash hook)"
conda activate <conda environment name>

# RUN TRAINING
deepspeed your_code.py
