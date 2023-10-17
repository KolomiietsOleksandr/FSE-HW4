import requests
import json

class CustomDataFetcher:
    def get_custom_data_from_url(self, base_url):
        max_offset = 0
        custom_all_data = []
        while True:
            url = f"{base_url}?offset={max_offset}"
            response = requests.get(url)
            if response.status_code == 200:
                json_content = response.text
                try:
                    container = json.loads(json_content)
                    custom_user_data = container["data"]
                    if not custom_user_data:
                        break
                    custom_all_data.extend(custom_user_data)
                    max_offset += len(custom_user_data)
                except json.JSONDecodeError as ex:
                    print(f"Failed to parse JSON: {ex}")
            else:
                print(f"Failed to fetch data for offset {max_offset}")
        return custom_all_data
