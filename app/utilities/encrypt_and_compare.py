## This code is to hash and compare hashes
import bcrypt

class encrypt_and_compare():
    def generate_hash(text_to_convert: str):
        b_text = text_to_convert.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(b_text, salt)
        return hashed

    def compare_hash(hashed: bytes, text_to_compare: str):
        b_text = text_to_compare.encode("utf-8")

        if bcrypt.checkpw(b_text, hashed):
            return "Son iguales"
        
        return "Nada que ver"

