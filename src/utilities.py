import os
import subprocess

##
#
class U():
    # Class variable
    conf_path='/etc/penguins-eggs.d'
    
    ##
    # eggs conf exists
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

    ##
    # wardrobe exists
    def wardrobe_exists() -> bool:
        exists=False
        wardrobe_path=os.path.expanduser('~')+"/.wardrobe"
        if os.path.exists(wardrobe_path):
            exists=True
        
        return exists

    def package_is_installed(package="eggs")->bool:
        installed=False
        result = subprocess.run(["dpkg -s " + package +" |grep Status"], shell=True, capture_output=True, text=True)
        if "Status: install ok installed" in result.stdout:
            installed=True

        return installed
    
# develop 
if __name__ == "__main__":
    pass

