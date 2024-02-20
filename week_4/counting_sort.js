function sortTemperatures(array) {
    const hashTable = {};
  
    for (const temperature of array) {
      if (hashTable[temperature]) {
        hashTable[temperature] += 1;
      } else {
        hashTable[temperature] = 1;
      }
    }
  
    const sortedTemperatures = [];
    let temperature = 95;
  
    while (temperature <= 105) {
      if (hashTable[temperature]) {
        for (let i = 0; i < hashTable[temperature]; i += 1) {
          sortedTemperatures.push(temperature);
        }
      }
  
      temperature += 1;
    }
  
    return sortedTemperatures;
  }

console.log(sortTemperatures([98, 99, 95, 105, 104, 98, 101, 99, 100, 97]));
