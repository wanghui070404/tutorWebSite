import ctypes
from ctypes import c_char_p
import sys
import os

# Import DLL files
dilithium_dll_path = os.path.join(os.getcwd(), "C:\\Users\\DELL\\Downloads\\Modify\\tutorWebSite\\app1\\dilithiumstring.dll")
oqs_dll_path = os.path.join(os.getcwd(), "C:\\Users\\DELL\\Downloads\\Modify\\tutorWebSite\\app1\\liboqs.dll")

try:
    dilithium_lib = ctypes.CDLL(dilithium_dll_path)
    oqs_lib = ctypes.CDLL(oqs_dll_path)
    print("DLLs loaded successfully.")
except Exception as e:
    print(f"Failed to load DLLs: {e}")
    sys.exit(1)

# Define the new function prototypes
try:
    keygen = dilithium_lib.keygen
    keygen.argtypes = [c_char_p]
    keygen.restype = c_char_p

    sign = dilithium_lib.sign
    sign.argtypes = [c_char_p, c_char_p]
    sign.restype = c_char_p

    verify = dilithium_lib.verify
    verify.argtypes = [c_char_p, c_char_p, c_char_p]
    verify.restype = ctypes.c_bool

    print("Function prototypes defined successfully.")
except Exception as e:
    print(f"Failed to define function prototypes: {e}")
    sys.exit(1)

# Call functions
def call_keygen(privateKeyFile):
    try:
        publicKeyFile = publicKeyFile.encode('utf-8')
        privateKeyFile = privateKeyFile.encode('utf-8')
        keygen(publicKeyFile, privateKeyFile)
        print(f"Keys generated: public key ({publicKeyFile}), private key ({privateKeyFile})")
    except Exception as e:
        print(f"Error during keygen: {e}")

def call_sign(messageFile, privateKeyFile, signatureFile):
    try:
        messageFile = messageFile.encode('utf-8')
        privateKeyFile = privateKeyFile.encode('utf-8')
        signatureFile = signatureFile.encode('utf-8')
        sign(messageFile, privateKeyFile, signatureFile)
        print(f"Message signed: message file ({messageFile}), private key ({privateKeyFile}), signature file ({signatureFile})")
    except Exception as e:
        print(f"Error during sign: {e}")

def call_verify(messageFile, signatureFile, publicKeyFile):
    try:
        messageFile = messageFile.encode('utf-8')
        signatureFile = signatureFile.encode('utf-8')
        publicKeyFile = publicKeyFile.encode('utf-8')
        result = verify(messageFile, signatureFile, publicKeyFile)
        print(f"Verification result: {result}")
        return result
    except Exception as e:
        print(f"Error during verify: {e}")
        return False

if __name__ == "__main__":
    print("Script started.")
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} [keygen|sign|verify] [other parameters]")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == "keygen":
        if len(sys.argv) != 4:
            print(f"Usage: {sys.argv[0]} keygen <public key file> <private key file>")
            sys.exit(1)

        public_key_path = sys.argv[2]
        private_key_path = sys.argv[3]

        call_keygen(public_key_path, private_key_path)
        print(f"Keys generated successfully: public key saved to {public_key_path}, private key saved to {private_key_path}")

    elif mode == "sign":
        if len(sys.argv) != 5:
            print(f"Usage: {sys.argv[0]} sign <message file> <private key file> <signature output file>")
            sys.exit(1)

        message_file_path = sys.argv[2]
        private_key_path = sys.argv[3]
        signature_path = sys.argv[4]

        call_sign(message_file_path, private_key_path, signature_path)
        print(f"Message signed successfully and saved signature to {signature_path}")

    elif mode == "verify":
        if len(sys.argv) != 5:
            print(f"Usage: {sys.argv[0]} verify <message file> <signature file> <public key file>")
            sys.exit(1)

        message_file_path = sys.argv[2]
        signature_path = sys.argv[3]
        public_key_path = sys.argv[4]

        if call_verify(message_file_path, signature_path, public_key_path):
            print("Message verified successfully.")
        else:
            print("Failed to verify message.")

    else:
        print("Invalid mode! Please choose keygen, sign, or verify!")
        sys.exit(1)

    sys.exit(0)

