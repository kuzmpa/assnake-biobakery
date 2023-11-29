# Add Snakemake workflow logic here
#chocophlan_db = config.get('chocophlan_db', None)


rule spades:
    input:
        r1 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz',
        r2 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz'
    output:
        out = '{fs_prefix}/{df}/assemble/metaSPAdes/{preproc}/{df_sample}/contigs.fasta'
    params:
        out_dir = '{fs_prefix}/{df}/assemble/metaSPAdes/{preproc}/{df_sample}'
    conda: './spades.yaml'
    threads: 16
    shell: "spades.py --meta --threads {threads} -1 {input.r1} -2 {input.r2} -o {params.out_dir};"