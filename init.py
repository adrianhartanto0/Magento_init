import os,sys


if(len(sys.argv) != 3):
	print("Please provide a ModuleNamespace & ModuleName");
	sys.exit();

for x in [1,2]:
	dir1 = os.getcwd() + "/" + sys.argv[x];
	os.mkdir(dir1);
	os.chdir(dir1);

targetDir1 = os.getcwd();
for x in ["/Block","/controllers","/etc","/Helper","/Model","/sql"]:
	os.mkdir(targetDir1 + x);

os.chdir(targetDir1 + "/etc");
file = open("config.xml","wb");
file.close();

