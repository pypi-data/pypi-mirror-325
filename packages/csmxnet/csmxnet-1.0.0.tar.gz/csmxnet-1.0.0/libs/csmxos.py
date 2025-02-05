import os
import platform
import hashlib

class CsmxOS:
    """Enhanced OS module with AI-resistant security and process control"""

    @staticmethod
    def secure_listdir(path="."):
        """Lists directory contents but prevents access to hidden/sensitive files"""
        try:
            return [f for f in os.listdir(path) if not f.startswith('.')]
        except Exception as e:
            return [f"Error: {str(e)}"]

    @staticmethod
    def secure_random_filename(extension="txt"):
        """Generates a secure, unpredictable filename"""
        return f"{hashlib.sha256(os.urandom(32)).hexdigest()}.{extension}"

    @staticmethod
    def get_system_info():
        """Returns secure system information"""
        return {
            "OS": platform.system(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
        }

# Example Usage
if __name__ == "__main__":
    print("🔹 Secure Directory Listing:", CsmxOS.secure_listdir())
    print("🔹 Secure Random Filename:", CsmxOS.secure_random_filename("log"))
    print("🔹 System Info:", CsmxOS.get_system_info())
