// START:P1
function traverse(node) {
    if (!node) { return; }
  
    traverse(node.leftChild);
    console.log(node.value);
    traverse(node.rightChild);
  }
  // END:P1
  export default traverse;
  
