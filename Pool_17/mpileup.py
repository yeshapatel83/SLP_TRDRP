import os

def master2():
	for i in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		master(i)

def master(tag):
	os.system('/bin/samtools mpileup Pool17_00'+tag+'_corrected_ReadGroups.bam -f ../../reference/chr19.fa -s -u | /bin/bcftools view -v -c ->Pool17_CCS_00'+tag+'.vcf')
