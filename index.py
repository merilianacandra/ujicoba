from http.server import BaseHTTPRequestHandler
from pymongo import MongoClient
import json


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        client = MongoClient(
            "mongodb+srv://cmeriliana:hwij8dts*@candracluster-eyzid.gcp.mongodb.net/test?retryWrites=true")

        db = client.mahasiswa
        collection = db.mhs

        all_mahasiswa = collection.find()

        for data in all_mahasiswa:
            self.wfile.write(data["nama"].encode())
            self.wfile.write("\n".encode())
            self.wfile.write(str(data['umur']).encode())
            self.wfile.write("\n".encode())

