# Add Snakemake workflow logic here
#chocophlan_db = config.get('chocophlan_db', None)

rule kraken2:
    input: 
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz'
    output: 
        f   = '{fs_prefix}/{df}/taxa/kraken2/{preproc}/{df_sample}_1.fq',
        s   = '{fs_prefix}/{df}/taxa/kraken2/{preproc}/{df_sample}_2.fq',
        o   = '{fs_prefix}/{df}/taxa/kraken2/{preproc}/{df_sample}.krak',
        r   = '{fs_prefix}/{df}/taxa/kraken2/{preproc}/{df_sample}.report',
    params: 
        out = '{fs_prefix}/{df}/taxa/kraken2/{preproc}/{df_sample}#.fq',
        kraken2_db = '~/db_assnake/kraken2_db'
    threads: 12
    conda: './kraken2.yaml'
    shell: '''kraken2 --db {params.kraken2_db} --threads {threads} --fastq-input --gzip-compressed \
        --paired {input.r1} {input.r2} --classified-out {params.out} --use-mpa-style --report {output.r} > {output.o}'''
