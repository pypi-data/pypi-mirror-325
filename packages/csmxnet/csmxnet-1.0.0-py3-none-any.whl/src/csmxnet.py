from libs.csmxos import CsmxOS
from libs.csmxsys import CsmxSys

class CsmxNet:
    """Main class integrating all custom system security libraries"""

    def __init__(self):
        self.os = CsmxOS()
        self.sys = CsmxSys()

    def check_security(self):
        """Runs security checks and returns results"""
        secure_dir = self.os.secure_listdir()
        fake_version = self.sys.randomize_python_version()
        
        # ✅ Instead of printing, return a structured response
        return {
            "secure_directory": secure_dir,
            "fake_python_version": fake_version
        }

# Run the script
if __name__ == "__main__":
    network = CsmxNet()
    print(network.check_security())  # Now it prints structured output
