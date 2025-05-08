# HoPE-MQTT-Project
Home Planet Environmental Monitoring System Project, a basic wireless communication simulator project. 

## Installation:
 - Change directory to the project directory (where `package.json` is located in)
 - (project dir)$ *`npm install`*
     - Type this command to install node-red dashboard and its dependencies for UI
     - A folder named *node_modules* will appear (if there is not). NPM will scan *package.json* files, from the project's and recursively all the dependencies', download them and populate that folder with the dependencies. The page and scripts refer to the modules (such as Three.js) that are inside this folder, so gathering the dependencies is essential.

<br>

### Start:
 - At wokwi/ folder open the url shortcut for Wokwi Emulator to start ESP32 sensors reading
 - (TO BE EDITED) 
 - (project dir)$ *`npm run start`*
 - This will start the subscriptor reading messages sent by ESP32 by subscribing the MQTT channel.
 - Then:
     - Go to http://localhost:{port}/ui (depending on the what port the server listens at, currently 1883) in a web browser on the same network.