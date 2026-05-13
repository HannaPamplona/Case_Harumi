#!/bin/bash  
#SBATCH --partition=SP2
#SBATCH --ntasks=1              # number of tasks / mpi processes
#SBATCH --cpus-per-task=1       # Number OpenMP Threads per process
#SBATCH -J aloca-1-cpu
#SBATCH --time=5:00:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

echo $SLURM_JOB_ID              #ID of job allocation
echo $SLURM_SUBMIT_DIR          #Directory job where was submitted
echo $SLURM_JOB_NODELIST        #File containing allocated hostnames
echo $SLURM_NTASKS              #Total number of cores for job


#run the application:
#pip install docplex
#pip install pandas
#pip install openpyxl
#pip install xlwings

module load cplex

cd /temporario2/9717617/Input_1
python ./cplex1.py

