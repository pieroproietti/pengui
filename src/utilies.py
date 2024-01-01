import os

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



