import requests

# Replace with your actual values
ACCESS_TOKEN = "EAAHMOgGDm30BOZBgIOGGx72gpFgqapNyQZA3QTzOHVvzgUUiZBl57RWqZCakRgen6Ny4CYthkYDQWZCeKqR7MinhrBzPFSEMXcNS1Uyki87S1TQ5SmzrkZBtOsz5aZAFJJhcmWgFLZAh02KfoRE7BCPuvr2gFUns033Fm3BObeZCApyml8zRpixDDuZC4eP9MgH0797qvknpjzLZCg6H339STlOagwcYu0ZD"
FACEBOOK_PAGE_ID = "your_facebook_page_id"

# Get the Instagram Business Account ID
def get_instagram_business_id():
    url = f"https://graph.facebook.com/v19.0/{FACEBOOK_PAGE_ID}?fields=instagram_business_account&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    
    if "instagram_business_account" in data:
        instagram_id = data["instagram_business_account"]["id"]
        print(f"✅ Instagram Business Account ID: {instagram_id}")
        return instagram_id
    else:
        print(f"❌ Error: {data}")
        return None

if __name__ == "__main__":
    get_instagram_business_id()
