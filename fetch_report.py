import requests

def get_food_report():
    # API URL targeting a single record
    url = "https://api.fda.gov/food/enforcement.json?limit=1"
    
    print("Connecting to openFDA API...")
    
    try:
        response = requests.get(url)
        
        # Step 3: Connection Test (Verification)
        if response.status_code == 200:
            data = response.json()
            # Navigate the JSON structure to get the first result
            report = data['results'][0]
            
            # Step 4: Specific Data Extraction
            print("\n" + "="*50)
            print("FDA ENFORCEMENT REPORT SUMMARY")
            print("="*50)
            print(f"RECALLING FIRM: {report.get('recalling_firm')}")
            print(f"LOCATION:      {report.get('city')}, {report.get('state')}")
            print(f"STATUS:        {report.get('status')}")
            print(f"REASON:        {report.get('reason_for_recall')}")
            print(f"DISTRIBUTION:  {report.get('distribution_pattern')}")
            print(f"CLASSIFICATION:{report.get('classification')}")
            print("="*50)
            
        else:
            print(f"Error: API returned status code {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred during extraction: {e}")

if __name__ == "__main__":
    get_food_report()
