import os
from ardent import ArdentClient, ArdentError, ArdentAPIError
from dotenv import load_dotenv
from tests.test_client import Ardent_Client

load_dotenv()

def test_delete_config():
    """Test deleting a configuration"""
    print("Starting delete config test...")
    
    client = Ardent_Client
    
    try:
        # Test deleting a config
        delete_id = "0d639e28-b0c0-4b9e-94b7-a51fbe33e5c9"
        result = client.delete_config(config_id=delete_id)
        print(f"Successfully deleted config: {result}")
        
    except ArdentError as e:
        print(f"Ardent error occurred: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise
    finally:
        client.close()

if __name__ == "__main__":
    test_delete_config()