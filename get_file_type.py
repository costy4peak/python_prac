import gzip, os
import tarfile, zipfile, rarfile

from library.utils.file import get_filetype
from library.utils.path import make_dir
from library.utils.type_conv import random_str

def uncompress(src_file, dst_dir):
	result=get_filetype(src_file)
	if not result[0]:
		return (False, result[1], '')
	filefmt = result[1]
	
	result = make_dir(dst_dir)
	if not result:
		return (False, 'make dir failed', filefmt)
	
	if filefmt in ('tgz', 'tar'):
		try:
			tar = tarfile.open(src_file)
			names = tar.getnames()
			for name in names:
				tar.extract(name, dst_dir)
			tar.close()
		except Exception as e:
			return (False, e, filefmt)
	elif filefmt == 'zip':
		try:
			zip_file = zipfile.ZipFile(src_file)
			for names in zip_file.namelist():
				zip_file.extract(names, dst_dir)
			zip_file.close()
		except Exception as e:
			return (False, e, filefmt)
	elif filefmt == 'rar':
		try:
			rar = rarfile.RarFile(src_file)
			os.chdir(dst_dir)
			rar.extractall()
			rar.close()
		except Exception as e:
			return (False, e, filefmt)
	elif filefmt == 'gz':
		try:
			f_name = dst_dir + '/' + os.path.basename(src_file）
			g_file = gzip.GzipFile(src_file)
			open(f_name, "w+").write(g_file.read())
			g_file.close()
			
			result = get_filetype(src_file)
			if not result[0]:
				new_filefmt = 'unknown'
			else:
				new_filefmt = result[1]
			return (True, 'file format after unzip: ' + new_filefmt, filefmt)
		except Exception as e:
			return (False, e, filefmt)
	else:
		return (False, 'File is not a zip file or format not supported', filefmt)
	
	return (True, '', filefmt)
			
