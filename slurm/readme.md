# Useful Slurm commands

## Slurm Job Status
### Checking my job status
```bash
squeue -u <user name>
```

### Canceling a job
```bash
scancel <job id>
```

## Graphic Card Usage Check
```bash
srun --jobid=<job_id> nvidia-smi
```