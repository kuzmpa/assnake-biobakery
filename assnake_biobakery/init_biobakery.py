import click
import assnake
from tabulate import tabulate
import  glob, os
from assnake.utils.general import download_from_url
from assnake.core.config import update_instance_config, read_assnake_instance_config
import tarfile
import subprocess
from git import Repo

@click.command('biobakery-chocophlan-db', short_help='Initialize CHOCOPhlAn database for metaphlan')
@click.option('--db-location','-d', 
            help='Where to store CHOCOPhlAn database. It will take minimum of 15GB of disk space. 	mpa_vOct22_CHOCOPhlAnSGB_202212_species  will be downloaded', 
            required=False )
@click.pass_obj

def chocophlan_init(config, db_location):

     print('Start download files for metaphlann and humann')

     db_url = "http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/mpa_vOct22_CHOCOPhlAnSGB_202212.tar"
     db_bw_ind = "http://cmprod1.cibio.unitn.it/biobakery4/metaphlan_databases/bowtie2_indexes/mpa_vOct22_CHOCOPhlAnSGB_202212_bt2.tar"
    
     if db_location is None: # If no path is provided use default
         instance_config = read_assnake_instance_config()
         db_location = os.path.join(instance_config['assnake_db'], 'chocophlan')
    
     def untar_file(tar_file, destination):
         with tarfile.open(tar_file, 'r') as mytar:
             mytar.extractall(destination)

     os.makedirs(db_location, exist_ok=True)
     filename = os.path.join(db_location, 'mpa_vOct22_CHOCOPhlAnSGB_202212_species')
     download_from_url(db_url, filename)
     untar_file(filename, db_location)
     filename = os.path.join(db_location, 'mpa_vOct22_CHOCOPhlAnSGB_202212_species_indexes')
     download_from_url(db_bw_ind, filename)
     untar_file(filename, db_location)

     update_instance_config({'biobakery_database': db_location})

@click.command('biobakery-uniref-db', short_help='Initialize uniref database for biobakery')
@click.option('--db-location','-d', 
            help='Where to store uniref90 database. It will take minimum of 20GB of disk space. uniref90_annotated_v201901b_full will be downloaded', 
            required=False )
@click.pass_obj
def uniref_init(config, db_location):

     print('Starts download files for humann')

     db_url = "http://huttenhower.sph.harvard.edu/humann_data/uniprot/uniref_annotated/uniref90_annotated_v201901b_full.tar.gz"
     #with tarfile.open('mpa_vOct22_CHOCOPhlAnSGB_202212.tar', 'r') as mytar:
     #    mytar.extractall('mpa_vOct22_CHOCOPhlAnSGB_202212_species')
     if db_location is None: # If no path is provided use default
         instance_config = read_assnake_instance_config()
         db_location = os.path.join(instance_config['assnake_db'], 'uniref')
    
     def untar_file(tar_file, destination):
         with tarfile.open(tar_file, 'r') as mytar:
             mytar.extractall(destination)

     os.makedirs(db_location, exist_ok=True)
     filename = os.path.join(db_location, 'uniref90_annotated_v201901b_full')
     download_from_url(db_url, filename)
     untar_file(filename, db_location)

     update_instance_config({'uniref90_annotated_v201901b_full': db_location})

@click.command('kraken2-db', short_help='Initialize database for kraken2')
@click.option('--db-location','-d', 
            help='Where to store silva database. It will take approximately 60 Mb of disk space. hash.k2d, opts.k2d, taxo.k2d will be downloaded', 
            required=False )
@click.pass_obj
def kraken2_init(config, db_location):

     print('Starts download files for kraken')

     
     hash_k = "https://refdb.s3.climb.ac.uk/kraken2-microbial/hash.k2d"
     opts = "https://refdb.s3.climb.ac.uk/kraken2-microbial/opts.k2d"
     taxo = "https://refdb.s3.climb.ac.uk/kraken2-microbial/taxo.k2d"

     if db_location is None: # If no path is provided use default
        instance_config = read_assnake_instance_config()
        db_location = os.path.join(instance_config['assnake_db'], 'kraken2_db')
    
     os.makedirs(db_location, exist_ok=True)
     filename = os.path.join(db_location, 'hash.k2d')
     download_from_url(hash_k, filename)

     filename = os.path.join(db_location, 'opts.k2d')
     download_from_url(opts, filename)

     filename = os.path.join(db_location, 'taxo.k2d')
     download_from_url(taxo, filename)

     update_instance_config({'kraken2_db': db_location})

@click.command('humann_tools', short_help='Initialize humann files')
@click.option('--db-location','-d', 
            help='Where to store humn GITHUB.',  
            required=False )
@click.pass_obj
def humann_init(config, db_location):
     if db_location is None: # If no path is provided use default
        instance_config = read_assnake_instance_config()
        db_location = os.path.join(instance_config['assnake_db'], 'humann_tools')
    
     #Repo.clone_from(git_url, repo_dir)
     command = ['git', 'clone', 'https://github.com/biobakery/humann',db_location]
     output = subprocess.check_output(command)
     
     update_instance_config({'humann_tools': db_location})