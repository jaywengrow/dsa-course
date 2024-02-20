function validate(node) {
    if (!node) { return true; }

    if ((!node.leftChild || node.leftChild.value < node.value) && (!node.rightChild || node.rightChild.value > node.value)) {
        return validate(node.leftChild) && validate(node.rightChild);
    } else {
        return false;
    }
}

export default validate;