# flask-scrapers-api

<!-- ABOUT THE PROJECT -->
## About The Project
This scrapper is a part of the [top video generator app](https://github.com/mage1711/video-generator-app) it scraps lists from https://www.metacritic.com/

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Getting Started

To test the scrapper send a post request to https://flask-scrapers.herokuapp.com/scrap <br/>
the post request should contain a condensed list url from https://www.metacritic.com/ </br>
a response will return a json with this structure 
```json
[
    {
        "filename": "Chicory A Colorful Tale",
        "name": "Chicory: A Colorful Tale",
        "platform": "PlayStation 5",
        "playlist_found": false,
        "position": 0,
        "rating": "87",
        "release_date": [
            "June",
            "10",
            "2021"
        ],
        "url": "https://www.metacritic.com/game/playstation-5/chicory-a-colorful-tale",
        "video_found": false
    },
    {
        "filename": "Mass Effect Legendary Edition",
        "name": "Mass Effect Legendary Edition",
        "platform": "PC",
        "playlist_found": true,
        "playlist_videos": [
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/02/01/646528/trailer_masseffectLE_202121_4000.mp4",
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/04/13/649310/trailer_masseffectlegend_comparison_4000.mp4",
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/05/12/649991/MELE1_CharacterCreatorGameplay_8000.mp4",
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/05/13/650014/GraphicsComp_MassEffect1_20210513_8000.mp4"
        ],
        "position": 1,
        "rating": "86",
        "release_date": [
            "May",
            "14",
            "2021"
        ],
        "url": "https://www.metacritic.com/game/pc/mass-effect-legendary-edition",
        "video_found": true,
        "video_url": "https://static-gamespotvideo.cbsistatic.com/vr/2021/02/09/646974/Feature_MELEComp_20210208_8000.mp4"
    },
    {
        "filename": "Final Fantasy VII Remake Intergrade",
        "name": "Final Fantasy VII Remake Intergrade",
        "platform": "PlayStation 5",
        "playlist_found": true,
        "playlist_videos": [
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/03/22/648808/trailer_ff7remakeintegradeextended_4000.mp4",
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/06/09/650625/PS5_FF7RScorpionFight4K_8000.mp4",
            "https://static-gamespotvideo.cbsistatic.com/vr/2021/06/10/650666/Feature_FF7RIGFXComparison_20210609_8000.mp4"
        ],
        "position": 2,
        "rating": "89",
        "release_date": [
            "June",
            "10",
            "2021"
        ],
        "url": "https://www.metacritic.com/game/playstation-5/final-fantasy-vii-remake-intergrade",
        "video_found": true,
        "video_url": "https://static-gamespotvideo.cbsistatic.com/vr/2021/05/17/650075/Trailer_FF7intergrade_finaltrailer_4000.mp4"
    }
]
```


  
