# CSGO-Console-Parser

## Description
A live damage tracker that scrapes the CSGO Console

During the round, damage totals will be streamed in the format:

    Damage Given: [DAMAGED_PLAYER_NAME] DAMAGE_AMOUNT in HIT_COUNT hits
  
At the end of a round it will print a round report with aggregated damage given/received numbers

    ---- Round # Report ----
    Damage Given:
    	PLAYER_NAME_ONE: 142 in 2 hits
    	Total Damage: 142 in 2 hits
    Damage Received:
    	PLAYER_NAME_ONE: 74 in 4 hits
    	PLAYER_NAME_TWO: 208 in 2 hits
    	Total Damage: 282 in 6 hits


## Configuration
Ensure you're running CSGO with the -condebug launch argument

By default the parse will look for a config named 'csgo-parser.conf' in the resources folder

Create a config based on the included example and fill in the path to where console.log is created

## Run Options
By default the parser will look for a config named 'csgo-parser.conf' in the resources folder

You may, however, include a custom location with the -config option

    python start_parser.py -config 'C:/The/Path/To/Your/Config.conf'
  
