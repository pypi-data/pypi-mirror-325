import os
from ardent import ArdentClient, ArdentError, ArdentValidationError
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

def test_mongodb_config():
    """Test MongoDB configuration validation and setting"""
    print("Starting MongoDB config test...")
    
    client = ArdentClient(
        public_key=os.getenv("PUBLIC_KEY"), 
        secret_key=os.getenv("SECRET_KEY"),
        base_url=os.getenv("BASE_URL"),
    )
    
    try:
        # Test valid config

        
        result = client.set_config(
            config_type="mongodb",
            connection_string=os.getenv("MONGODB_CONNECTION_STRING"),
            databases=[{
                "name": "Testing_DB",
                "collections": [
                    {"name": "Testing"}
                ]
            }]
        )

        print(result)
        print("Valid config test passed")
        
        # Test invalid configs
        invalid_configs = [
            # Missing collections
            {
                "connection_string": "mongodb://localhost:27017",
                "databases": [{"name": "test_db"}]
            },
            # Invalid database structure
            {
                "connection_string": "mongodb://localhost:27017",
                "databases": ["invalid"]
            },
            # Invalid collection structure
            {
                "connection_string": "mongodb://localhost:27017",
                "databases": [{
                    "name": "test_db",
                    "collections": ["invalid"]
                }]
            }
        ]
        
        for i, invalid_config in enumerate(invalid_configs):
            try:
                client.set_config(
                    config_type="mongodb",
                    **invalid_config
                )
                raise Exception(f"Invalid config {i} should have failed validation")
            except ArdentValidationError:
                print(f"Invalid config {i} correctly failed validation")
                
    except ArdentError as e:
        print(f"Ardent error occurred: {str(e)}")
        raise
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise
    finally:
        client.close()

if __name__ == "__main__":
    test_mongodb_config()
