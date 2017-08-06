from luigi import six

import luigi
import luigi.contrib.hadoop
import luigi.contrib.hdfs
import luigi.contrib.postgres
from shutil import copyfile



class copy_file(luigi.Task):
	def run(self):
		src='~/test_file.txt'
		dst='~/luigi_step1.txt'
		copyfile(src, dst)
		with self.output().open('w') as output:
			output.write('All done!')

	def output(self):
		return luigi.LocalTarget('./read_from_file.done')

class copy_second_file(luigi.Task):
	def run(self):
		src='~/luigi_step1.txt'
		dst='~/luigi_step2.txt'
		copyfile(src,dst)
		with self.output().open('w') as output:
			output.write('All done!')
	def requires(self):
		return [copy_file()]
	def output(self):
		return luigi.LocalTarget('./read_from_file2.done')

if __name__ == "__main__":
    luigi.run()