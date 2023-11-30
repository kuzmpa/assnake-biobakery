import os
import assnake

from assnake_biobakery.init_biobakery import chocophlan_init,uniref_init,kraken2_init,humann_init

snake_module = assnake.SnakeModule(name = 'assnake-biobakery', 
                           install_dir = os.path.dirname(os.path.abspath(__file__)),
                           initialization_commands = [chocophlan_init,uniref_init,kraken2_init,humann_init]
                           )