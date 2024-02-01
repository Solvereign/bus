const fs = require('fs');

// Specify the path to your JSON file
const jsonFilePath = 'bus_lines.json';

const bus_stop_json = "bus_lines_pretty.json";
// Read the JSON file
fs.promises.readFile(jsonFilePath, 'utf-8')
  .then(jsonString => {
    // Parse the JSON string
    const data = JSON.parse(jsonString);

    // Now 'data' contains the contents of your JSON file
    console.log(data[0]);

    return fs.promises.writeFile(bus_stop_json, JSON.stringify(data, null, 2), 'utf-8');
  })
  .then(() => {
    console.log('Modified data written to', bus_stop_json);
  })
  .catch(error => console.error('Error:', error));
