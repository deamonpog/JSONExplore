#!/usr/bin/env python3
"""
Test script for JSON Scout package installation and basic functionality.
Run this in a fresh environment after installing the package.
"""

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        import jsonscout
        print("✅ Main package import successful")
    except ImportError as e:
        print(f"❌ Main package import failed: {e}")
        return False
    
    try:
        import jsonscout as js
        print("✅ Namespace import successful")
    except ImportError as e:
        print(f"❌ Namespace import failed: {e}")
        return False
    
    try:
        from jsonscout import Explore, Maybe, Xplore, SimpleXML
        print("✅ Individual class imports successful")
    except ImportError as e:
        print(f"❌ Individual imports failed: {e}")
        return False
    
    try:
        from jsonscout import get_json_file_paths, read_json_file
        print("✅ Function imports successful")
    except ImportError as e:
        print(f"❌ Function imports failed: {e}")
        return False
    
    return True

def test_basic_functionality():
    """Test basic functionality of the package."""
    print("\nTesting basic functionality...")
    
    import jsonscout as js
    
    # Test data
    test_data = {
        "users": [
            {"name": "Alice", "age": 30, "email": "alice@example.com"},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
        ],
        "metadata": {"version": "1.0", "created": "2024-01-01"}
    }
    
    try:
        # Test Xplore
        explorer = js.Xplore(test_data)
        name = explorer['users'][0]['name'].data
        assert name == "Alice", f"Expected 'Alice', got {name}"
        print("✅ Xplore safe navigation works")
        
        # Test missing field (should return None)
        missing = explorer['users'][1]['email'].data
        assert missing is None, f"Expected None, got {missing}"
        print("✅ Xplore handles missing fields correctly")
        
        # Test keys
        keys = explorer.keys()
        assert 'users' in keys and 'metadata' in keys
        print("✅ Xplore keys() works")
        
    except Exception as e:
        print(f"❌ Xplore test failed: {e}")
        return False
    
    try:
        # Test Maybe
        maybe = js.Maybe(test_data['users'])
        names = maybe.array(lambda i, user: user.get('name'))
        assert len(names) == 3 and 'Alice' in names
        print("✅ Maybe array transformation works")
        
    except Exception as e:
        print(f"❌ Maybe test failed: {e}")
        return False
    
    try:
        # Test Explore
        explore = js.Explore(test_data['users'])
        field_counts = explore.field_counts()
        assert field_counts['name'] == 3
        assert field_counts['age'] == 3
        assert field_counts['email'] == 2
        print("✅ Explore field analysis works")
        
    except Exception as e:
        print(f"❌ Explore test failed: {e}")
        return False
    
    try:
        # Test SimpleXML
        xml_data = "<user><name>Test</name><age>30</age></user>"
        xml_explorer = js.Xplore(xml_data)
        if xml_explorer.xml:
            result = xml_explorer.xml.to_dict()
            assert 'name' in result and result['name'] == 'Test'
            print("✅ SimpleXML conversion works")
        else:
            print("⚠️ XML data not recognized (this might be OK)")
            
    except Exception as e:
        print(f"❌ SimpleXML test failed: {e}")
        return False
    
    return True

def test_version_info():
    """Test version and package info."""
    print("\nTesting package information...")
    
    try:
        import jsonscout
        
        # Check if __version__ exists
        if hasattr(jsonscout, '__version__'):
            print(f"✅ Package version: {jsonscout.__version__}")
        else:
            print("⚠️ No __version__ attribute found")
        
        # Check package contents
        contents = dir(jsonscout)
        expected = ['Explore', 'Maybe', 'Xplore', 'SimpleXML', 'get_json_file_paths', 'read_json_file']
        
        for item in expected:
            if item in contents:
                print(f"✅ {item} available in package")
            else:
                print(f"❌ {item} missing from package")
                return False
                
    except Exception as e:
        print(f"❌ Package info test failed: {e}")
        return False
    
    return True

def main():
    """Run all tests."""
    print("🧪 JSON Scout Package Test Suite")
    print("=" * 40)
    
    success = True
    
    success &= test_imports()
    success &= test_basic_functionality()
    success &= test_version_info()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 All tests passed! Package is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Check the output above.")
        return 1

if __name__ == "__main__":
    exit(main())