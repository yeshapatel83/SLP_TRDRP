import os

#requires that .bam files have been created first

def master2():
	for i in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		master('00'+i)

def master(tag):
	os.system("/bin/samtools view Pool16_"+tag+".bam |awk '{print length($10)}'|sort -u >readStats"+tag+".txt")

