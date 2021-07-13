# pi-home-status-bar
A Pi Zero with a Blinkt! LED hat that allows for visual feedback on changes in Home Assistant instance. 

## Todo:
- Create connect script to the HA MQTT broker and determine topic for Pi Status Bar to listen to
- Determine best MQTT topic that conforms with other topics already in place on HA instance.
- Determine all possible display options for Status Bar
  - "Armed" whenever alarm is primed and ready to trigger. Blinks orange twice then stays lit
  - "Pending" whenever alarm is allowing users to exit premises without trigerring alarm. Slowly to rapidly blinks yellow to indicate time left
  - "Disarmed" whenever alarm is disarmed, rapidly fades in as green then slowly fades to nothing
  - "Disconnected" whenever Pi Status Bar is unable to connect to the MQTT broker, flashes light blue in intervals
- Create small loops for when the MQTT topic is set to strings mentioned above.
- Create wall mount for pi zero + case
