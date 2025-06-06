# Guía para ejecutar procesos con SLURM usando un archivo `.sh`

Este documento explica cómo crear un archivo de script `.sh` para solicitar recursos de un clúster de computación utilizando SLURM, y cómo ejecutar un proceso dentro de un contenedor Singularity con soporte para GPU.

## Requisitos previos

Antes de proceder, asegúrate de tener acceso al clúster donde se ejecutan trabajos con SLURM y tener el contenedor Singularity listo para usar. También necesitarás un script Python o cualquier otro proceso que quieras ejecutar en el contenedor.

## 1. Creación del archivo `.sh`

Para solicitar recursos y ejecutar un proceso con SLURM, primero debes crear un archivo de script `.sh`. A continuación se muestra un ejemplo de cómo se vería este archivo, llamado `slurm2.sh`.

### Ejemplo de archivo `slurm2.sh`:

```bash
#!/bin/bash
#SBATCH --job-name=example          # Nombre del trabajo
#SBATCH --cpus-per-task=1           # Número de CPUs por tarea
#SBATCH --mem=1G                    # Memoria solicitada (1 GB)
#SBATCH --error=example.err         # Archivo para errores
#SBATCH --output=example.out        # Archivo para salida estándar
#SBATCH --gres=gpu:1                # Solicita una GPU
#SBATCH --mail-type=ALL             # Notificaciones de cualquier cambio en el estado del trabajo
#SBATCH --mail-user=correo@uoh.cl   # Dirección de correo para recibir notificaciones

# Ejecutar el proceso dentro del contenedor Singularity
singularity exec --nv my_container.sif python3 ../test_2.py


# Con esto ya podemos virtualizar el entrenamiento del modelo
