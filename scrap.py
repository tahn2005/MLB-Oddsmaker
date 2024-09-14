import requests
from bs4 import BeautifulSoup

# Define the URL of the MLB player stats page
url = 'https://www.mlb.com/stats'  # Replace with the actual URL

# Send a GET request to the MLB stats page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Find a table with player stats
    # Update the selector based on the actual structure of the webpage
    stats_table = soup.find('table', {'class': 'stats'})  # Update class or ID based on the actual HTML

    if stats_table:
        # Extract headers
        headers = [header.get_text(strip=True) for header in stats_table.find_all('th')]
        
        # Extract rows
        rows = stats_table.find_all('tr')
        
        # Parse each row
        for row in rows[1:]:  # Skip header row
            columns = row.find_all('td')
            data = [column.get_text(strip=True) for column in columns]
            if data:
                player_stats = dict(zip(headers, data))
                print(player_stats)
    else:
        print("Stats table not found.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
