import sys
import threading
import re

class Malicious:
    
    addr = re.match('/@"^[13][a-km-zA-HJ-NP-Z0-9]{26,33}$"/', '1fakedontsendinvalidmfBsbif4miY36v')