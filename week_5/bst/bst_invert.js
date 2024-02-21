function invert(node) {
    if (!node) { return; }

    const temp = node.leftChild;
    node.leftChild = node.rightChild;
    node.rightChild = temp;
    
    invert(node.leftChild);
    invert(node.rightChild);
}

export default invert;