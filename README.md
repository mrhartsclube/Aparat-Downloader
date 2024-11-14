### Aparat Video Downloader Script
This script is made to download best quality available for videos from [aparat.com](https://www.aparat.com "آپارات - سرویس اشتراک ویدیو"). Needs two libraries to function and you can simply install it using this command:

```powershell
pip install tqdm requests
```

`tqdm` is used for generating progress bar, and `requests` is used for sending requests for downloading videos.
The whole code is fully commented for ones who like to study or expand it further.

### Downloading Playlists
If you are trying to download a playlist from [aparat.com](https://www.aparat.com "آپارات - سرویس اشتراک ویدیو") you'll have a link like [https://www.aparat.com/playlist/7382665](https://www.aparat.com/playlist/7382665, "ویچر | The Witcher - لیست پخش"), navigate to the link in your browser and run this code in the console after the page fully loaded.

```javascript
videoHashes = [];
$$("ul.playlist-list a.titled-link.thumb.default.video-playlist").forEach(a =>
  videoHashes.push(
    a.href
      .replace("https://www.aparat.com/v/", "")
      .replace("?playlist=" + window.location.toString().split("/")[4], "")
  )
);
outputString = "";
videoHashes.forEach(item => (outputString += item + ","));
console.log(outputString.slice(0, -1));
```
Then you'll get a list of comma separated video hashes like this:

```plaintext
q42nvs6,y808x93,d0VO3,f99579n,m2jke,g33i4zn,Q3baw,f92634d,z759rsu,m917y15,r45og2d,UIx5z,z763oyd,h25bzi7,w59r97s,b6601wi,Mdbna,f35w177,l51tn6z,a067src,a800tya,rfLTF,47yY3,TBMg0
```

Then in powershell or command prompt run this code:

```powershell
python playlist_downloader.py q42nvs6,y808x93,d0VO3,f99579n,m2jke,g33i4zn,Q3baw,f92634d,z759rsu,m917y15,r45og2d,UIx5z,z763oyd,h25bzi7,w59r97s,b6601wi,Mdbna,f35w177,l51tn6z,a067src,a800tya,rfLTF,47yY3,TBMg0
```

It will download the best quality available for all the videos into a folder named `downloads` and shows a beautiful progress bar for each download.

### Downloading Single Video
For a single video your URL looks like [https://www.aparat.com/v/sqy0yxq](https://www.aparat.com/v/sqy0yxq "آیا شفق قطبی رو میشه با چشم دید ؟") which contains the base address `https://www.aparat.com/v/` and video hash which in this example is `sqy0yxq`. 

Simply copy the video hash and run this command in your powershell or command prompt:

```powershell
python playlist_downloader.py sqy0yxq
```

It will download the best quality available for the video into a folder named `downloads` and shows a beautiful progress bar for download.

### Naming Output Files
This script tries to use video titles as their respective file names, you can edit or change file names by uncommenting line 44 and changing it to your will, for example what I did for one session was the titles were all looked like this:

```plaintext
‫فصل 1 سریال ویچر قسمت 5 | The Witcher دوبله فارسی
```
But I wanted it to be like `SXXEXX` which is Season `XX` Episode `XX`, so as I knew it has 3 seasons and each season has 8 episodes I used this template `S0XE0X` and the season number was at index `4` and episode number was at index `22` so I added:

```python
title = f"S0{title[4]}E0{title[22]}
```

You can change this line according to your video titles as you please or leave it commented for the full title as file names.
