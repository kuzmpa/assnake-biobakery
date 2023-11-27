# Add Snakemake workflow logic here
#chocophlan_db = config.get('chocophlan_db', None)

rule cat:
    input:
        r1 = "{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1.fastq.gz",
        r2 = "{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R2.fastq.gz"
    output:
        "{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1_R2.fastq.gz"
    threads:15
    shell:
        "cat {input} > {output}"

rule humann:
    input:
        read = "{fs_prefix}/{df}/reads/{preproc}/{df_sample}_R1_R2.fastq.gz"
    output:
        gf = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2__genefamilies.tsv",
        pa = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2_pathabundance.tsv",
        pc = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2_pathcoverage.tsv" 
    params:
        output_dir    = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}" ,
        metaphlan_dir = '{fs_prefix}/{df}/taxa/metaphlan/{preproc}/{df_sample}_metaphlan_R1_R2.txt'
    threads:15
    conda: '../biobakery.yaml'
    shell:
        """humann --input {input.read} --output {params.output_dir} --threads {threads} --taxonomic-profile {params.metaphlan_dir} --remove-temp-output   
        """ 
rule renorm:
    input: 
        input_path_table  = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2_pathabundance.tsv",
        input_gene_table  = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2__genefamilies.tsv"
    output:
        renorm_path_table = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2_pathabundance-relab.tsv",
        renorm_gene_table = "{fs_prefix}/{df}/pathway/humann/{preproc}/{df_sample}_R1_R2_genefamilies-relab.tsv"
    shell:
        """humann_renorm_table --input {input.input_path_table}  --output {output.renorm_path_table} --units relab --update-snames;
           humann_renorm_table --input {input.input_gene_table}  --output {output.renorm_gene_table} --units relab --update-snames
        """