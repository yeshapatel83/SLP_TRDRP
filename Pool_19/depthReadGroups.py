import os
def master():
	for tag in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		os.system('/bin/samtools depth Pool19_00'+tag+'_corrected_ReadGroups.bam>depthReadGroups_Pool19_00'+tag+'.txt')

if __name__=="__main__":
	master()
