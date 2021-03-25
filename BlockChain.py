import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request


# Declaring class
class BlockChain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.nodes = []

        # Genesis block
        self.new_block(previous_hash="1", proof=100)

    def register_node(self, address):
        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.add(parsed_url.netloc)
        elif parsed_url.path:
            self.nodes.add(parsed_url.path)
        else:
            raise ValueError('Invalid')