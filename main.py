import importlib  
playyt = importlib.import_module("play-yt")
searchyt = importlib.import_module("search-yt")

result = searchyt.run(5)
playyt.main(result['vid_id'])