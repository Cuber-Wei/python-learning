from time import sleep
import requests

# 音乐地址：http://music.163.com/song/media/outer/url?id=
# "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="

webURL = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
res = requests.post(
    webURL,
    data={
        "params": "Rm83G6utIBSbb0/vioM94ENwyOQJHC9B7vMaS+Fdgi8D2bv9YuglE5t5jMi2DmmS7KL/6YVzvIOcI9DGU5scbU7yIS3UMFLnd4ICZiRfLZ8zCztknJeQRAgLjmQURF0gzIwspeIS9HRtzU5hlOElaOaANWURG9tf5FrOhq5G6mr8X1iYEeO4DkLhVE3+0L4fhZqhcDe4XXc4hT4PFPmRy7POZYQ3TbvHI75laskuO3Ah76fB9LLJ7RLeS8X3Sfkzpv27pdAk3r3cQMixIP0FPA==",
        "encSecKey": "084138fa97aedb9fd6586934ef32bff21c1ff3fd64d8a08cfc5041ae6b9d7b4537f46803e1384dd048418f3ccf8f42eb034a812cd96399166c07e4d1fa8b326ce9e09854820e5ea602d3d6ac47a3773b12c3c0e899157452c0f65b37d34e57d372509bdbc97557930f3c5fff29e26886d037323740e070e31cc225300082c9e3"
    }
).json()

# 筛选id 歌手名 歌曲名
result = res['result']['songs']

for each in result:
    sleep(2)
    music_name = each["name"]
    music_id = each["id"]
    url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(
        music_id)
    mp3 = requests.get(url).content
# 保存
    with open("C:\\Users\\CuberWei\\Desktop\\网易云音乐\\" + music_name + ".mp3", "wb") as file:
        file.write(mp3)
    print(music_name + "\t下载完成!")
print("本轮下载已完成!")
