# Add Snakemake workflow logic here
#chocophlan_db = config.get('chocophlan_db', None)


rule metaphlan:
    input:
        read1 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz',
        read2 = '{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz'
    output:
        bt = '{fs_prefix}/{df}/taxa/metaphlan/{preproc}/{df_sample}_R1_R2_bowtie2.bz2',
        profiled_metagenome = '{fs_prefix}/{df}/taxa/metaphlan/{preproc}/{df_sample}_metaphlan_R1_R2.txt'
    params:
        db_chocophlan = "~/db_assnake/chocophlan",
        threads = 12  ,
        mapq = 5,
        quantile_robust = 0.2, 
        non_zero = 0.33
    conda: '../biobakery.yaml'
    shell:
            "metaphlan -t rel_ab --unclassified_estimation {input.read1},{input.read2} --input_type fastq "
            " --bowtie2db {params.db_chocophlan} --bowtie2out {output.bt} --nproc {params.threads} --bt2_ps very-sensitive"
            " --min_mapq_val {params.mapq} --tax_lev a --stat_q {params.quantile_robust} "
            " --perc_nonzero {params.non_zero} -o {output.profiled_metagenome}"