from LibHanger.Library.uwGlobals import configer
from Scrapinger.Library.scrapingConfig import scrapingConfig

class scrapingConfiger(configer):
    
    """
    Scrapinger共通設定クラス
    """
    
    def __init__(self, _tgv, _file, _configFolderName):
        
        """
        コンストラクタ
        """
        
        # 基底側コンストラクタ
        super().__init__(_tgv, _file, _configFolderName)
        
        # netkeibar.ini
        da = scrapingConfig()
        da.getConfig(_file, _configFolderName)

        # gvセット
        _tgv.scrapingConfig = da
