function etl2(data) {
    const output = {};

    for (const [key, values] of Object.entries(data)) {
        for (const value of values) {
            console.log(value)
            output[value.toLowerCase()] = key;
        }
    }

    return output;

}


input = {
    1: ["A", "E"],
    2: ["D", "G"]
}

console.log(etl2(input))

// # expected output:
// # {
// # 'a': 1,
// # 'd': 2,
// # 'e': 1,
// # 'g': 2
// # }