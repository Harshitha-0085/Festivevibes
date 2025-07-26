#!/usr/bin/env python3
"""
Test script for FestiveVibe application
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Streamlit: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Pandas: {e}")
        return False
    
    try:
        from PIL import Image
        print("✅ PIL imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import PIL: {e}")
        return False
    
    return True

def test_app_structure():
    """Test if the main app file exists and has required functions"""
    if not os.path.exists("app.py"):
        print("❌ app.py file not found")
        return False
    
    print("✅ app.py file found")
    
    # Try to import the main functions
    try:
        import app
        print("✅ app.py imported successfully")
        
        # Check if main functions exist
        if hasattr(app, 'get_festival_data'):
            print("✅ get_festival_data function found")
        else:
            print("❌ get_festival_data function not found")
            return False
        
        if hasattr(app, 'show_homepage'):
            print("✅ show_homepage function found")
        else:
            print("❌ show_homepage function not found")
            return False
        
        if hasattr(app, 'show_festival_explorer'):
            print("✅ show_festival_explorer function found")
        else:
            print("❌ show_festival_explorer function not found")
            return False
        
        if hasattr(app, 'show_submit_form'):
            print("✅ show_submit_form function found")
        else:
            print("❌ show_submit_form function not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to import app.py: {e}")
        return False

def test_festival_data():
    """Test if festival data is properly structured"""
    try:
        import app
        festivals = app.get_festival_data()
        
        if not isinstance(festivals, dict):
            print("❌ Festival data is not a dictionary")
            return False
        
        print(f"✅ Found {len(festivals)} festivals")
        
        # Check structure of first festival
        first_festival = list(festivals.values())[0]
        required_keys = ['telugu_name', 'date', 'description', 'telugu_description', 
                        'regions', 'rituals', 'foods', 'attire', 'dances', 'events']
        
        for key in required_keys:
            if key not in first_festival:
                print(f"❌ Missing required key: {key}")
                return False
        
        print("✅ Festival data structure is correct")
        return True
        
    except Exception as e:
        print(f"❌ Error testing festival data: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing FestiveVibe Application")
    print("=" * 40)
    
    tests = [
        ("Import Dependencies", test_imports),
        ("Application Structure", test_app_structure),
        ("Festival Data", test_festival_data)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            print(f"✅ {test_name} passed")
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\n🚀 To run the application:")
        print("   streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 