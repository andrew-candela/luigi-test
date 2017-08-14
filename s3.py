from luigi import six

import luigi
import luigi.contrib.hadoop
import luigi.contrib.s3
from shutil import copyfile


class are_files_in_s3(luigi.task.ExternalTask):
	"""This task will set the dependancies of this process 
	as the existence of some files in S3.
	External tasks don't have a run() method. 
	This is used to denote some process who's input is generated outside of Luigi"""

	def output(self,paths):
		yield [luigi.contrib.s3.S3Target(path) for path in paths]

class copy_files_from_s3(luigi.task):
	"""This will copy some files from S3 into the local dir"""