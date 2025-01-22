from bs4 import BeautifulSoup
import requests
import time
import csv
import pandas as pd

def international_box_office_performance():
    # URL to scrape
    url = 'https://www.boxofficemojo.com/intl/?ref_=bo_nb_ydw_tab'
    # Request headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        rows = soup.find_all('tr')
        current_weekend = None

        data = []
        
        for row in rows:
            weekend_heading = row.find('th', class_="a-size-base mojo-table-header")
            if weekend_heading:
                current_weekend = weekend_heading.text.strip()
                print(f"\n{current_weekend}")
                continue
            columns = row.find_all('td')
            if columns:
                area = columns[0].text.strip()
                weekend = columns[1].text.strip()
                releases = columns[2].text.strip()
                top_release = columns[3].text.strip()
                distributor = columns[4].text.strip()
                money_made = columns[5].text.strip()
                link_tag = columns[1].find('a')
                more_info = f"https://www.boxofficemojo.com{link_tag['href']}" if link_tag and link_tag.has_attr('href') else "N/A"

                data.append({
                    "Area": area,
                    "Weekend": weekend,
                    "Releases": releases,
                    "Top Release": top_release,
                    "Distributor": distributor,
                    "Weekend_Gross": money_made,
                    "More Info": more_info
                })

                # Print the data
                print(
                    f"Area: {area} | Weekend: {weekend} | Releases: {releases} | "
                    f"Top Release: {top_release} | Distributor: {distributor} | Weekend Gross: {money_made} | more info: {more_info}"
                )
        
        data_frame = pd.DataFrame(data)
        data_frame.to_csv("box_office_data.csv", index=False)
        print("\nData saved to box_office_data.csv")
        
    else:
        print("Failed to fetch row data")

if __name__ == '__main__':
    international_box_office_performance()
        
