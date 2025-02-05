from yt_dlp import YoutubeDL
import os

def grab_shorts(channel_url, output_dir="downloads", quality="720p"):
    """
    Download YouTube Shorts from a channel
    quality options: "360p", "720p", "1080p"
    """
    os.makedirs(output_dir, exist_ok=True)
    
    format_map = {
        "360p": "mp4[height<=360]",
        "720p": "mp4[height<=720]",
        "1080p": "mp4[height<=1080]"
    }
    
    video_format = format_map.get(quality, "mp4[height<=720]")
    
    ydl_opts = {
        'format': video_format,
        'outtmpl': os.path.join(output_dir, '%(title)s-%(id)s.%(ext)s'),
        'ignoreerrors': True,
        'no_warnings': True,
        'extract_flat': 'in_playlist',
        'quiet': False,
        'force_generic_extractor': False,
        'extractor_args': {
            'youtube': {
                'skip': ['dash', 'hls'],
            }
        }
    }
    
    def is_shorts(url):
        return 'shorts' in url.lower()
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            playlist = ydl.extract_info(channel_url, download=False)
            
            if 'entries' in playlist:
                for entry in playlist['entries']:
                    if not entry:
                        continue
                        
                    video_url = f"https://www.youtube.com/watch?v={entry['id']}"
                    if is_shorts(entry.get('url', '') or entry.get('webpage_url', '')):
                        try:
                            print(f"\nAttempting to download: {entry.get('title', 'Unknown Title')}")
                            with YoutubeDL(ydl_opts) as video_ydl:
                                video_ydl.download([video_url])
                            print(f"Successfully downloaded: {entry.get('title', 'Unknown Title')}")
                        except Exception as e:
                            print(f"Failed to download {video_url}: {str(e)}")
                            continue
                            
        except Exception as e:
            print(f"An error occurred with the playlist: {str(e)}")