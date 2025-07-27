#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Portfolio Application
Tests all portfolio backend APIs as specified in the review request.
"""

import requests
import json
import sys
import os
from datetime import datetime

# Get backend URL from frontend .env file
def get_backend_url():
    try:
        with open('/app/frontend/.env', 'r') as f:
            for line in f:
                if line.startswith('REACT_APP_BACKEND_URL='):
                    return line.split('=', 1)[1].strip()
    except Exception as e:
        print(f"Error reading frontend .env file: {e}")
        return None

# Test configuration
BACKEND_URL = get_backend_url()
if not BACKEND_URL:
    print("❌ Could not get backend URL from frontend/.env")
    sys.exit(1)

print(f"🔗 Testing backend at: {BACKEND_URL}")

class PortfolioAPITester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.test_results = []
        
    def log_test(self, test_name, success, details):
        """Log test results"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        
        self.test_results.append({
            'test': test_name,
            'success': success,
            'details': details,
            'timestamp': datetime.now().isoformat()
        })
    
    def test_health_check(self):
        """Test GET /api/health endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'status' in data and data['status'] == 'healthy':
                    self.log_test("Health Check", True, f"Status: {data.get('status')}, Message: {data.get('message')}")
                    return True
                else:
                    self.log_test("Health Check", False, f"Invalid response format: {data}")
                    return False
            else:
                self.log_test("Health Check", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Health Check", False, f"Request failed: {str(e)}")
            return False
    
    def test_portfolio_profile(self):
        """Test GET /api/portfolio/profile endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/profile", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Validate required fields
                required_fields = ['id', 'about', 'contact', 'education', 'created_at', 'updated_at']
                missing_fields = [field for field in required_fields if field not in data]
                
                if missing_fields:
                    self.log_test("Portfolio Profile", False, f"Missing required fields: {missing_fields}")
                    return False
                
                # Validate contact info
                contact = data.get('contact', {})
                contact_fields = ['email', 'phone', 'linkedin']
                missing_contact = [field for field in contact_fields if field not in contact]
                
                if missing_contact:
                    self.log_test("Portfolio Profile", False, f"Missing contact fields: {missing_contact}")
                    return False
                
                # Validate education info
                education = data.get('education', {})
                education_fields = ['degree', 'university', 'period']
                missing_education = [field for field in education_fields if field not in education]
                
                if missing_education:
                    self.log_test("Portfolio Profile", False, f"Missing education fields: {missing_education}")
                    return False
                
                # Check if it's Riddhi Kalra's profile
                about_text = data.get('about', '').lower()
                if 'riddhi' not in about_text and 'tata technologies' not in about_text:
                    self.log_test("Portfolio Profile", False, "Profile doesn't match expected Riddhi Kalra data")
                    return False
                
                self.log_test("Portfolio Profile", True, f"Profile loaded for: {contact.get('email', 'N/A')}")
                return True
                
            else:
                self.log_test("Portfolio Profile", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Portfolio Profile", False, f"Request failed: {str(e)}")
            return False
    
    def test_projects(self):
        """Test GET /api/portfolio/projects endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/projects", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Projects", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Projects", False, "No projects found")
                    return False
                
                # Validate project structure
                for i, project in enumerate(data):
                    required_fields = ['id', 'title', 'description', 'highlights', 'technologies', 'created_at', 'updated_at']
                    missing_fields = [field for field in required_fields if field not in project]
                    
                    if missing_fields:
                        self.log_test("Projects", False, f"Project {i} missing fields: {missing_fields}")
                        return False
                    
                    if not isinstance(project['highlights'], list) or not isinstance(project['technologies'], list):
                        self.log_test("Projects", False, f"Project {i} highlights/technologies not lists")
                        return False
                
                # Check for expected projects
                project_titles = [p['title'].lower() for p in data]
                expected_projects = ['middleware api suite', 'microservices with spring boot', 'platform migration']
                
                found_projects = []
                for expected in expected_projects:
                    for title in project_titles:
                        if expected in title:
                            found_projects.append(expected)
                            break
                
                if len(found_projects) < 2:  # At least 2 expected projects should be found
                    self.log_test("Projects", False, f"Expected projects not found. Found: {found_projects}")
                    return False
                
                self.log_test("Projects", True, f"Found {len(data)} projects including expected ones: {found_projects}")
                return True
                
            else:
                self.log_test("Projects", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Projects", False, f"Request failed: {str(e)}")
            return False
    
    def test_skills(self):
        """Test GET /api/portfolio/skills endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/skills", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Skills", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Skills", False, "No skills found")
                    return False
                
                # Validate skill category structure
                for i, skill_category in enumerate(data):
                    required_fields = ['id', 'category', 'items', 'created_at', 'updated_at']
                    missing_fields = [field for field in required_fields if field not in skill_category]
                    
                    if missing_fields:
                        self.log_test("Skills", False, f"Skill category {i} missing fields: {missing_fields}")
                        return False
                    
                    if not isinstance(skill_category['items'], list):
                        self.log_test("Skills", False, f"Skill category {i} items not a list")
                        return False
                
                # Check for expected skill categories
                categories = [s['category'].lower() for s in data]
                expected_categories = ['programming', 'frameworks', 'tools']
                
                found_categories = []
                for expected in expected_categories:
                    for category in categories:
                        if expected in category:
                            found_categories.append(expected)
                            break
                
                if len(found_categories) < 2:  # At least 2 expected categories should be found
                    self.log_test("Skills", False, f"Expected skill categories not found. Found: {found_categories}")
                    return False
                
                self.log_test("Skills", True, f"Found {len(data)} skill categories including: {found_categories}")
                return True
                
            else:
                self.log_test("Skills", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Skills", False, f"Request failed: {str(e)}")
            return False
    
    def test_achievements(self):
        """Test GET /api/portfolio/achievements endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/achievements", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Achievements", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Achievements", False, "No achievements found")
                    return False
                
                # Validate achievement structure
                for i, achievement in enumerate(data):
                    required_fields = ['id', 'title', 'description', 'created_at', 'updated_at']
                    missing_fields = [field for field in required_fields if field not in achievement]
                    
                    if missing_fields:
                        self.log_test("Achievements", False, f"Achievement {i} missing fields: {missing_fields}")
                        return False
                
                # Check for expected achievements
                achievement_titles = [a['title'].lower() for a in data]
                expected_achievements = ['champion', 'snowflake', 'integration']
                
                found_achievements = []
                for expected in expected_achievements:
                    for title in achievement_titles:
                        if expected in title:
                            found_achievements.append(expected)
                            break
                
                if len(found_achievements) < 2:  # At least 2 expected achievements should be found
                    self.log_test("Achievements", False, f"Expected achievements not found. Found: {found_achievements}")
                    return False
                
                self.log_test("Achievements", True, f"Found {len(data)} achievements including: {found_achievements}")
                return True
                
            else:
                self.log_test("Achievements", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Achievements", False, f"Request failed: {str(e)}")
            return False
    
    def test_certifications(self):
        """Test GET /api/portfolio/certifications endpoint"""
        try:
            response = self.session.get(f"{self.base_url}/api/portfolio/certifications", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if not isinstance(data, list):
                    self.log_test("Certifications", False, "Response is not a list")
                    return False
                
                if len(data) == 0:
                    self.log_test("Certifications", False, "No certifications found")
                    return False
                
                # Validate certification structure
                for i, certification in enumerate(data):
                    required_fields = ['id', 'name', 'issuer', 'created_at', 'updated_at']
                    missing_fields = [field for field in required_fields if field not in certification]
                    
                    if missing_fields:
                        self.log_test("Certifications", False, f"Certification {i} missing fields: {missing_fields}")
                        return False
                
                # Check for expected certifications
                cert_names = [c['name'].lower() for c in data]
                expected_certs = ['ui design', 'sql', 'cybersecurity']
                
                found_certs = []
                for expected in expected_certs:
                    for name in cert_names:
                        if expected in name:
                            found_certs.append(expected)
                            break
                
                if len(found_certs) < 2:  # At least 2 expected certifications should be found
                    self.log_test("Certifications", False, f"Expected certifications not found. Found: {found_certs}")
                    return False
                
                self.log_test("Certifications", True, f"Found {len(data)} certifications including: {found_certs}")
                return True
                
            else:
                self.log_test("Certifications", False, f"HTTP {response.status_code}: {response.text}")
                return False
                
        except Exception as e:
            self.log_test("Certifications", False, f"Request failed: {str(e)}")
            return False
    
    def test_error_handling(self):
        """Test error handling for invalid requests"""
        try:
            # Test invalid endpoint
            response = self.session.get(f"{self.base_url}/api/portfolio/invalid", timeout=10)
            
            if response.status_code == 404:
                self.log_test("Error Handling - Invalid Endpoint", True, "Correctly returns 404 for invalid endpoint")
                return True
            else:
                self.log_test("Error Handling - Invalid Endpoint", False, f"Expected 404, got {response.status_code}")
                return False
                
        except Exception as e:
            self.log_test("Error Handling - Invalid Endpoint", False, f"Request failed: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting Portfolio Backend API Tests")
        print("=" * 50)
        
        tests = [
            self.test_health_check,
            self.test_portfolio_profile,
            self.test_projects,
            self.test_skills,
            self.test_achievements,
            self.test_certifications,
            self.test_error_handling
        ]
        
        passed = 0
        total = len(tests)
        
        for test in tests:
            if test():
                passed += 1
            print()  # Add spacing between tests
        
        print("=" * 50)
        print(f"📊 Test Results: {passed}/{total} tests passed")
        
        if passed == total:
            print("🎉 All tests passed! Backend APIs are working correctly.")
            return True
        else:
            print(f"⚠️  {total - passed} tests failed. Check the details above.")
            return False
    
    def save_results(self, filename="backend_test_results.json"):
        """Save test results to file"""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'timestamp': datetime.now().isoformat(),
                    'backend_url': self.base_url,
                    'total_tests': len(self.test_results),
                    'passed_tests': sum(1 for r in self.test_results if r['success']),
                    'results': self.test_results
                }, f, indent=2)
            print(f"📄 Test results saved to {filename}")
        except Exception as e:
            print(f"❌ Failed to save results: {e}")

def main():
    """Main test execution"""
    tester = PortfolioAPITester(BACKEND_URL)
    
    try:
        success = tester.run_all_tests()
        tester.save_results("/app/backend_test_results.json")
        
        if success:
            print("\n✅ All backend APIs are working correctly!")
            sys.exit(0)
        else:
            print("\n❌ Some backend APIs have issues!")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()