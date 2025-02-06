import os
import shutil
from flaskr.configs.logger import log_system

# 当前文件所在文件夹
# os.path.dirname(__file__)


class __PathOperate:

    def mkdir(self, path: str):
        abspath = os.path.abspath(path)

        if os.path.isfile(abspath):
            abspath = os.path.dirname(abspath)

        if not os.path.exists(abspath):
            os.makedirs(abspath)

        return abspath

    def rmdir(self, path: str):
        abspath = os.path.abspath(path)

        if os.path.isfile(abspath):
            abspath = os.path.dirname(abspath)

        def onerror(func, path, exc_info):
            log_system.warning(f'remove {path} error: {exc_info}')

        shutil.rmtree(path=abspath, ignore_errors=False, onerror=onerror)
        # if os.path.exists(abspath):
        #     dir_content = os.listdir(abspath)

        #     if len(dir_content) == 0:
        #         os.rmdir(abspath)
        #     else:
        #         for file in dir_content:
        #             file_path = os.path.join(abspath, file)

        #             if os.path.isfile(file_path):
        #                 os.remove(file_path)
        #             elif os.path.isdir(file_path):
        #                 self.rmdir(file_path)

        #         os.rmdir(abspath)

    def rmfile(self, path: str):
        abspath = os.path.abspath(path)

        if os.path.exists(abspath) and os.path.isfile(abspath):
            os.remove(abspath)


Path = __PathOperate()
