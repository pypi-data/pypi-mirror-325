import unittest
import sys
import os

# Ensure the test script finds advxml properly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from advxml import advxml
from cryptography.fernet import Fernet

class TestAdvXml(unittest.TestCase):
    def test_to_from_xml(self):
        data = {"name": "Alice", "role": "admin"}
        xml_str = advxml.to_xml(data)
        parsed_data = advxml.from_xml(xml_str)
        self.assertEqual(data, parsed_data)

    def test_compress_decompress_xml(self):
        xml_str = "<root><name>Alice</name></root>"
        compressed = advxml.compress_xml(xml_str)
        decompressed = advxml.decompress_xml(compressed)
        self.assertEqual(xml_str, decompressed)

    def test_encrypt_decrypt_xml(self):
        xml_str = "<root><name>Alice</name></root>"
        key = advxml.generate_key()
        encrypted = advxml.encrypt_xml(xml_str, key)
        decrypted = advxml.decrypt_xml(encrypted, key)
        self.assertEqual(xml_str, decrypted)

    def test_validate_xml(self):
        xml_str = "<root><name>Alice</name></root>"
        xsd_schema = """<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
                        <xs:element name="root">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="name" type="xs:string"/>
                                </xs:sequence>
                            </xs:complexType>
                        </xs:element>
                        </xs:schema>"""
        self.assertTrue(advxml.validate_xml(xml_str, xsd_schema))

if __name__ == "__main__":
    unittest.main()
