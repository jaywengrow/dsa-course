function sameTree(firstRoot, secondRoot) {
    if (!firstRoot && !secondRoot) { return true; }
    if ((firstRoot && !secondRoot) || (!firstRoot && secondRoot)) { return false;}

    return (firstRoot.value === secondRoot.value && sameTree(firstRoot.leftChild, secondRoot.leftChild) && sameTree(firstRoot.rightChild, secondRoot.rightChild));
}

export default sameTree;
