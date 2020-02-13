import os

def master2():
	for i in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		master('00'+i)

def master(tag):
	#used to create a .bam file for each sample
	fh=open('SAM_'+tag+'.BATCH','w')
	fh.write('#!/bin/bash\n')
	fh.write('#SBATCH --export=NONE\n')
	fh.write('#SBATCH --ntasks=1\n')
	fh.write('#SBATCH --time=04:00:00\n')
	fh.write('#SBATCH --job-name=Pool16_'+tag+'_SAM\n')
	fh.write('echo -n "Running on host: "\n')
	fh.write('hostname\n')
	fh.write('echo "Alignment starting"\n')
	fh.write('/auto/pmd-02/slp/sm_513/bwa/bwa mem -x pacbio -o Pool16_'+tag+'.sam /auto/pmd-02/slp/sm_513/reference/chr19.fa Pool16_'+tag+'.ccs.fastq\n')
	fh.write('echo "conversion to bam file"\n')
	fh.write('/bin/samtools view -S -u Pool16_'+tag+'.sam | /bin/samtools sort - Pool16_'+tag+'\n')
	fh.write('echo "indexing bam file"\n')
	fh.write('/bin/samtools index Pool16_'+tag+'.bam\n')
	fh.write('echo "End of alignment sam creation"\n')
	fh.close()
