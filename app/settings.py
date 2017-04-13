"""Settings for Fireball"""
import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
WORK_FOLDER = os.environ.get('FIREBALL_WORK_FOLDER')
DOWNLOAD_POOL_SIZE = int(os.environ.get('FIREBALL_DOWNLOAD_POOL_SIZE'))
DEFAULT_DPI = 300
PDF_COMPLIANCE_VERSION = "%PDF-1.3"
LOGFILE = os.environ.get('FIREBALL_LOGFILE')