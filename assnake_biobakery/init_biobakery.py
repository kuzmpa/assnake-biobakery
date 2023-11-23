import click
import assnake
from tabulate import tabulate
import  glob, os
from assnake.utils.general import download_from_url
from assnake.core.config import update_instance_config, read_assnake_instance_config
import tarfile

@click.command('biobakery-chocophlan-db', short_help='Initialize CHOCOPhlAn database for biobakery')
@click.option('--db-location','-d', 
            help='Where to store CHOCOPhlAn database. It will take minimum of 15GB of disk space. 	mpa_vOct22_CHOCOPhlAnSGB_202212_species will be downloaded', 
            required=False )
@click.pass_obj

def chocophlan_init(config, db_location):

    # print('HELLO WORLD')

    # db_url = "http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/"
    # #with tarfile.open('mpa_vOct22_CHOCOPhlAnSGB_202212.tar', 'r') as mytar:
    # #    mytar.extractall('mpa_vOct22_CHOCOPhlAnSGB_202212_species')

    # if db_location is None: # If no path is provided use default
    #     instance_config = read_assnake_instance_config()
    #     db_location = os.path.join(instance_config['assnake_db'], 'chocophlan')
    
    # os.makedirs(db_location, exist_ok=True)
    # filename = os.path.join(db_location, 'mpa_vOct22_CHOCOPhlAnSGB_202212_species')
    # download_from_url(db_url, filename)
    update_instance_config({'chocophlan-mpa_vOct22_CHOCOPhlAnSGB_202212_species': '/home/kuzmichenko_pa/METAPHLAN_DATABASE'})
