import os
import re
import sys
from logger import Logger


class PlaylistParser:

    @staticmethod
    def parse_folder(absolute_folder_path):
        Logger.log_info('Start parsing folder: ' + absolute_folder_path)

        normalized_path = os.path.normpath(absolute_folder_path)
        PlaylistParser._check_folder_exists(normalized_path)

        file_names = os.listdir(normalized_path)
        Logger.log_info('Find ' + str(len(file_names)) + ' files in folder')

        files = []
        for file_name in file_names:
            if re.match('mpd\.slice\.\d+\-\d+\.json', file_name):
                absolute_file_name = os.path.join(normalized_path, file_name)
                files.append(absolute_file_name)

        Logger.log_info(str(len(files)) + ' playlist files conform file name convention')
        return files

    @staticmethod
    def _check_folder_exists(normalized_path):
        if not os.path.exists(normalized_path):
            Logger.log_error("Path not found: " + normalized_path)
            sys.exit(1)
