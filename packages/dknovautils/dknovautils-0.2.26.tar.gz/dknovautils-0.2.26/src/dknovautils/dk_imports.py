from __future__ import annotations

import logging

from typing import List, Dict, Tuple, Union, Any

import random
import time

import math
import random
from collections import namedtuple, deque
import re
import sys


import os
import subprocess
from queue import Queue
from queue import Empty
from pathlib import Path
import itertools
import itertools as ite

import threading

import hashlib


import time
from datetime import datetime
from datetime import date



from enum import Enum, unique

import base64
import argparse
import random
import time
import os

from typing import Callable, List, Dict, Tuple, Union, Any, Deque
from typing import Iterable, TYPE_CHECKING

import os, sys, math
import logging
import time
from datetime import datetime
from datetime import date

from collections import deque

import threading

import os
from os.path import join, getsize
import shutil
from pathlib import Path
from typing import List, Dict, Iterator, Set, Tuple

from functools import *

import traceback


# ---------------------------------------

# 这是非系统内置的 第三方库 集中写在此处
try:
    import numpy as np
    import urllib3
    import pyperclip
    
    from dataclasses import dataclass
    import dataclasses    

finally:
    pass


# ----------------------------------------


class LLevel(Enum):
    Trace = 0
    Debug = 10
    Info = 20
    Warn = 30
    Error = 40
