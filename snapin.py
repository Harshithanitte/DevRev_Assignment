
    
import requests

def create_work_item(title, description, priority, due_date):
    
    url = "https://api.devrev.ai/works.create"# Replace with the actual API endpoint
  
    headers = {
        "Authorization": "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFZVmlKd3N4RkY6ZGV2dS8xIiwiZXhwIjoxODA3MjExNDM5LCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL29pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTQyN2JkYWUzNGQ1MDRjZjgwNGM1MSIsImh0dHA6Ly9kZXZyZXYuYWkvYXV0aDBfdXNlcl9pZCI6Im9pZGN8cGFzc3dvcmRsZXNzfGVtYWlsfDY2MTQyN2JkYWUzNGQ1MDRjZjgwNGM1MSIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b19kb24iOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVlWaUp3c3hGRiIsImh0dHA6Ly9kZXZyZXYuYWkvZGV2b2lkIjoiREVWLTFZVmlKd3N4RkYiLCJodHRwOi8vZGV2cmV2LmFpL2RldnVpZCI6IkRFVlUtMSIsImh0dHA6Ly9kZXZyZXYuYWkvZGlzcGxheW5hbWUiOiI0bm0yMGlzMDU0IiwiaHR0cDovL2RldnJldi5haS9lbWFpbCI6IjRubTIwaXMwNTRAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9mdWxsbmFtZSI6IjRubTIwaXMwNTRAbm1hbWl0LmluIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjYwMzQzOSwiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMVlWaUp3c3hGRjp0b2tlbi9vdUJ6SDdOZyIsIm9yZ19pZCI6Im9yZ190VGZwZVpKRkdUQTh5SGJGIiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFZVmlKd3N4RkY6ZGV2dS8xIn0.ycp4jYwoPPoeean3whnKXuQ_c-TAT4pUci7onepSd8NM3jqlgd-nXf33fUFGw_U21UzclIu-5WVVIYkhzkNT4cUncD-GjFvhsbN1nfjaRh_6p6cUjSMsaAC0MzS9rYiIXNywxugXqd6ZGBONA3wyMs9NzA2ZHP4U21y7rGHgFyIeHEBbYaudAIMHslM3hJLrIBYhtRY2K0o73BGcjUH-Wjza4brzSDt_2sFqmxcePmfZfnCxLjuMRhajCqFtGmXtCRtasLekFSege2i4nu2MKKP8aoeUqqHTU9uLgVxQ4588BuLkI5ivEOG8TH-K6YN7tsjAvb_S13pTCwfrtEKEZA",  # Replace with your access token
        "Content-Type": "application/json"
    }
    payload = {
        "type": "task",
        "applies_to_part": "frontend UI",
        "owned_by": ["DEVU-1"],
        "title": title,
        "body": description,
        "priority": priority,
        "target_close_date": due_date

    }
   
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 201:
            print("Work item created successfully.")
        else:
            print(f"Failed to create work item. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    title = "Development Review for Feature X"
    description = "Review and test the implementation of Feature X"
    priority = "p1"
    due_date = "2024-04-15"

    create_work_item(title, description, priority, due_date)











