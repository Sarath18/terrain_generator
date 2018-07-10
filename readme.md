# Terrain Generator
A wizard written in python that helps in creating terrains in Gazebo with appropriate textures and lighting. 
Terrains are generated using the heightmaps provided by the user which is stored either on disk or a url.

### Working
The wizard basically does the folowing:
- Ask you simple questions regarding the model
- Creates the model and saves it in your `.gazebo/models ` folder
- Creates a `.world` file at the destination path provied by the user

### Requirements:
- Python
- Gazebo 7.0 or higher
- lxml
- urllib
