
const objectsEqual = (o1, o2) => Object.keys(o1).length
=== Object.keys(o2).length && Object.keys(o1).every((p) => o1[p] === o2[p]);

function areAnagrams(firstString, secondString) { 
    const firstWordHashTable = {};
    const secondWordHashTable = {};

    for (const char of firstString) { 
        if (firstWordHashTable[char]) {
            firstWordHashTable[char] += 1; 
        } else {
            firstWordHashTable[char] = 1;
        }
    }

    for (const char of secondString) {
        if (secondWordHashTable[char]) {
            secondWordHashTable[char] += 1;
        } else {
            secondWordHashTable[char] = 1;
        }
    }

    return objectsEqual(firstWordHashTable, secondWordHashTable);
}
