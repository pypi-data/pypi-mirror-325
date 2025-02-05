import base64
import json
import logging
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .crypto_utils import calu_crc, decrypt_aes
from .socket_utils import send_http_request, DEFAULT_PORT
from .custom_exceptions import InvalidDataException

# Enable logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

def check_not_found_case(response):
    """Check if the response indicates a 'not found' case."""
    return "404 Not Found" not in response

def get_thing_status(ip_address, key):
    try:
        # Prepare the raw HTTP GET request
        request_str = f"GET /acstatus HTTP/1.1\r\nhost: {ip_address}\r\n\r\n"
        # logging.debug(f"Request string: {request_str}")

        # Use the common function to send the request and get the parsed response
        headers, body = send_http_request(ip_address, DEFAULT_PORT, request_str)

        # Process the response body
        logging.debug(f"Thing status received.")

        # Extract the Base64 encoded body
        base64_body = body
        # logging.debug(f"Base64 encoded body: {base64_body}") 
        
        # Decode the Base64 data
        received_data = base64.b64decode(base64_body)
        # logging.debug(f"Decoded data (hex): {received_data.hex()}")

        if len(received_data) == 0:
            logging.error("Received empty data.")
            raise InvalidDataException()

        # Validate the checksum
        total_len = len(received_data)
        checksum = calu_crc(0, received_data, total_len - 2) & 0xFFFF
        checksum_pkt = ((received_data[total_len - 1] & 0xFF) << 8) | (received_data[total_len - 2] & 0xFF)
        logging.debug(f"Calculated checksum: {checksum}, Packet checksum: {checksum_pkt}")

        if checksum != checksum_pkt:
            logging.error("Checksum validation failed.")
            raise InvalidDataException()

        # Extract AES IV and encrypted data
        aes_iv = received_data[:16]
        encrypted_data = received_data[17:-2]
        # logging.debug(f"AES IV: {aes_iv.hex()}")
        # logging.debug(f"Encrypted Data (hex): {encrypted_data.hex()}")

        # Extract AES Key
        aes_key = base64.b64decode(key)
        # logging.debug(f"AES Key (base64 decoded): {aes_key.hex()}")

        # Decrypt the data using AES CFB mode
        decrypted_data = decrypt_aes(aes_key, aes_iv, encrypted_data)
        # logging.debug(f"Decrypted data (raw): {decrypted_data.hex()}")

        # Attempt to decode the decrypted data as JSON
        decrypted_str = decrypted_data.decode('utf-8')
        # logging.info(f"Decrypted string: {decrypted_str}")
        # logging.debug(f"Decrypted string (with replacement): {decrypted_data.decode('utf-8', errors='replace')}")

        try:
            device_status = json.loads(decrypted_str)
            # logging.info(f"Device Status: {device_status}")
            return device_status
        except json.JSONDecodeError:
            logging.error("Failed to decode decrypted data as JSON.")
            raise InvalidDataException()

    except Exception as e:
        logging.error("An error occurred:", exc_info=True)
        # raise e
        return False

