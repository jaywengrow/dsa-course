function groupSort(array) {
    const hashTable = {};
    const newArray = [];
  
    for (const value of array) {
      if (hashTable[value]) {
        hashTable[value] += 1;
      } else {
        hashTable[value] = 1;
      }
    }
  
    for (const key of Object.keys(hashTable)) {
      const count = hashTable[key];
      for (let i = 0; i < count; i += 1) {
        newArray.push(key);
      }
    }
  
    return newArray;
  }

console.log(groupSort(["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]));
  