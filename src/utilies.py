import os
import subprocess

##
#
class U():
    # Class variable
    conf_path='/etc/penguins-eggs.d'
    
    ##
    # eggs is installed
    def conf_exists() -> bool:
        exists=False
        if os.path.exists(U.conf_path):
            exists=True
        
        return exists

    ##
    # /etc/penguins-eggs.d/eggs.yaml
    def eggs_yaml_exists(self)->bool:
        exists=False
        if os.path.exists(U.conf_path+'/eggs.yaml'):
            exists=True
        
        return exists


    ##
    # /etc/penguins-eggs.d/tools.yaml
    def tools_yaml_exists(self)->bool:
        exists=False
        if os.path.exists(U.conf_path+'/tools.yaml'):
            exists=True
        
        return exists

    def package_is_installed(package="eggs")->bool:
        installed=False
        result = subprocess.run(["dpkg -s " + package +" |grep Status"], shell=True, capture_output=True, text=True)
        print(result.stdout)
        if "Status: install ok installed" in result.stdout:
            installed=True

        print("packags: " + package )
        print(installed)
        return installed
    
    def package_install(package="eggs")->bool:
        subprocess.run(["/usr/bin/sudo", "apt" ,"install", package])
        return True

# develop 
if __name__ == "__main__":
    U.package_install("eggs")