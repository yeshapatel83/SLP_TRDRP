import os,itertools

def master2():
	for i in ['01','02','03','05','06','09','10','12','16','19','21','24','26','27','33','34','37','39','40','45','55','56','58','59']:
		master('00'+i)

def master(tag):
	os.system('/bin/samtools depth Pool19_'+tag+'.bam>depth_Pool19_'+tag+'.txt')
	fh=open('depth_Pool19_'+tag+'.txt','r')
	fn=fh.readlines()
	numberlist=[]
	for i in range(0,len(fn)):
		fn[i]=fn[i].rstrip().split('\t')
		if int(fn[i][-1])>=1:
			if 40842583<=int(fn[i][1])<=40850993:
				numberlist.append(int(fn[i][1]))
			elif 40874836<=int(fn[i][1])<=40882778:
				numberlist.append(int(fn[i][1]))
			elif 41086451<=int(fn[i][1])<=41098195:
				numberlist.append(int(fn[i][1]))
	a=list(ranges(numberlist))
	print a
	print len(a)

	qh=open('ALEC_template.BATCH','r')
	qn=qh.readlines()
	ch=open('ALEC_'+tag+'.BATCH','w')
	for i in qn:
		if i.startswith('#START'):
			for j in range(0,len(a)):
				ch.write('python ../../alec/ALEC/ALEC/ALEC.py -r ../../reference/chr19.fasta -i Pool19_'+tag+'.sam -x pacbio_ccs -t chr19:'+str(a[j][0])+'-'+str(a[j][1])+'\n')
				ch.write('mv Pool19_'+tag+'.corrected.fasta temp0'+str(j)+'_Pool19_'+tag+'.corrected.fasta\n')
		elif i.startswith('#END'):
			continue
		else:
			ch.write(i.replace('0001',tag))
	ch.write('rm -rf temp*'+tag+'*\n')
	ch.close()

def ranges(i):
	for a,b in itertools.groupby(enumerate(i),lambda(x,y):y-x):
		b=list(b)
		yield b[0][1],b[-1][1]

