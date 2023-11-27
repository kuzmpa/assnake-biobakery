import click
import assnake
from tabulate import tabulate
import  glob, os
from assnake.utils.general import download_from_url
from assnake.core.config import update_instance_config, read_assnake_instance_config
import tarfile

@click.command('biobakery-chocophlan-db', short_help='Initialize CHOCOPhlAn and uniref database for biobakery')
@click.option('--db-location','-d', 
            help='Where to store CHOCOPhlAn and uniref database. It will take minimum of 15GB + 20 GB of disk space. 	mpa_vOct22_CHOCOPhlAnSGB_202212_species and uniref90_annotated_v201901b_full will be downloaded', 
            required=False )
@click.pass_obj

def chocophlan_init(config, db_location):

     print('Start download files for metaphlann and humann')

     db_url = "http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vOct22_CHOCOPhlAnSGB_202212.tar"
     #db_bw_ind = "http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/bowtie2_indexes/mpa_vOct22_CHOCOPhlAnSGB_202212_bt2.tar"
     db_url_uniref = "http://huttenhower.sph.harvard.edu/humann_data/uniprot/uniref_annotated/uniref90_annotated_v201901b_full.tar.gz"

     #with tarfile.open('mpa_vOct22_CHOCOPhlAnSGB_202212.tar', 'r') as mytar:
     #    mytar.extractall('mpa_vOct22_CHOCOPhlAnSGB_202212_species')
     if db_location is None: # If no path is provided use default
         instance_config = read_assnake_instance_config()
         db_location = os.path.join(instance_config['assnake_db'], 'biobakery')
    
     def untar_file(tar_file, destination):
         with tarfile.open(tar_file, 'r') as mytar:
             mytar.extractall(destination)

     os.makedirs(db_location, exist_ok=True)
     filename = os.path.join(db_location, 'mpa_vOct22_CHOCOPhlAnSGB_202212_species')
     download_from_url(db_url, filename)
     untar_file(filename, db_location)
     #filename = os.path.join(db_location, 'mpa_vOct22_CHOCOPhlAnSGB_202212_species_indexes')
     #download_from_url(db_bw_ind, filename)
     #untar_file(filename, db_location)
     filename = os.path.join(db_location, 'uniref90_annotated_v201901b_full')
     download_from_url(db_url_uniref, filename)
     untar_file(filename, db_location)

     update_instance_config({'biobakery_database': db_location})

#@click.command('biobakery-uniref-db', short_help='Initialize uniref database for biobakery')
#@click.option('--db-location','-d', 
#            help='Where to store uniref90 database. It will take minimum of 20GB of disk space. uniref90_annotated_v201901b_full will be downloaded', 
#            required=False )
#@click.pass_obj
#def humann_init(config, db_location):
#
#     print('Starts download files for humann')
#
#     db_url = "http://huttenhower.sph.harvard.edu/humann_data/uniprot/uniref_annotated/uniref90_annotated_v201901b_full.tar.gz"
#     #with tarfile.open('mpa_vOct22_CHOCOPhlAnSGB_202212.tar', 'r') as mytar:
#     #    mytar.extractall('mpa_vOct22_CHOCOPhlAnSGB_202212_species')
#     if db_location is None: # If no path is provided use default
#         instance_config = read_assnake_instance_config()
#         db_location = os.path.join(instance_config['assnake_db'], 'uniref')
#    
#     def untar_file(tar_file, destination):
#         with tarfile.open(tar_file, 'r') as mytar:
#             mytar.extractall(destination)
#
#     os.makedirs(db_location, exist_ok=True)
#     filename = os.path.join(db_location, 'uniref90_annotated_v201901b_full')
#     download_from_url(db_url, filename)
#     untar_file(filename, db_location)
#
#     update_instance_config({'uniref90_annotated_v201901b_full': db_location})
