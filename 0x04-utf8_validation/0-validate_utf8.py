def validUTF8(data):
    # Helper function
    def is_valid_utf8_char(bytes_sequence):
        # check if the byte sequence starts with correct prefix
        if bytes_sequence[0] & 0b10000000 == 0:
            return True

        num_bytes = 0
        for byte in bytes_sequence:
            if byte & 0b10000000 == 0b10000000:
                num_bytes += 1
            else:
                break

            if num_bytes == 1 or num_bytes > 4:
                return False

            for i in range(1, num_bytes):
                if (bytes_sequence[i] & 0b11000000) != 0b10000000:
                    return False

            return True

            i = 0
            while i < len(data):

                first_byte = data[i]

                if first-byte & 0b10000000 == 0:
                    i += 1

                else:
                    num_bytes = 0
            while first_byte & (0b10000000 >> num_bytes):
                num_bytes += 1

            # Extract the byte sequence
            byte_sequence = data[i:i + num_bytes]
            if not is_valid_utf8_char(byte_sequence):
                return False
            i += num_bytes

    return True
