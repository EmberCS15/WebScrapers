#! python3

import sys, bs4, webbrowser, requests, os

if __name__ == '__main__':
		dn_str = 'http://codex.cs.yale.edu/avi/os-book/OS9/slide-dir/'
		itr=0
		for itr in range(1,19):
			print("Downloading : ch"+str(itr))
			res = requests.get(dn_str+'PPT-dir/ch'+str(itr)+'.ppt')
			res.raise_for_status()
			print('File recieved . Writing file.....')
			file_path = os.path.join(os.getcwd(), "ch{}.ppt".format(itr))
			f = open(file_path, 'wb')
			for chunk in res.iter_content(100000):
				f.write(chunk)
			f.close()
