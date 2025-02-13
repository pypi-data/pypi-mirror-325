
import requests
import re
import time
from pathlib import Path
from urllib.parse import quote

class TikTakNawaf:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Referer": "https://www.tiktok.com/",
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.session.headers.update(self.headers)

    def get_video_info(self, video_url):
        api_url = f"https://www.tikwm.com/api/?url={quote(video_url)}"
        try:
            headers = {k: str(v).encode("utf-8").decode("utf-8") for k, v in self.headers.items()} 
            response = self.session.get(api_url, headers=headers)
            if response.status_code != 200:
                print(f"❌ HTTP Error: {response.status_code} - {response.text}")
                return None

            try:
                data = response.json()
            except ValueError:
                print(f"❌ Response is not JSON: {response.text}")
                return None

            if "data" in data and "play" in data["data"]:
                return data["data"]["play"]
            else:
                print("❌ Could not find the direct video link. Check the URL.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Error while extracting video link: {e}")
            return None
    
    def download_video(self, video_url, output_path="downloads"):
    	video_link = self.get_video_info(video_url)
    	if not video_link:
        	print("❌ فشل تحميل الفيديو. تحقق من الرابط.")
        	return False  # إرجاع False عند الفشل

    	Path(output_path).mkdir(parents=True, exist_ok=True)
    	video_name = f"tiktok_video_{int(time.time())}.mp4"
    	output_file = Path(output_path) / video_name

    	try:
        	video_response = self.session.get(video_link, stream=True)
        	if video_response.status_code == 403:
            		print("❌ فشل تحميل الفيديو. كود الحالة: 403")
            		return False  # إرجاع False عند الفشل
        
        	with open(output_file, "wb") as file:
            		for chunk in video_response.iter_content(chunk_size=1024):
                		if chunk:
                    			file.write(chunk)
                    
        	print(f"✅ تم تحميل الفيديو بنجاح: {output_file}")

        	# ✅ التأكد من أن الملف تم تحميله بنجاح قبل إرجاع True
        	if output_file.exists() and output_file.stat().st_size > 0:
            		return True
        	else:
            		print("⚠️ الملف تم إنشاؤه ولكنه فارغ!")
            		return False

    	except requests.exceptions.RequestException as e:
        	print(f"❌ خطأ أثناء تحميل الفيديو: {e}")
        	return False  # إرجاع False عند الخطأ



