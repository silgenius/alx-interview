def validUTF8(data):
    num_bytes = 0
    
    for byte in data:
        # Get the last 8 bits
        byte &= 0xFF
        
        if num_bytes == 0:
            # Determine how many bytes to expect based on the first byte
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:
            # We're expecting a continuation byte
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1
    
    return num_bytes == 0  # Check if we've completed the UTF-8 character sequences

# Example usage
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False

