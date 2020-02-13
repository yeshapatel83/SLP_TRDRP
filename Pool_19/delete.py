numbers=['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']
def crap(file_):
	fh=open(file_,'r')
	fn=fh.readlines()
	fh=open(file_,'w')
	for i in fn:
		fh.write(i.replace('Pool16','Pool17'))
	fh.close()

for i in numbers:
	crap('ALEC_00'+i+'.BATCH')
