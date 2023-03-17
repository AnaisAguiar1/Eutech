# SCRIPT PARA AUTOMATZAR BACKUPS DE ANAIS G. AGUIAR CONTRERAS.

# Import all the modules that we are going to use

import json
import datetime
import logging
import shutil
import os
import schedule
import time

# Indicate to open the config file with json from python / Indicar que se abra el archivo con json desde python

def backup_eutech(config_file):
    # Load the config file
    with open(config_file) as f:
        config = json.load(f)

# Create the backup directory with the date and time of the moment the backup is made / Creacion del directorio de backup con la fecha como nombre

    backup_dirs = os.path.join(config["backup_destinations_directories"][0],
            datetime.datetime.now().strftime
            ("%d-%m-%Y_%H-%M-%S"))
    os.makedirs(backup_dirs)

# Copy each directory indicated to make the respective backup / Guardar cada directorio que fue copiado en el directorio de backups indicado

    for directory in config["backup_directories_to_copy"]:
        try:
            shutil.copytree(directory, os.path.join(backup_dirs, os.path.basename(directory)))
        except Exception as e:
            logging.error(f"Error backing up {directory}: {e}")

# Log file of errors and process / documentar el proceso de los backups 

    logging.basicConfig(filename=config["log_file_of_errors_and_process"][0], level=logging.INFO)
    logging.info(f"Backup created at {backup_dirs}")

# Delete oldest backup directories when the max number is reached / Eliminar los backup cando lleguen a un maximo de 

    backup_dir = sorted(os.listdir(config["backup_destinations_directories"][0]))
    if len(backup_dir) > int(config["max_backups_to_reach"]):
        oldest_backup = os.path.join(config["backup_destinations_directories"][0], backup_dir[0])
        shutil.rmtree(oldest_backup)
        logging.info(f"Deleted oldest backup at {oldest_backup}")

    return backup_dirs

if __name__ == '__main__':

# Schedule backup to run every day at the hour that you decide and specify / Programar exactamente cada cuanto queremos generar los backups.

    schedule.every(2).seconds.do(backup_eutech, config_file='config.json')

# If you want to change the time when the backups are generated, you must change in this case the word "minutes" by the sequence of time you want.

# example: schedule.every(1).hours.do(backup_eutech, config_file='config.json')
# example: schedule.every(1).days.do(backup_eutech, config_file='config.json')

# Keep running scheduled tasks / Comprobar constantemente si hay alguna tarea programada por ejecutar.

    while True:
        schedule.run_pending()
        time.sleep(2)