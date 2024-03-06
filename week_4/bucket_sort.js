function bucketSort(array) {
  const hashTable = {};
  const newArray = [];

  for (const value of array) {
    if (hashTable[value]) {
      hashTable[value] += 1;
    } else {
      hashTable[value] = 1;
    }
  }

  
  for (const char of ["a", "b", "c", "d"]) {
    const count = hashTable[char];
    for (let i = 0; i < count; i += 1) {
      newArray.push(char);
    }
  }

  return newArray;
}

console.log(bucketSort(["a", "c", "d", "b", "b", "c", "a", "d", "c", "b", "a", "d"]));

{"a": 3, "b": 3, "d": 4}

newArray = ["a", "a", "a", "b", "b", "b"]
2N -> O(N)
