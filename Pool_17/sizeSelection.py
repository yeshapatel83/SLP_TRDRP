def master2():
	for i in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		master(i)

def master(tag):
	qh=open('size_selected_Pool9_00'+tag+'.ccs.fastq','w')
	fh=open('Pool9_00'+tag+'.ccs.fastq','r')
	title=fh.readline()
	fn=fh.readline()
	while fn!='':
		if len(fn.rstrip())<1000:
			fh.readline()
			fh.readline()
			fh.readline()
			fh.readline()
			title=fh.readline()
			fn=fh.readline()
			continue
		else:
			qh.write(title)
			qh.write(fn)
			qh.write(fh.readline())
			qh.write(fh.readline())
			title=fh.readline()
			fn=fh.readline()
	qh.write('\n')
	qh.close()
